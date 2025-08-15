from selenium.webdriver.common.by import By

from pages.base import BasePage


class EcoNewsListPage(BasePage):
    CREATE_NEWS = (By.XPATH, "//div[@id='create-button' and .//span[text()='Create news']]")

    # tag buttons
    news_tag_button = '//*[@id="main-content"]/div/div[2]/div/app-tag-filter/div/div/button[1]/a'
    events_tag_button = '//*[@id="main-content"]/div/div[2]/div/app-tag-filter/div/div/button[2]/a'
    education_tag_button = '//*[@id="main-content"]/div/div[2]/div/app-tag-filter/div/div/button[3]/a'
    initiatives_tag_button = '//*[@id="main-content"]/div/div[2]/div/app-tag-filter/div/div/button[4]/a'
    ads_tag_button = '//*[@id="main-content"]/div/div[2]/div/app-tag-filter/div/div/button[5]/a'
    # news
    first_news_on_eco_news_page = '//*[@id="main-content"]/div/div[4]/ul/li[1]/a/app-news-list-gallery-view/div/div/div[2]/div[1]/h3'
    first_news_tags_list = '//*[@id="main-content"]/div/div[4]/ul/li[1]/a/app-news-list-gallery-view/div/div/div[1]'
    second_news_tags_list = '//*[@id="main-content"]/div/div[4]/ul/li[2]/a/app-news-list-gallery-view/div/div/div[1]'

    def click_news_filter(self):
        news_filter_button = self.driver.find_element(By.XPATH, self.news_tag_button)
        news_filter_button.click()
        self.driver.implicitly_wait(5)
        self.driver.refresh()

    def click_events_filter(self):
        news_filter_button = self.driver.find_element(By.XPATH, self.events_tag_button)
        news_filter_button.click()
        self.driver.implicitly_wait(5)
        self.driver.refresh()

    def click_education_filter(self):
        news_filter_button = self.driver.find_element(By.XPATH, self.education_tag_button)
        news_filter_button.click()
        self.driver.implicitly_wait(5)
        self.driver.refresh()

    def click_initiatives_filter(self):
        news_filter_button = self.driver.find_element(By.XPATH, self.initiatives_tag_button)
        news_filter_button.click()
        self.driver.implicitly_wait(5)
        self.driver.refresh()

    def click_ads_filter(self):
        news_filter_button = self.driver.find_element(By.XPATH, self.ads_tag_button)
        news_filter_button.click()
        self.driver.implicitly_wait(5)
        self.driver.refresh()

    def get_tags_of_first_and_second_news(self):
        # TODO: add "try" for case when news doesn't exist

        first_element = self.driver.find_element(By.XPATH, self.first_news_tags_list)
        second_element = self.driver.find_element(By.XPATH, self.second_news_tags_list)
        return set(first_element.text.split('|\n') + second_element.text.split('|\n'))

    def is_tag_in_list(self, tag):
        list = self.get_tags_of_first_and_second_news()
        if tag in list:
            return True
        else:
            return False

    def is_tag_filter_active(self, tag):
        tag_to_dict = {"NEWS": self.news_tag_button, "EVENTS": self.events_tag_button,
            "EDUCATION": self.education_tag_button, "INITIATIVES": self.initiatives_tag_button,
            "ADS": self.ads_tag_button}

        expected_activ_color = "rgba(19, 170, 87, 1)"
        element = self.driver.find_element(By.XPATH, tag_to_dict[tag])
        element_color = element.value_of_css_property("background-color")
        return expected_activ_color == element_color
