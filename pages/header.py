from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

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

    @log_wrapper
    def sign_out(self):
        """Navigate to start page via Sign Out"""
        self.click(xpath=self.const.SIGN_OUT_BUTTON_XPATH)

        from pages.start_page import StartPage
        return StartPage(self.driver)

    @log_wrapper
    def navigate_to_profile_page(self, username):
        """Navigate to profile page via username"""
        self.click(xpath=self.const.MY_PROFILE_BUTTON_XPATH.format(username=username.lower()))

        from pages.profile_page import ProfilePage
        return ProfilePage(self.driver)

    @log_wrapper
    def open_chat(self):
        """Open chat via button"""
        self.click(xpath=self.const.CHAT_BUTTON_XPATH)

    @log_wrapper
    def navigate_to_post_by_title(self, title):
        """Search for the post and click on it"""
        self.click(xpath=self.const.SEARCH_BUTTON_XPATH)
        self.fill_field(xpath=self.const.SEARCH_INPUT_XPATH, value=title + Keys.ENTER)
        results = self.wait_until_displayed_elements(by=By.XPATH, xpath=self.const.SEARCH_RESULTS_XPATH)
        for result in results:
            if result.text == title:
                result.click()

        from pages.post_page import PostPage
        return PostPage(self.driver)
