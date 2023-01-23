"""Tests related to create post page"""
import logging

import pytest

from constants.base import BaseConstants


@pytest.mark.parametrize("browser", [BaseConstants.CHROME, BaseConstants.FIREFOX])
class TestCreatePostPage:
    """Stores tests for create post page base functionality"""

    log = logging.getLogger("[TestCreatePostPage]")

    @pytest.fixture()
    def create_post_page(self, start_page, random_user):
        """
        Steps:
            - Sign Up as a user
            - Navigate to create post page
        """
        # Sign Up as a user
        hello_page = start_page.sign_up(random_user)

        # Navigate to create post page
        create_post_page = hello_page.header.navigate_to_create_post()
        return create_post_page

    def test_create_post(self, create_post_page, random_post):
        """
        - Pre-conditions:
            - Sign Up as a user
            - Navigate to create post page
        - Step:
            - Create post by filling title and body
            - Verify the success message
        """

        # Create post by filling title and body
        post_page = create_post_page.create_post(random_post)

        # Verify the success message
        post_page.verify_post_created()
