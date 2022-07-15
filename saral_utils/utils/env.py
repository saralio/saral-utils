
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

def create_env_api_url(url: str) -> str:
    """depending on the environment variable returns the api url. Attaches the environment variable at the beggining of api url e.g. `https://test-deregister.saral.club`. But for prod it's without env i.e. `https://deregister.saral.club`

    Args:
        url (str): URL string

    Returns:
        str: `https://test-deregister.saral.club` for test/stg environment and `https://deregister.saral.club` for prod environments
    """
    if url.startswith('http'):
        url = url.split('//')[-1]

    env = get_env_var('MY_ENV')
    if env != 'prod':
        if len(url.split('.')) == 3:
            url = f'{env}-{url}'
        else:
            url = f'{env}.{url}'

    return f'https://{url}'

