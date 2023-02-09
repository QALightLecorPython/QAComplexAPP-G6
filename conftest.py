import os

import pytest

from constants.base import BaseConstants
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


@pytest.fixture()
def hello_page(start_page, random_user):
    return start_page.sign_up(random_user)


def pytest_sessionstart(session):
    os.environ["PATH"] = os.environ["PATH"] + f":{os.path.abspath(BaseConstants.DRIVER_PATH)}"

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """Preserve screenshot on failure"""
#     outcome = yield
#     result = outcome.get_result()
#
#     if result.failed:
#         driver = [item.funcargs[arg] for arg in item.funcargs if arg.endswith("_page")][0].driver  # hello_page.driver
#         file_name = f"{item.name}_{datetime.datetime.now().strftime('%H-%M-%S')}.png"
#         file_path = (
#             "/Users/almin/PycharmProjects/QAComplexAPP-G6/screenshots"
#         )
#         driver.save_screenshot(os.path.join(file_path, file_name))
