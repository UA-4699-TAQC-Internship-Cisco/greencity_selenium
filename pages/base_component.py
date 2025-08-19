from selenium.webdriver.chrome.webdriver import WebDriver

from pages.base import Base


class BaseComponent(Base):
    def __init__(self, driver: WebDriver, element=None):
        super().__init__(driver)
        self.element = element
