import allure
import pytest
from allure_commons.types import Severity

from constants.base import BaseConstants


@pytest.mark.parametrize("browser", [BaseConstants.CHROME])
class TestHeader:
    """Stores tests for header base functionality"""

    @allure.epic("Auth")
    @allure.feature("Sign Out")
    @allure.story("Test sign out from hello page")
    @allure.severity(Severity.CRITICAL)
    def test_sign_out(self, hello_page):
        """
        - Pre-conditions:
            - Open start page
            - Sign Up as the user
        - Steps:
            - Click on Sign Out Button
            - Verify the result
        """
        # Click on Sign Out Button
        start_page = hello_page.header.sign_out()

        # Verify the result
        start_page.verify_sign_in_exists()
