import json
from typing import Any, Optional

from mypy_boto3_ssm.client import SSMClient

from saral_utils.aws._base import AWSBase
from saral_utils.utils.utils import get_my_env, get_my_region


class ParameterStore(AWSBase):
    def __init__(
        self,
        parameter_name: str,
        my_env: Optional[str] = None,
        my_region: Optional[str] = None,
        decrypt: bool = True,
        branch: Optional[str] = None,
    ) -> None:
        self.parameter_name = parameter_name
        self.my_env = my_env or get_my_env()
        self.my_region = my_region or get_my_region()
        self.branch = branch
        self.decrypt = decrypt
        super().__init__(service="ssm", env=self.my_env, region=self.my_region)  # type: ignore
        self.client: SSMClient = self._create_client()

    @property
    def parameters(self) -> dict[str, Any]:
        ps = self.client.get_parameter(
            Name=self.parameter_name, WithDecryption=self.decrypt
        )
        if "Parameter" in ps and "Value" in ps["Parameter"]:
            return json.loads(ps["Parameter"]["Value"])
        else:
            raise ValueError(
                f"Parameter {self.parameter_name} not found, response returned: {ps}"
            )
