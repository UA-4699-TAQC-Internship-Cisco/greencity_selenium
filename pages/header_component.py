import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base import BaseComponent
from pages.eco_news_list_page import EcoNewsListPage
from pages.login import LoginModal


class Header(BaseComponent):
    sign_in_btn = (By.XPATH, "//a[contains(text(),'Sign in')]")
    USERNAME_DISPLAY = (By.XPATH, "//li[@class='body-2 user-name']")
    ECO_NEWS_BTN = (By.XPATH, "//a[contains(@class,'url-name') and normalize-space()='Eco news']")

    def __init__(self, driver, node):
        super().__init__(driver)
        self.node = node

    def click_sign_in(self) -> LoginModal:
        print("click_sign_in")
        self.get_wait().until(EC.visibility_of_element_located(self.sign_in_btn))
        we = self.driver.find_element(*self.sign_in_btn)
        we.click()
        return LoginModal(self.driver, we)

    def get_displayed_username(self):
        username = self.get_wait().until(EC.presence_of_element_located(self.USERNAME_DISPLAY)).text.strip()
        with allure.step(f"Username displayed: {username}"):
            return username

    @allure.step("Click 'Eco News' button")
    def click_eco_news_button(self) -> EcoNewsListPage:
        btn = self.get_wait().until(EC.presence_of_element_located(self.ECO_NEWS_BTN))
        btn.click()
        return EcoNewsListPage(self.driver)
