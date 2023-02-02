import pytest

from pages.start_page import StartPage
from pages.utils import create_driver
from pages.values import User, Post


@pytest.fixture()
def driver(browser):
    """Creates selenium driver"""
    driver = create_driver(browser=browser)
    yield driver
    driver.close()


@pytest.fixture()
def start_page(driver):
    """Creates start page object"""
    return StartPage(driver)


@pytest.fixture()
def empty_user():
    """Creates an empty user"""
    return User()


@pytest.fixture()
def random_user(empty_user):
    """Creates random user"""
    empty_user.fill_data()
    return empty_user


@pytest.fixture()
def random_post():
    """Creates random post"""
    post = Post()
    post.fill_data()
    return post
