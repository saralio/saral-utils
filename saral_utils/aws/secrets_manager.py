import json
from typing import Any, Optional

from mypy_boto3_secretsmanager.client import SecretsManagerClient

from saral_utils.utils.utils import get_my_env, get_my_region

from ._base import AWSBase


class SecretsManager(AWSBase):

    def __init__(
        self,
        secret_id: str,
        my_env: Optional[str] = None,
        my_region: Optional[str] = None,
        branch: Optional[str] = None,
    ) -> None:
        self.secret_id = secret_id
        self.my_env = my_env or get_my_env()
        self.my_region = my_region or get_my_region()
        self.branch = branch
        super().__init__(
            service="secretsmanager", env=self.my_env, region=self.my_region  # type: ignore
        )
        self.client: SecretsManagerClient = self._create_client()

    @property
    def secrets(self) -> dict[str, Any]:
        sec = self.client.get_secret_value(SecretId=self.secret_id)
        if "SecretString" in sec:
            return json.loads(sec["SecretString"])
        else:
            raise ValueError(
                f"Secret {self.secret_id} not found, response returned: {sec}"
            )
