import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

__all__ = ["BasePage", "BaseComponent"]

, from pages.header_component import Header


class Base:
    header_locator = (By.XPATH, "//a[contains(text(),'Sign in')]")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_header(self)->Header:
        we = self.driver.find_element(*self.header_locator)
        return Header(self.driver, we)

    def get_wait(self, explicit_wait=30):
        return WebDriverWait(self.driver, explicit_wait)


class BasePage(Base):

    @allure.step("Open news by link")
    def open_page_by_link(self, link):
        self.driver.get(link)


class BaseComponent(Base):
    pass
