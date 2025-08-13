import time

import allure
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.locators.eco_news_page_locators import CREATE_NEWS
from pages.locators.login_page_locators import (EMAIL_INPUT,
                                                PASSWORD_INPUT,
                                                LOGIN_BUTTON,
                                                USERNAME_DISPLAY,
                                                GREEN_CITY_BTN,
                                                ECO_NEWS_BTN)


class LoginModal(BasePage):

    @allure.step("Open 'Login' page")
    def click_captcha(self):
        self.driver.uc_open_with_reconnect(self.driver.current_url, reconnect_time=6)
        print("self.driver.uc_open_with_reconnect")
        self.click_sign_in()
        self.driver.uc_gui_click_captcha()
        return self

    @allure.step("Input email: {email}")
    def enter_email(self, email):
        email_input = self.get_wait().until(EC.visibility_of_element_located(EMAIL_INPUT))
        email_input.clear()
        email_input.send_keys(email)
        return self

    @allure.step("Input password: {password}")
    def enter_password(self, password):
        password_input = self.get_wait().until(EC.visibility_of_element_located(PASSWORD_INPUT))
        password_input.clear()
        password_input.send_keys(password)
        return self

    @allure.step("Click login")
    def click_login(self):
        login_btn = self.get_wait().until(EC.element_to_be_clickable(LOGIN_BUTTON))
        login_btn.click()

    def get_displayed_username(self):
        username = self.get_wait().until(EC.presence_of_element_located(USERNAME_DISPLAY)).text.strip()
        with allure.step(f"Username displayed: {username}"):
            return username

    # Steps after login
    @allure.step("Click 'Green City' button")
    def click_green_city_button(self):
        btn = self.get_wait().until(EC.element_to_be_clickable(GREEN_CITY_BTN))
        btn.click()

    @allure.step("Click 'Eco News' button")
    def click_eco_news_button(self):
        btn = self.get_wait().until(EC.element_to_be_clickable(ECO_NEWS_BTN))
        btn.click()

    @allure.step("Click 'Create News' button")
    def click_create_news_button(self):
        btn = self.get_wait().until(EC.element_to_be_clickable(CREATE_NEWS))
        btn.click()
