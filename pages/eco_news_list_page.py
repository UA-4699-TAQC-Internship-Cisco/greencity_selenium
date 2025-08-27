import time
from typing import List

import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

from config.resources import ECO_NEWS_TITLE_TEXT
from pages.base_page import BasePage
from pages.create_news_page import CreateNewsPage
from pages.news_page import NewsPage


class EcoNewsListPage(BasePage):
    """Page object for the Eco News List page with standardized locators and improved methods."""

    # Constants
    SCROLL_PAUSE_TIME = 1
    EXPECTED_ACTIVE_COLOR = "rgba(19, 170, 87, 1)"
    CHARACTER_INPUT_DELAY = 0.2

    # Main page elements - using consistent tuple format (By.STRATEGY, "locator")
    CREATE_NEWS = (By.XPATH, "//div[@id='create-button' and .//span[text()='Create news']]")
    ECO_NEWS_TITLE = (By.XPATH, "//h1[@class='main-header']")
    BOOKMARK_BUTTON = (By.XPATH, "//*[@id='main-content']/div/div[1]/div/div/div[2]/span")
    EVENT_ICON_BUTTON = (By.XPATH, "//*[@id='main-content']/div/div[1]/div/div/div[3]/img")

    # Tag filter buttons
    NEWS_TAG_BUTTON = (By.XPATH, "//*[@id='main-content']/div/div[2]/div/app-tag-filter/div/div/button[1]/a")
    EVENTS_TAG_BUTTON = (By.XPATH, "//*[@id='main-content']/div/div[2]/div/app-tag-filter/div/div/button[2]/a")
    EDUCATION_TAG_BUTTON = (By.XPATH, "//*[@id='main-content']/div/div[2]/div/app-tag-filter/div/div/button[3]/a")
    INITIATIVES_TAG_BUTTON = (By.XPATH, "//*[@id='main-content']/div/div[2]/div/app-tag-filter/div/div/button[4]/a")
    ADS_TAG_BUTTON = (By.XPATH, "//*[@id='main-content']/div/div[2]/div/app-tag-filter/div/div/button[5]/a")

    # News elements
    FIRST_NEWS_ON_ECO_NEWS = (
        By.XPATH,
        "//*[@id='main-content']/div/div[4]/ul/li[1]/a/app-news-list-gallery-view/div/div/div[2]/div[1]/h3",
    )
    NEWS_COUNT_STRING = (By.XPATH, "//*[@id='main-content']/div/div[3]/app-remaining-count/div/h2")
    NEWS_TITLES = (By.CSS_SELECTOR, "ul[aria-label='news list'] li h3")
    NEWS_OWNER = (By.CSS_SELECTOR, "ul[aria-label='news list'] li p span")
    NEWS_TILES = (By.CSS_SELECTOR, "ul[aria-label='news list'] li")

    NEWS_TAGS_IN_TILES = "//app-news-list-gallery-view/div/div/div[1]"

    # Tags button
    TAGS_XPATH = {
        "NEWS": "//app-tag-filter/div/div/button[1]/a",
        "EVENTS": "//app-tag-filter/div/div/button[2]/a",
        "EDUCATION": "//app-tag-filter/div/div/button[3]/a",
        "INITIATIVES": "//app-tag-filter/div/div/button[4]/a",
        "ADS": "//app-tag-filter/div/div/button[5]/a",
    }

    # Search elements
    SEARCH_BUTTON = (By.XPATH, "//*[@id='main-content']/div/div[1]/div/div/div[1]/span")
    SEARCH_TEXTBOX = (By.XPATH, "//*[@id='main-content']/div/div[1]/div/div/div[1]/input")

    # Tag mapping dictionary
    TAG_BUTTON_MAP = {
        "NEWS": NEWS_TAG_BUTTON,
        "EVENTS": EVENTS_TAG_BUTTON,
        "EDUCATION": EDUCATION_TAG_BUTTON,
        "INITIATIVES": INITIATIVES_TAG_BUTTON,
        "ADS": ADS_TAG_BUTTON,
    }

    @allure.step("Open a first news item in the news list")
    def go_to_first_news(self) -> NewsPage:
        first_news = self.driver.find_element(*self.FIRST_NEWS_ON_ECO_NEWS)
        first_news.click()
        self.driver.implicitly_wait(10)
        return NewsPage(self.driver)

    @allure.step("Click 'Create news' button")
    def click_create_news_button(self) -> CreateNewsPage:
        """Click the "create news" button and go to the CreateNewsPage."""
        publish_btn = self.get_wait().until(EC.element_to_be_clickable(self.CREATE_NEWS))
        publish_btn.click()
        return CreateNewsPage(self.driver)

    @allure.step("Check 'Eco news' page title")
    def check_eco_news_title(self) -> None:
        """Verify the eco news page title matches expected text."""
        title_element = self.get_wait().until(EC.presence_of_element_located(self.ECO_NEWS_TITLE))
        actual_text = title_element.text
        assert actual_text == ECO_NEWS_TITLE_TEXT

    @allure.step("get news count from string")
    def get_news_count_from_string(self) -> int:
        """Extract and return the news count from the count string element."""
        count_element = self.get_wait().until(EC.presence_of_element_located(self.NEWS_COUNT_STRING))
        count_string = count_element.text
        return int(count_string.split(" ")[0])

    @allure.step("click tag filter")
    def click_tag_filter(self, tag: str) -> None:
        """Click a tag filter button by tag name.

        Args:
            tag: The tag name (e.g., 'NEWS', 'EVENTS', 'EDUCATION', etc.)
        """
        if tag not in self.TAG_BUTTON_MAP:
            raise ValueError(f"Unknown tag: {tag}. Available tags: {list(self.TAG_BUTTON_MAP.keys())}")

        tag_button = self.get_wait().until(EC.element_to_be_clickable(self.TAG_BUTTON_MAP[tag]))
        tag_button.click()
        self.driver.refresh()

    @allure.step("get all tags after press tag")
    def get_all_tags_after_press_tag(self) -> List[str]:
        """Get all news tags on page.

        Returns:
            List of tag strings from all news items.
        """
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
            all_tags_on_page = [
                el.text for el in self.driver.find_elements(By.XPATH, self.NEWS_TAGS_IN_TILES) if el.is_displayed()
            ]
            self.driver.execute_script("window.scrollTo(0, 0);")

            return all_tags_on_page
        except NoSuchElementException:
            return []

    @allure.step("Check if a tag filter is active")
    def is_tag_filter_active(self, tag: str) -> bool:
        """Check if a tag filter is currently active by checking its background color.

        Args:
            tag: The tag name to check.

        Returns:
            True if the tag filter is active, False otherwise.
        """
        if tag not in self.TAG_BUTTON_MAP:
            raise ValueError(f"Unknown tag: {tag}. Available tags: {list(self.TAG_BUTTON_MAP.keys())}")

        element = self.get_wait().until(EC.presence_of_element_located(self.TAG_BUTTON_MAP[tag]))
        element_color = element.value_of_css_property("background-color")
        return self.EXPECTED_ACTIVE_COLOR == element_color

    @allure.step("get news titles on page")
    def get_news_items_titles(self) -> List[WebElement]:
        """Scroll through the page and collect all visible news items.

        Returns:
            List of WebElement objects representing news tiles.
        """
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(self.SCROLL_PAUSE_TIME)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        elements = [el for el in self.driver.find_elements(*self.NEWS_TILES) if el.is_displayed()]
        self.driver.execute_script("window.scrollTo(0, 0);")
        return elements

    @allure.step("Click bookmark button")
    def click_bookmark_button(self) -> None:
        """Click the bookmark button."""
        bookmark_button = self.get_wait().until(EC.element_to_be_clickable(self.BOOKMARK_BUTTON))
        bookmark_button.click()

    @allure.step("Get all news items that have active bookmarks")
    def news_with_bookmark(self) -> List[WebElement]:
        """Get all news items that have active bookmarks.

        Returns:
            List of WebElement objects with active bookmark flags.
        """
        return self.driver.find_elements(By.CSS_SELECTOR, ".flag-active")

    @allure.step("Enter search text")
    def search_enter_text(self, word: str) -> None:
        """Enter search text character by character with delay.

        Args:
            word: The search term to enter.
        """
        search_button = self.get_wait().until(EC.element_to_be_clickable(self.SEARCH_BUTTON))
        search_button.click()

        search_textbox = self.get_wait().until(EC.element_to_be_clickable(self.SEARCH_TEXTBOX))
        for character in word:
            search_textbox.send_keys(character)
            time.sleep(self.CHARACTER_INPUT_DELAY)

    @allure.step("Get all news items written by user")
    def news_written_by_user(self, user: str) -> List[WebElement]:
        """Get all news items written by a specific user.

        Args:
            user: The username to filter by.

        Returns:
            List of WebElement objects for news written by the specified user.
        """
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(self.SCROLL_PAUSE_TIME)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        news_by_user = [
            el for el in self.driver.find_elements(*self.NEWS_TILES) if el.is_displayed() and user in el.text
        ]

        self.driver.execute_script("window.scrollTo(0, 0);")
        return news_by_user

    @allure.step("click event icon")
    def click_event_icon(self) -> None:
        """Click the event icon button."""
        event_button = self.get_wait().until(EC.element_to_be_clickable(self.EVENT_ICON_BUTTON))
        event_button.click()
