"""Tests related to start page"""
import logging

from pages.utils import random_num, random_str


class TestStartPage:
    """Stores tests for start page base functionality"""

    log = logging.getLogger("[TestStartPage]")

    def test_invalid_login(self, start_page):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill login
            - Fill password
            - Click on SignIn button
            - Verify error
        """
        # Login as invalid user
        start_page.sign_in("test123", "pwd123")
        self.log.info("Logged in as invalid user")

        # Verify error
        start_page.verify_sign_in_error()
        self.log.info("Error message was verified")

    def test_empty_login(self, start_page):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Left empty login
            - Left empty password
            - Click on SignIn button
            - Verify error
        """
        # Login as invalid user
        start_page.sign_in("", "")
        self.log.info("Logged in as invalid user")

        # Verify error
        start_page.verify_sign_in_error()
        self.log.info("Error message was verified")

    def test_register(self, start_page):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill email, login and password fields
            - Click on Sign Up button
            - Verify registration is successful
        """
        # Prepare test data
        username_value = f"{random_str()}{random_num()}"
        email_value = f"{username_value}@mail.com"
        password_value = f"{random_str(6)}{random_num()}"

        # Fill email, login and password fields
        hello_page = start_page.sign_up(username=username_value, email=email_value, password=password_value)
        self.log.info("User was registered")

        # Verify register success
        hello_page.verify_sign_up_message(username=username_value)
        self.log.info("Registration for user '%s' was success and verified", username_value)
