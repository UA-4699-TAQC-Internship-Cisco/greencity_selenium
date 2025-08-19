import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from config.resources import ECO_NEWS_TITLE_TEXT
from pages.base_page import BasePage


class EcoNewsListPage(BasePage):
    CREATE_NEWS = (By.XPATH, "//div[@id='create-button' and .//span[text()='Create news']]")
    first_news_on_eco_news_page = '//*[@id="main-content"]/div/div[4]/ul/li[1]/a/app-news-list-gallery-view/div/div/div[2]/div[1]/h3'
    ECO_NEWS_TITLE = (By.XPATH, "//h1[@class='main-header']")

    @allure.step("Click 'Create news' button")
    def click_create_news_button(self):
        publish_btn = self.get_wait().until(EC.element_to_be_clickable(self.CREATE_NEWS))
        publish_btn.click()

    @allure.step("Check 'Eco news' page title")
    def check_eco_news_title(self):
        title_element = self.get_wait().until(EC.presence_of_element_located(self.ECO_NEWS_TITLE))
        actual_text = title_element.text
        assert actual_text == ECO_NEWS_TITLE_TEXT
