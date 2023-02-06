"""Tests related to profile page"""
import allure
import pytest
from allure_commons.types import Severity

from constants.base import BaseConstants
from pages.utils import random_str, random_text
from pages.values import User, Post


@pytest.mark.parametrize("browser", [BaseConstants.CHROME])
class TestProfilePage:
    """Stores tests for profile page base functionality"""

    @pytest.fixture()
    def user_with_post(self, start_page):
        """
        - Sign Up as a user
        - Navigate to create post page
        - Create post (preserve title somewhere)
        - Logout
        """
        # User
        user = User()
        user.fill_data()
        # Post
        post = Post(title=random_str(10), body=random_text(20))
        # Sign Up as a user
        hello_page = start_page.sign_up(user)
        # Navigate to create post page
        create_post_page = hello_page.header.navigate_to_create_post()
        # Create post (preserve title somewhere)
        post_page = create_post_page.create_post(post)
        user.posts.append(post)
        # Logout
        post_page.header.sign_out()

        return user

    @allure.epic("Profile Page")
    @allure.feature("Username")
    @allure.story("Test username on profile page")
    @allure.severity(Severity.CRITICAL)
    def test_profile_username(self, hello_page, random_user):
        """
         - Pre-conditions:
             - Sign Up as a user
         - Steps:
             - Click on "My Profile"
             - Verify profile username
        """
        # Click on "My Profile"
        profile_page = hello_page.header.navigate_to_profile_page(random_user.username)

        # Verify profile username
        profile_page.verify_profile_user_name(random_user.username)

    @allure.epic("Profile Page")
    @allure.feature("Following")
    @allure.story("Test followings tab")
    @allure.severity(Severity.NORMAL)
    def test_followings(self, user_with_post, hello_page, random_user):
        """
        - Pre-conditions:
            - Sign Up as a user
            - Navigate to create post page
            - Create post (preserve title somewhere)
            - Logout
            - Sign Up as a NEW user
        - Step:
            - Search for the post & Navigate to post page
            - Navigate to author profile
            - Click follow
            - Navigate to my profile
            - Verify Followings tab
        """
        post = user_with_post.posts[0]
        # Search for the post
        post_page = hello_page.header.navigate_to_post_by_title(post.title)

        # Navigate to author profile
        author_profile_page = post_page.navigate_to_author_profile(username=user_with_post.username)

        # Click follow
        author_profile_page.follow()

        # Navigate to my profile
        my_profile_page = author_profile_page.header.navigate_to_profile_page(username=random_user.username)

        # Verify Followings tab
        my_profile_page.verify_followings(username=random_user.username)
