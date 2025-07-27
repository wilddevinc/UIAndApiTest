from main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait

class Application(object):

    def __init__(self, driver, base_url):
        driver.get(base_url)
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.MainPage = MainPage(driver, base_url)
