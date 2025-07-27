from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

"""
Class Page : basic page class
"""


class Page(object):


    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 10)


    def is_element_visible(self, locator):
        try:
            self.wait.until(visibility_of_element_located(locator))
            return True
        except WebDriverException:
            return False

    def is_elements_visible(self, locators):
        try:
            self.wait.until(visibility_of_all_elements_located(locators))
            return True
        except WebDriverException:
            return False

    def wait_element(self, locator):
        WebDriverWait(self.driver, 120).until(EC.presence_of_element_located(locator))

    def find_element(self, locator, time=60):
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException)
        return WebDriverWait(self.driver, time, poll_frequency=1, ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located(locator),
    message=f"Can't find element by locator {locator}")


