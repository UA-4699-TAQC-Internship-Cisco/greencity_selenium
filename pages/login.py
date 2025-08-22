import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_component import BaseComponent
from pages.my_space_page import MySpace


class LoginModal(BaseComponent):
    EMAIL_INPUT = (By.XPATH, "//input[@id='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='password']")
    SIGN_IN_BUTTON = (By.XPATH, "//button[contains(text(),'Sign in')]")

    @allure.step("Open 'Login' page")
    def click_captcha(self):
        # self.driver.uc_open_with_reconnect(self.driver.current_url, reconnect_time=6)
        # self.driver.uc_gui_click_captcha()
        return self

    @allure.step("Input email: {email}")
    def enter_email(self, email):
        email_input = self.get_wait().until(EC.visibility_of_element_located(self.EMAIL_INPUT))
        email_input.clear()
        email_input.send_keys(email)
        return self

    @allure.step("Input password: {password}")
    def enter_password(self, password):
        password_input = self.get_wait().until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        password_input.clear()
        password_input.send_keys(password)
        return self

    @allure.step("Click login")
    def click_sign_in_btn(self) -> MySpace:
        login_btn = self.get_wait().until(EC.element_to_be_clickable(self.SIGN_IN_BUTTON))
        login_btn.click()
        return MySpace(self.driver)
