"""Tests related to start page"""
import logging

import pytest

from constants.base import BaseConstants


@pytest.mark.parametrize("browser", [BaseConstants.CHROME, BaseConstants.FIREFOX])
class TestStartPage:
    """Stores tests for start page base functionality"""

    log = logging.getLogger("[TestStartPage]")

    def test_invalid_login(self, start_page, random_user):
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
        start_page.sign_in(random_user)

        # Verify error
        start_page.verify_sign_in_error()

    def test_empty_login(self, start_page, empty_user):
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
        start_page.sign_in(empty_user)

        # Verify error
        start_page.verify_sign_in_error()

    def test_register(self, start_page, random_user):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill email, login and password fields
            - Click on Sign Up button
            - Verify registration is successful
        """
        # Fill email, login and password fields
        hello_page = start_page.sign_up(random_user)

        # Verify register success
        hello_page.verify_sign_up_message(username=random_user.username)
