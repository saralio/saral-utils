# utility functions related to frontend (consumer facing) components
from typing import Union

from .env import create_env_api_url


class ShareLinks:
    def __init__(self, email_id: Union[str, None] = None):
        """creates links that can be used in sites navbar or emails footer e.g. links like twitter account, youtube account link etc

        Args:
            email_id (str, None): email id for creating email id dependent link for deregister url
        """

        self.twitter_account_link = "https://twitter.com/data_question"
        self.twitter_hashtag_link = "https://twitter.com/search?q=%23RStats"
        self.saral_website_link = create_env_api_url(url="saral.club")
        self.sharing_link = "https://twitter.com/intent/tweet?text="  # type:ignore
        self.donation_link = "https://www.buymeacoffee.com/NgFs2zX"
        self.my_account_link = "https://twitter.com/mohitsh48631107"
        self.youtube_link = "https://www.youtube.com/channel/UChZfYRQRGADaLtgdYaB0YBg"
        self.feedback_link = "https://forms.gle/nNafF5sHS1ezwHoH9"
        self.twitter_rstats = "https://twitter.com/data_question"
        self.twitter_python = "https://twitter.com/python_a_day"
        # TODO: [SAR-178] create saral twitter account and update the url here
        # self.twitter_saral = "https://twitter.com/saral"
        self.instagram = "https://www.instagram.com/saral_club/"
        self.linkedin = "https://www.linkedin.com/company/a-question-a-day/"
        self.kofi = "https://ko-fi.com/dsqad"
        self.buy_me_a_coffee = "https://www.buymeacoffee.com/NgFs2zX"
        self.paypal = "https://paypal.me/mohit2013?country.x=IN&locale.x=en_GB"
        if email_id is not None:
            self.unsubscribe_link = create_env_api_url(
                url=f"deregister.saral.club/emailId/{email_id}"
            )
