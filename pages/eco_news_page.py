import allure

from pages.base_page import BasePage
from pages.locators.eco_news_page_locators import *
from pages.locators.navbar_locators import *

class EcoNews(BasePage):

    @allure.step("Open eco news page")
    def go_to_eco_news_page(self):
        self.driver.implicitly_wait(10)
        eco_news=self.driver.find_element(By.XPATH, navbar_eco_news)
        eco_news.click()

    def click_news_filter(self):
        news_filter_button = self.driver.find_element(By.XPATH, news_tag_button)
        news_filter_button.click()
        self.driver.implicitly_wait(5)
        self.driver.refresh()


    def click_events_filter(self):
        news_filter_button = self.driver.find_element(By.XPATH, events_tag_button)
        news_filter_button.click()
        self.driver.implicitly_wait(5)
        self.driver.refresh()


    def click_education_filter(self):
        news_filter_button = self.driver.find_element(By.XPATH, education_tag_button)
        news_filter_button.click()
        self.driver.implicitly_wait(5)
        self.driver.refresh()


    def click_initiatives_filter(self):
        news_filter_button = self.driver.find_element(By.XPATH, initiatives_tag_button)
        news_filter_button.click()
        self.driver.implicitly_wait(5)
        self.driver.refresh()


    def click_ads_filter(self):
        news_filter_button = self.driver.find_element(By.XPATH, ads_tag_button)
        news_filter_button.click()
        self.driver.implicitly_wait(5)
        self.driver.refresh()

    def get_tags_of_first_and_second_news(self):
        #TODO: add "try" for case when news doesn't exist

        first_element = self.driver.find_element(By.XPATH, first_news_tags_list)
        second_element = self.driver.find_element(By.XPATH, second_news_tags_list)
        return set(first_element.text.split('|\n') + second_element.text.split('|\n'))

    def is_tag_in_list(self, tag):
        list = self.get_tags_of_first_and_second_news()
        if tag in list:
            return True
        else:
            return False

    def is_tag_filter_active(self, tag):
        tag_to_dict = {
            "NEWS": news_tag_button,
            "EVENTS": events_tag_button,
            "EDUCATION": education_tag_button,
            "INITIATIVES": initiatives_tag_button,
            "ADS": ads_tag_button
        }

        expected_activ_color = "rgba(19, 170, 87, 1)"
        element = self.driver.find_element(By.XPATH, tag_to_dict[tag])
        element_color = element.value_of_css_property("background-color")
        return expected_activ_color == element_color
