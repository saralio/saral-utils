
from dataclasses import dataclass
import os

def get_env_var(env: str) -> str:
    """fetches the value of environment variable from environment

    Args:
        env (str): environment variable to check

    Raises:
        ValueError: Value error if environment variable is not present

    Returns:
        str: environment variable value
    """    
    env_var = os.getenv(env)
    if env_var is None:
        raise ValueError(f'Provided environment variable is not present in environment')

    return env_var


@dataclass
class EnvVars:
    """Class to check for required environment variables in environment. Checks for following environment variables:
        1. MY_ENV
        2. MY_REGION 
    """ 

    MY_ENV: str = get_env_var('MY_ENV')
    MY_REGION: str = get_env_var('MY_REGION') 