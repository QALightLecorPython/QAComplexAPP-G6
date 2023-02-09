from itertools import zip_longest

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from constants.chat import ChatConsts
from pages.base_page import BasePage
from pages.utils import log_wrapper


class Chat(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.const = ChatConsts

    @log_wrapper
    @allure.step
    def send_message(self, text):
        """Send message via chat"""
        self.fill_field(xpath=self.const.INPUT_FIELD_XPATH, value=text + Keys.ENTER)

    @log_wrapper
    @allure.step
    def verify_messages(self, expected_messages):
        """Verify all sent messages"""
        messages = self.wait_until_displayed_elements(by=By.XPATH, xpath=self.const.SELF_MESSAGES_XPATH)
        for message, expected_message in zip_longest(messages, expected_messages):
            assert message.text.strip() == expected_message, f"Actual: {message}, Expected: {expected_message}"
