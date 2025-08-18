from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# __all__ = ["BasePage", "BaseComponent"]


class Base:
    header_locator = (By.XPATH, "//a[contains(text(),'Sign in')]")
   #header_locator = (By.XPATH, "//header[@aria-label='Welcome to header']")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # def get_header(self) -> 'Header':
    #     from pages.header_component import Header
    #     we = self.driver.find_element(*self.header_locator)
    #     return Header(self.driver, we)

    def get_wait(self, explicit_wait=120):
        return WebDriverWait(self.driver, explicit_wait)
