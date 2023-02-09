import datetime
import logging
import random
import string
from time import sleep

from selenium import webdriver

from constants.base import BaseConstants
from pages.text_presets import EN_TEXT


def random_num():
    """Generate random number"""
    return str(random.randint(111111, 999999))


def random_str(length=5):
    """Generate random string"""
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def random_text(length=15, preset=EN_TEXT):
    """Create text using provided preset"""
    words = preset.split(" ")
    return " ".join((random.choice(words).replace("\n", "") for _ in range(length)))


def wait_until_ok(timeout=5, period=0.25):
    """Retires function until ok (or 5 seconds)"""
    log = logging.getLogger("[WaitUntilOk]")

    def decorator(original_function):
        def wrapper(*args, **kwargs):
            end_time = datetime.datetime.now() + datetime.timedelta(
                seconds=timeout
            )
            while True:
                try:
                    return original_function(*args, **kwargs)
                except Exception as err:
                    log.warning(f"Catching: {err}")
                    if datetime.datetime.now() > end_time:
                        raise err
                    sleep(period)

        return wrapper

    return decorator


def log_wrapper(func):
    """Add logs for method based on the docstring"""

    def wrapper(*args, **kwargs):
        log = logging.getLogger("[LogDecorator]")
        result = func(*args, **kwargs)
        # log.info(f"{func.__doc__}; Args: {args}; Kwargs: {kwargs}")
        log.info(func.__doc__)
        return result

    return wrapper


def create_driver(browser):
    """Create driver according to provided browser"""
    if browser == BaseConstants.CHROME:
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("headless")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(options=options)
    elif browser == BaseConstants.FIREFOX:
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unknown browser name: {browser}")
    driver.implicitly_wait(1)
    driver.get(BaseConstants.URL)
    return driver
