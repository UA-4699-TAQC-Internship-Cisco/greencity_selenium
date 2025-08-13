import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.locators.login_page_locators import (
    EMAIL_INPUT,
    PASSWORD_INPUT,
    LOGIN_BUTTON,
    USERNAME_DISPLAY,
)


class LoginPage(BasePage):


    def open_login_page(self, url):
        # Standard way to open a page
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        return self

    def click_sign_in(self):
        button = self.driver.find_element(By.XPATH, '/html/body/app-root/app-main/div/app-header/header/div[2]/div/div/div/ul/img')
        button.click()

    def enter_email(self, email):
        email_input = self.get_wait().until(EC.visibility_of_element_located(EMAIL_INPUT))
        email_input.clear()
        email_input.send_keys(email)
        self.driver.implicitly_wait(10)
        return self

    def enter_password(self, password):
        password_input = self.get_wait().until(EC.visibility_of_element_located(PASSWORD_INPUT))
        password_input.clear()
        password_input.send_keys(password)
        self.driver.implicitly_wait(10)
        return self

    def click_login(self):
        login_btn = self.get_wait().until(EC.element_to_be_clickable(LOGIN_BUTTON))
        login_btn.click()
        return self

    def get_logged_in_username(self):
        username_elem = self.get_wait().until(EC.visibility_of_element_located(USERNAME_DISPLAY))
        return username_elem.text



