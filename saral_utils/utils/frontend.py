# utility functions related to frontend (consumer facing) components
from typing import Union, Dict
from env import create_env_api_url

def generate_share_links(email_id: Union[str, None] = None) -> Dict[str, str]:
    """creates links that can be used in sites navbar or emails footer e.g. links like twitter account, youtube account link etc

    Args:
        email_id (str, None): email id for creating email id dependent link for deregister url

    Returns:
        Dict[str, str]: with links e.g. `{'twitter_account_link', 'twitter_hashtag_link', 'saral_website_link', 'base_sharing_link', 'donation_link', 'personal_account_link', 'unsubscribe_link'}`
    """    
    twitter_account_link = "https://twitter.com/data_question"
    twitter_hashtag_link = "https://twitter.com/search?q=%23RStats"
    saral_website_link = create_env_api_url(url='saral.club')
    sharing_link = f'https://twitter.com/intent/tweet?text=' #type:ignore
    donation_link = 'https://www.buymeacoffee.com/NgFs2zX'
    my_account_link = 'https://twitter.com/mohitsh48631107'
    resp = {
        'twitter_account_link': twitter_account_link,
        'twitter_rstats_hashtag_link': twitter_hashtag_link,
        'saral_website_link': saral_website_link,
        'base_sharing_link': sharing_link,
        'donation_link': donation_link,
        'personal_account_link': my_account_link
    }
    
    if email_id is not None:
        unsubscribe_link = create_env_api_url(url=f'deregister.saral.club/emailId/{email_id}')
        resp['unsubscribe_link'] = unsubscribe_link
    return resp