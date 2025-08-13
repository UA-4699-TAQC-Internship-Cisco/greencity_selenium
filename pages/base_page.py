from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from seleniumbase.core.sb_driver import DriverMethods


class BasePage:
    def __init__(self, driver: WebDriver ):
        self.driver = driver

    def get_wait(self, explicit_wait=20):
        return WebDriverWait(self.driver, explicit_wait)
