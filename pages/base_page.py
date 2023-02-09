import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Describes base methods for the website"""

    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver=driver, timeout=5)

    @allure.step
    def wait_until_displayed(self, by, xpath):
        """Waits until element displayed and return it, else raise an exception"""
        return self.waiter.until(method=expected_conditions.visibility_of_element_located((by, xpath)))

    @allure.step
    def wait_until_displayed_elements(self, by, xpath):
        """Waits until element displayed and return it, else raise an exception"""
        return self.waiter.until(method=expected_conditions.visibility_of_all_elements_located((by, xpath)))

    @allure.step
    def wait_until_clickable(self, by, xpath):
        """Waits until element clickable and return it, else raise an exception"""
        return self.waiter.until(method=expected_conditions.element_to_be_clickable((by, xpath)))

    @allure.step
    def is_element_exists(self, xpath):
        """Check if element exists"""
        try:
            self.driver.find_element(by=By.XPATH, value=xpath)
            return True
        except (TimeoutError, NoSuchElementException):
            return False

    @allure.step
    def is_element_visible(self, xpath):
        """Check if element exists"""
        try:
            self.wait_until_displayed(by=By.XPATH, xpath=xpath)
            return True
        except (TimeoutError, NoSuchElementException):
            return False

    @allure.step
    def fill_field(self, xpath, value):
        """Fill field using provided value"""
        field = self.wait_until_clickable(By.XPATH, xpath)
        field.clear()
        field.send_keys(value)

    @allure.step
    def click(self, xpath):
        """Find and click on the element by provided xpath"""
        self.wait_until_clickable(by=By.XPATH, xpath=xpath).click()

    @allure.step
    def compare_element_text(self, xpath, text, strip=False):
        """Compare element text to provided one"""
        element = self.wait_until_displayed(by=By.XPATH, xpath=xpath)
        if strip:
            return element.text.strip() == text
        else:
            return element.text == text

    def __repr__(self):
        return str(self.__class__.__name__)
