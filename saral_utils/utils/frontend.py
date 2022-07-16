# utility functions related to frontend (consumer facing) components
from typing import Union
from env import create_env_api_url

class ShareLinks:
    def __init__(self, email_id: Union[str, None] = None):
        """creates links that can be used in sites navbar or emails footer e.g. links like twitter account, youtube account link etc

        Args:
            email_id (str, None): email id for creating email id dependent link for deregister url

        Returns:
            Dict[str, str]: with links e.g. `{'twitter_account_link', 'twitter_hashtag_link', 'saral_website_link', 'base_sharing_link', 'donation_link', 'personal_account_link', 'unsubscribe_link'}`
        """    

        self.twitter_account_link = "https://twitter.com/data_question"
        self.twitter_hashtag_link = "https://twitter.com/search?q=%23RStats"
        self.saral_website_link = create_env_api_url(url='saral.club')
        self.sharing_link = f'https://twitter.com/intent/tweet?text=' #type:ignore
        self.donation_link = 'https://www.buymeacoffee.com/NgFs2zX'
        self.my_account_link = 'https://twitter.com/mohitsh48631107'
        self.youtube_link = "https://www.youtube.com/channel/UChZfYRQRGADaLtgdYaB0YBg"
        self.feedback_link = "https://forms.gle/nNafF5sHS1ezwHoH9"
        if email_id is not None:
            self.unsubscribe_link = create_env_api_url(url=f'deregister.saral.club/emailId/{email_id}')