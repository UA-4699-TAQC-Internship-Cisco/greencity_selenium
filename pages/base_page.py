from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    sign_in_btn = (By.XPATH, "//a[contains(text(),'Sign in')]")
    def __init__(self, driver: WebDriver ):
        self.driver = driver

    def get_wait(self, explicit_wait=20):
        return WebDriverWait(self.driver, explicit_wait)

    def click_sign_in(self):
        print("click_sign_in")
        self.get_wait().until(EC.visibility_of_element_located(self.sign_in_btn))
        self.driver.find_element(*self.sign_in_btn).click()
