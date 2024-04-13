from typing import Optional

import boto3
from mypy_boto3_secretsmanager.literals import ServiceName

from ..types.env import Env, Region
from ..utils.utils import get_my_env, get_my_region


class AWSBase:
    def __init__(
        self,
        service: ServiceName,
        env: Optional[Env] = None,
        region: Optional[Region] = None,
    ):
        self.service = service
        self.env = env or get_my_env()
        self.region = region or get_my_region()
        self._validate_env_region()

    def _validate_env_region(self):
        if self.env not in ["test", "stg", "prod"]:
            raise ValueError("env must be test, stg or prod")
        if self.region not in ["ap-south-1", "us-west-2"]:
            raise ValueError("region must be ap-south-1 or us-west-2")

        env_region_map = {"test": "ap-south-1", "prod": "us-west-2"}

        if env_region_map[self.env] != self.region:
            raise ValueError(
                f"Incorrect env and region mapping, correct mapping: {env_region_map}"
            )

    def _create_client(self):
        return boto3.client(service_name=self.service, region_name=self.region)  # type: ignore
