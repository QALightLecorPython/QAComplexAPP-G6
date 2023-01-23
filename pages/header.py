from constants.header import HeaderConsts
from pages.base_page import BasePage
from pages.utils import log_wrapper


class Header(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.const = HeaderConsts

    @log_wrapper
    def navigate_to_create_post(self):
        """Navigate to create post page via header button"""
        self.click(xpath=self.const.CREATE_POST_BUTTON_XPATH)

        from pages.create_post_page import CreatePostPage
        return CreatePostPage(self.driver)
