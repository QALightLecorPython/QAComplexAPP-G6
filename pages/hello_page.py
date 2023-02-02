from constants.hello_page import HelloPageConsts
from pages.base_page import BasePage
from pages.header import Header
from pages.utils import log_wrapper


class HelloPage(BasePage):
    """Stores methods describes hello page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = HelloPageConsts
        self.header = Header(self.driver)

    @log_wrapper
    def verify_sign_up_message(self, username):
        """Verify sign up message"""
        assert self.compare_element_text(
            xpath=self.const.HELLO_MESSAGE_XPATH, text=f"Hello {username.lower()}, your feed is empty."
        )
        assert self.compare_element_text(xpath=self.const.USERNAME_IN_HELLO_MESSAGE_XPATH, text=username.lower())
