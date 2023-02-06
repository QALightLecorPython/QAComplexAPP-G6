from constants.profile_page import ProfilePageConsts
from pages.base_page import BasePage
from pages.header import Header
from pages.utils import log_wrapper


class ProfilePage(BasePage):
    """Stores methods describes profile page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = ProfilePageConsts
        self.header = Header(self.driver)

    @log_wrapper
    def verify_profile_user_name(self, username):
        """Verify username in the profile"""
        assert self.compare_element_text(xpath=self.const.USERNAME_XPATH, text=username.lower(), strip=True)

    @log_wrapper
    def follow(self):
        """Click on follow button"""
        self.click(xpath=self.const.FOLLOW_BUTTON_XPATH)

    @log_wrapper
    def verify_followings(self, username, count=1):
        """Verify followings count"""
        assert self.compare_element_text(xpath=self.const.FOLLOWING_TAB_XPATH.format(user=username.lower()),
                                         text=self.const.FOLLOWING_TAB_TEXT.format(count=count),
                                         strip=True)
