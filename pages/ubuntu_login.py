import undetected_chromedriver as uc
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators.login_page_locators import (
    EMAIL_INPUT,
    PASSWORD_INPUT,
    LOGIN_BUTTON,
    USERNAME_DISPLAY,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options



class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open_login_page(self, url):
        # Standard way to open a page
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        return self

    def click_sign_in(self):
        button = self.driver.find_element(By.XPATH, '/html/body/app-root/app-main/div/app-header/header/div[2]/div/div/div/ul/img')
        button.click()

    def enter_email(self, email):
        email_input = self.wait.until(EC.visibility_of_element_located(EMAIL_INPUT))
        email_input.clear()
        email_input.send_keys(email)
        self.driver.implicitly_wait(10)
        return self

    def enter_password(self, password):
        password_input = self.wait.until(EC.visibility_of_element_located(PASSWORD_INPUT))
        password_input.clear()
        password_input.send_keys(password)
        self.driver.implicitly_wait(10)
        return self

    def click_login(self):



        login_btn = self.wait.until(EC.element_to_be_clickable(LOGIN_BUTTON))
        login_btn.click()
        return self

    def get_logged_in_username(self):
        username_elem = self.wait.until(EC.visibility_of_element_located(USERNAME_DISPLAY))
        return username_elem.text



# Example usage on Ubuntu
if __name__ == "__main__":

    driver = uc.Chrome(use_subprocess=False,
        headless=True, version_main=136)  # undetected_chromedriver
    driver.maximize_window()
    login_page = LoginPage(driver)
    login_page.open_login_page("https://www.greencity.cx.ua/#/greenCity")
    time.sleep(10)
    login_page.click_sign_in()
    login_page.enter_email("b-t-p@ukr.net")
    login_page.enter_password("My-pass-test1")
    login_page.click_login()
    print("++++++++++++++++++++++++++++++")

    print("Logged in as:", login_page.get_logged_in_username())
    driver.quit()


