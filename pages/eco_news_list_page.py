import time

import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from config.resources import ECO_NEWS_TITLE_TEXT
from pages.base_page import BasePage


class EcoNewsListPage(BasePage):
    SCROLL_PAUSE_TIME = 1

    CREATE_NEWS = (By.XPATH, "//div[@id='create-button' and .//span[text()='Create news']]")
    ECO_NEWS_TITLE = (By.XPATH, "//h1[@class='main-header']")
    BOOKMARK_BUTTON = '//*[@id="main-content"]/div/div[1]/div/div/div[2]/span'
    EVENT_ICON_BUTTON = '//*[@id="main-content"]/div/div[1]/div/div/div[3]/img'
    EXPECTED_ACTIV_COLOR = "rgba(19, 170, 87, 1)"

    # tag buttons
    NEWS_TAG_BUTTON = '//*[@id="main-content"]/div/div[2]/div/app-tag-filter/div/div/button[1]/a'
    EVENTS_TAG_BUTTON = '//*[@id="main-content"]/div/div[2]/div/app-tag-filter/div/div/button[2]/a'
    EDUCATION_TAG_BUTTON = '//*[@id="main-content"]/div/div[2]/div/app-tag-filter/div/div/button[3]/a'
    INITIATIVES_TAG_BUTTON = '//*[@id="main-content"]/div/div[2]/div/app-tag-filter/div/div/button[4]/a'
    ADS_TAG_BUTTON = '//*[@id="main-content"]/div/div[2]/div/app-tag-filter/div/div/button[5]/a'
    # news
    FIRST_NEWS_ON_ECO_NEWS = '//*[@id="main-content"]/div/div[4]/ul/li[1]/a/app-news-list-gallery-view/div/div/div[2]/div[1]/h3'
    NEWS_COUNT_STRING = '//*[@id="main-content"]/div/div[3]/app-remaining-count/div/h2'
    NEWS_TITLES = "ul[aria-label='news list'] li h3"
    NEWS_OWNER = "ul[aria-label='news list'] li p span"
    NEWS_TILES = "ul[aria-label='news list'] li"
    NEWS_TAGS = '//app-news-list-gallery-view/div/div/div[1]'

    first_news_tags_list = '//*[@id="main-content"]/div/div[4]/ul/li[1]/a/app-news-list-gallery-view/div/div/div[1]'
    second_news_tags_list = '//*[@id="main-content"]/div/div[4]/ul/li[2]/a/app-news-list-gallery-view/div/div/div[1]'
    TAGS_XPATH = {'NEWS': '//app-tag-filter/div/div/button[1]/a',
                  'EVENTS': '//app-tag-filter/div/div/button[2]/a',
                  'EDUCATION': '//app-tag-filter/div/div/button[3]/a',
                  'INITIATIVES': '//app-tag-filter/div/div/button[4]/a',
                  'ADS': '//app-tag-filter/div/div/button[5]/a', }

    # search
    SEARCH_BUTTON = '//*[@id="main-content"]/div/div[1]/div/div/div[1]/span'
    SEARCH_TEXTBOX = '//*[@id="main-content"]/div/div[1]/div/div/div[1]/input'

    @allure.step("Click 'Create news' button")
    def click_create_news_button(self):
        publish_btn = self.get_wait().until(EC.element_to_be_clickable(self.CREATE_NEWS))
        publish_btn.click()

    @allure.step("Check 'Eco news' page title")
    def check_eco_news_title(self):
        title_element = self.get_wait().until(EC.presence_of_element_located(self.ECO_NEWS_TITLE))
        actual_text = title_element.text
        assert actual_text == ECO_NEWS_TITLE_TEXT

    def get_news_count_from_string(self) -> int:
        count_string = self.driver.find_element(By.XPATH, self.NEWS_COUNT_STRING).text
        return int(count_string.split(' ')[0])

    def click_tag_filter(self, tag):
        news_filter_button = self.driver.find_element(By.XPATH, self.TAGS_XPATH[tag])
        news_filter_button.click()
        self.driver.implicitly_wait(5)
        self.driver.refresh()

    def get_all_tags_after_press_tag(self):
        try:
            last_height = self.driver.execute_script("return document.body.scrollHeight")

            while True:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(self.SCROLL_PAUSE_TIME)
                new_height = self.driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
                self.driver.implicitly_wait(10)
            all_tags_on_page = [el.text for el in self.driver.find_elements(By.XPATH, self.NEWS_TAGS) if el.is_displayed()]
            self.driver.execute_script("window.scrollTo(0, 0);")

            return all_tags_on_page
        except NoSuchElementException:
            return []


    def is_tag_filter_active(self, tag):
        tag_to_dict = {"NEWS": self.NEWS_TAG_BUTTON, "EVENTS": self.EVENTS_TAG_BUTTON,
                       "EDUCATION": self.EDUCATION_TAG_BUTTON, "INITIATIVES": self.INITIATIVES_TAG_BUTTON,
                       "ADS": self.ADS_TAG_BUTTON}

        element = self.driver.find_element(By.XPATH, tag_to_dict[tag])
        element_color = element.value_of_css_property("background-color")
        return self.EXPECTED_ACTIV_COLOR == element_color

    def get_news_items_titles(self):
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

    @allure.step('Click bookmark')
    def click_bookmark_button(self):
        bookmark_button = self.driver.find_element(By.XPATH, self.BOOKMARK_BUTTON)
        bookmark_button.click()
        self.driver.execute_script('return document.body.innerHTML')

    def news_with_bookmark(self):
        bookmark = self.driver.find_elements(By.CSS_SELECTOR, ".flag-active")
        return bookmark

    def search_enter_text(self, word):
        self.driver.find_element(By.XPATH, self.SEARCH_BUTTON).click()

        for _character in word:
            self.driver.find_element(By.XPATH, self.SEARCH_TEXTBOX).send_keys(_character)
            time.sleep(0.2)

    def news_written_by_user(self, user):
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(self.SCROLL_PAUSE_TIME)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            self.driver.implicitly_wait(10)

        news_written_by_user = [el for el in self.driver.find_elements(By.CSS_SELECTOR, self.NEWS_TILES) if el.is_displayed() and user in el.text]

        self.driver.execute_script("window.scrollTo(0, 0);")

        return news_written_by_user

    def click_event_icon(self):
        bookmark_button = self.driver.find_element(By.XPATH, self.EVENT_ICON_BUTTON)
        bookmark_button.click()
        self.driver.execute_script('return document.body.innerHTML')
