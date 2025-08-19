import time
import operator
import sys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from seleniumbase.fixtures.page_actions import send_keys

from pages.base import BasePage


class EcoNewsListPage(BasePage):
    CREATE_NEWS = (By.XPATH, "//div[@id='create-button' and .//span[text()='Create news']]")
    SCROLL_PAUSE_TIME = 1

    # tag buttons
    NEWS_TAG_BUTTON = '//*[@id="main-content"]/div/div[2]/div/app-tag-filter/div/div/button[1]/a'
    EVENTS_TAG_BUTTON = '//*[@id="main-content"]/div/div[2]/div/app-tag-filter/div/div/button[2]/a'
    EDUCATION_TAG_BUTTON = '//*[@id="main-content"]/div/div[2]/div/app-tag-filter/div/div/button[3]/a'
    INITIATIVES_TAG_BUTTON = '//*[@id="main-content"]/div/div[2]/div/app-tag-filter/div/div/button[4]/a'
    ADS_TAG_BUTTON = '//*[@id="main-content"]/div/div[2]/div/app-tag-filter/div/div/button[5]/a'
    # news
    FIRST_NEWS_ON_ECO_NEWS = '//*[@id="main-content"]/div/div[4]/ul/li[1]/a/app-news-list-gallery-view/div/div/div[2]/div[1]/h3'
    NEWS_COUNT_STRING = '//*[@id="main-content"]/div/div[3]/app-remaining-count/div/h2'
    NEWS_TILES = "ul[aria-label='news list'] li"

    first_news_tags_list = '//*[@id="main-content"]/div/div[4]/ul/li[1]/a/app-news-list-gallery-view/div/div/div[1]'
    second_news_tags_list = '//*[@id="main-content"]/div/div[4]/ul/li[2]/a/app-news-list-gallery-view/div/div/div[1]'
    TAGS_XPATH={
        'NEWS': '//*[@id="main-content"]/div/div[2]/div/app-tag-filter/div/div/button[1]/a',
        'EVENTS': '//*[@id="main-content"]/div/div[2]/div/app-tag-filter/div/div/button[2]/a',
        'EDUCATION': '//*[@id="main-content"]/div/div[2]/div/app-tag-filter/div/div/button[3]/a',
        'INITIATIVES': '//*[@id="main-content"]/div/div[2]/div/app-tag-filter/div/div/button[4]/a',
        'ADS': '//*[@id="main-content"]/div/div[2]/div/app-tag-filter/div/div/button[5]/a',
    }
    #search
    SEARCH_BUTTON = '//*[@id="main-content"]/div/div[1]/div/div/div[1]/span'
    SEARCH_TEXTBOX = '//*[@id="main-content"]/div/div[1]/div/div/div[1]/input'


    def get_news_count_from_string(self):
        count_string = self.driver.find_element(By.XPATH, self.NEWS_COUNT_STRING).text
        return count_string.split(' ')[0]

    def click_tag_filter(self, tag):
        news_filter_button = self.driver.find_element(By.XPATH, self.TAGS_XPATH[tag])
        news_filter_button.click()
        self.driver.implicitly_wait(5)
        self.driver.refresh()

    def get_tags_of_first_and_second_news(self):
        try:
            first_element = self.driver.find_element(By.XPATH, self.first_news_tags_list)
            second_element = self.driver.find_element(By.XPATH, self.second_news_tags_list)
        except NoSuchElementException:
            print("Less than two comments found for this tag")
            sys.exit()
        else:
            return first_element.text.split('|\n') + second_element.text.split('|\n')

    def is_tag_in_list(self, tag):
        list = self.get_tags_of_first_and_second_news()
        if tag in list:
            return 2 == operator.countOf(list, tag)
        else:
            return False

    def is_tag_filter_active(self, tag):
        tag_to_dict = {"NEWS": self.NEWS_TAG_BUTTON, "EVENTS": self.EVENTS_TAG_BUTTON,
                       "EDUCATION": self.EDUCATION_TAG_BUTTON, "INITIATIVES": self.INITIATIVES_TAG_BUTTON,
                       "ADS": self.ADS_TAG_BUTTON}

        expected_activ_color = "rgba(19, 170, 87, 1)"
        element = self.driver.find_element(By.XPATH, tag_to_dict[tag])
        element_color = element.value_of_css_property("background-color")
        return expected_activ_color == element_color

    def get_news_tiles_count(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(self.SCROLL_PAUSE_TIME)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            self.driver.implicitly_wait(10)

        elements = [el for el in self.driver.find_elements(By.CSS_SELECTOR, self.NEWS_TILES) if el.is_displayed()]
        self.driver.execute_script("window.scrollTo(0, 0);")

        return elements

    def search(self, word):
        self.driver.find_element(By.XPATH, self.SEARCH_BUTTON).click()

        self.get_wait()
        self.driver \
            .find_element(By.XPATH, self.SEARCH_TEXTBOX) \
            .send_keys(word + Keys.ENTER)
        ActionChains(self.driver).perform()
        time.sleep(2)
        self.driver.implicitly_wait(10)
        time.sleep(2)



