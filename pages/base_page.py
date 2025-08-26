import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base import Base


class BasePage(Base):
    header_locator = (By.XPATH, "//header[@aria-label='Welcome to header']")

    @allure.step("Open news by link")
    def open_page_by_link(self, link):
        self.driver.get(link)

    def get_header(self):
        from pages.header_component import Header
        # return Header(self.driver, self.driver.find_element(*self.header_locator))
        return Header(self.driver,
                      WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.header_locator)))
