import allure

from config.resources import NEWS_LINK
from pages.base_page import BasePage
from pages.locators.eco_news_page_locators import *
from pages.locators.news_page_locators import *


class NewsPage(BasePage):

    @allure.step("Open page by link")
    def open_page_by_link(self, link):
        self.driver.get(f'{link}')
        self.driver.implicitly_wait(10)

    @allure.step("Message sent successfully")
    def send_message(self, message):
        self.driver.implicitly_wait(10)
        comment_textarea_fild=self.driver.find_element(By.XPATH, comment_textarea)
        comment_textarea_fild.clear()
        comment_textarea_fild.send_keys(message)
        button=self.driver.find_element(By.XPATH, comment_button)
        button.click()

    def right_like(self):
        pass

    def like_post(self):
        pass

    @allure.step("Open a first news item in the news list")
    def go_to_first_news(self):
        eco_news=self.driver.find_element(By.XPATH, navbar_eco_news)
        eco_news.click()
        self.driver.implicitly_wait(10)
        first_news=self.driver.find_element(By.XPATH, first_news_on_eco_news_page)
        first_news.click()
        self.driver.implicitly_wait(10)

    @allure.step("Get first comment data")
    def get_first_comment_data(self):
        data = {
            'author': self.driver.find_element(By.XPATH, first_comment_author).text,
            'text': self.driver.find_element(By.XPATH, first_comment_text).text
        }
        return data

    @allure.step("Get news title")
    def get_news_title(self):
        return self.driver.find_element(By.XPATH, news_title).text

    @allure.step("Open created news by link")
    def open_page_by_link(self, link):
        self.driver.get(link)
