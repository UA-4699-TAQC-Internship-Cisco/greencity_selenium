import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class PreviewNewsPage(BasePage):

    PAGE_TITLE = '//app-news-preview-page/div/div[2]'
    AUTHOR = '//app-news-preview-page/div/div[4]/div[2]/div[3]'
    PRE_TITLE = '//app-news-preview-page/div/div[4]/div[1]/div'
    PRE_TAGS = '//app-news-preview-page/div/div[3]'
    PRE_LINK = '//app-news-preview-page/div/div[4]/div[3]/div[2]/div[2]/div[2]'
    PRE_TEXT = '//app-news-preview-page/div/div[4]/div[3]/div[2]/div[1]'


    @allure.step("get author")
    def get_author(self):
        return self.driver.find_element(By.XPATH, self.AUTHOR).text

    @allure.step("'create news' title is present")
    def is_create_news_title_present(self):
        if 'Create news' == self.driver.find_element(By.XPATH, self.PAGE_TITLE).text:
            return True
        else:
            return False

    @allure.step("get title")
    def get_title(self):
        return self.driver.find_element(By.XPATH, self.PRE_TITLE).text

    @allure.step("get link")
    def get_link(self):
        return self.driver.find_element(By.XPATH, self.PRE_LINK).text


    @allure.step("get body")
    def get_body_text(self):
        return self.driver.find_element(By.XPATH, self.PRE_TEXT).text

    @allure.step("get tags")
    def get_tags(self):
        return  self.driver.find_element(By.XPATH, self.PRE_TAGS).text
