"""
For managing rds secrets with caching
- first checks environment if it is evailable
- then it checks in parameter store
- lastly it checks in secrets manager
"""

import json
import logging
import os
from functools import wraps
from typing import Any, Callable, Optional

import requests

from saral_utils.aws.parameter_store import ParameterStore
from saral_utils.aws.secrets_manager import SecretsManager
from saral_utils.utils.utils import get_env_var, get_my_env, get_my_region


def cache(func) -> Callable:

    @wraps(func)
    def _wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, dict):
            for k, v in result.items():
                key_name = k if k.startswith("RDS") else f"RDS_{k.upper()}"
                os.environ[key_name] = str(v)
        return result

    return _wrapper


class RDSSecrets:

    def __init__(
        self,
        secretid: str,
        branch: Optional[str] = None,
        my_env: Optional[str] = None,
        my_region: Optional[str] = None,
    ) -> None:
        self.secretid = secretid
        self.branch = branch or get_env_var("CIRCLE_BRANCH")
        self.branch = "main" if self.branch == "master" else self.branch
        self.my_env = my_env or get_my_env()
        self.my_region = my_region or get_my_region()
        self.username, self.password, self.host, self.port = self.fetch_secrets(
            frm_localhost_secrets_manager=True
        )

    @cache
    def get_secrets_frm_secrets_manager(self) -> dict[str, Any] | None:
        sm = SecretsManager(
            secret_id=self.secretid,
            branch=self.branch,
            my_env=self.my_env,
            my_region=self.my_region,
        )
        return sm.secrets.get(self.branch)

    def get_secrets_frm_env(self, key: str) -> str | None:
        return get_env_var(key, raise_error=False)

    def get_secrets_frm_localhost(
        self, frm_secret_manager: bool = True
    ) -> dict[str, dict[str, str]]:
        token = os.environ["AWS_SESSION_TOKEN"]
        headers = {"X-Aws-Parameters-Secrets-Token": token}
        http_port = os.getenv("PARAMETERS_SECRETS_EXTENSION_HTTP_PORT")
        if frm_secret_manager:
            secrets_ext_endpoint = f"http://localhost:{http_port}/secretsmanager/get?secretId={self.secretid}"
        else:
            secrets_ext_endpoint = f"http://localhost:{http_port}/systemsmanager/parameters/get?name={self.secretid}&withDecryption=true"
        r = requests.get(secrets_ext_endpoint, headers=headers)
        secret = json.loads(json.loads(r.text)["SecretString"])
        return secret.get(self.branch)

    @cache
    def get_secrets_frm_parameter_store(self) -> dict[str, str]:
        ps = ParameterStore(
            parameter_name=self.secretid,
            my_env=self.my_env,
            my_region=self.my_region,
            branch=self.branch,
        )
        secret = ps.parameters
        return secret.get(self.branch)  # type: ignore

    def fetch_secrets(
        self, frm_localhost_secrets_manager: bool = False
    ) -> tuple[str, str, str, int]:
        """Returns username, password, host, port"""
        keys = [f"RDS_{k.upper()}" for k in ["username", "password", "host", "port"]]
        username, password, host, port = [self.get_secrets_frm_env(k) for k in keys]
        port = port or 3306

        if any([username, password, host, port]):
            logging.warning("Secrets not found in environment")
            try:
                secrets = self.get_secrets_frm_localhost(
                    frm_secret_manager=frm_localhost_secrets_manager
                )
            except Exception as error:
                logging.warning(f"Secrets not found in localhost secrets manager.")
                try:
                    secrets = self.get_secrets_frm_parameter_store()
                except Exception as error:
                    logging.warning(f"Secrets not found in parameter store.")
                    try:
                        secrets = self.get_secrets_frm_secrets_manager()
                    except Exception as error:
                        logging.warning(f"Secrets not found in secrets manager.")
                        raise ValueError(
                            f"Couldn't find secrets anywhere for {self.secretid}"
                        )
            username, password, host, port = [self.get_secrets_frm_env(k) for k in keys]
        return username, password, host, port  # type: ignore
