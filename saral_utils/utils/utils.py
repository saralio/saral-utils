import logging
import os
from typing import Any

from saral_utils.types.env import Env, Region


def configure_logger() -> None:
    # reference: https://stackoverflow.com/a/56579088/8547986
    # by default aws sets up handlers to root logger
    if logging.getLogger().hasHandlers():
        # The Lambda environment pre-configures a handler logging to stderr. If a handler is already configured,
        # `.basicConfig` does not execute. Thus we set the level directly.
        logging.getLogger().setLevel(logging.INFO)
    else:
        logging.basicConfig(level=logging.INFO)


def get_env_var(name: str, default: Any = None, raise_error: bool = True) -> str:
    """environment variable from environment

    Args:
        name: of the environment variable to fetch
        default: default value of environment variable
        raise_error: if True, raise error if environment variable is not found

    Returns:
        environment variable value
    """
    if raise_error:
        return os.environ[name]
    else:
        return os.getenv(name, default)


def get_my_region() -> Region:
    return get_env_var("MY_REGION")  # type: ignore


def get_my_env() -> Env:
    return get_env_var("MY_ENV")  # type: ignore
