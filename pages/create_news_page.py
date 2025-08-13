from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.resources import CONTENT_TEXT, TITLE_TEXT, LINK
from pages.base_page import BasePage
from pages.locators.create_news_page_locators import *
import allure


class CreateNewsPage(BasePage):


    @allure.step("Check 'Create news' page title")
    def check_page_title(self):
        title_element = self.get_wait().until(EC.presence_of_element_located(PAGE_TITLE))
        actual_text = title_element.text
        assert actual_text == "Create news"

    @allure.step("Enter text in to 'Title' field")
    def enter_news_title(self):
        input_title = self.get_wait().until(EC.visibility_of_element_located(INPUT_TITLE))
        input_title.clear()
        input_title.send_keys(TITLE_TEXT)
        return self

    # Tags
    @allure.step("Click 'News' tag")
    def click_news_tag(self):
        news_tag = self.get_wait().until(EC.element_to_be_clickable(NEWS_TAG))
        news_tag.click()

    @allure.step("Click 'Events' tag")
    def click_events_tag(self):
        events_tag = self.get_wait().until(EC.element_to_be_clickable(EVENTS_TAG))
        events_tag.click()

    @allure.step("Click 'Education' tag")
    def click_education_tag(self):
        education_tag = self.get_wait().until(EC.element_to_be_clickable(EDUCATION_TAG))
        education_tag.click()

    @allure.step("Click 'Initiatives' tag")
    def click_initiatives_tag(self):
        initiatives_tag = self.get_wait().until(EC.element_to_be_clickable(INITIATIVES_TAG))
        initiatives_tag.click()

    @allure.step("Click 'Ads' tag")
    def click_ads_tag(self):
        ads_tag = self.get_wait().until(EC.element_to_be_clickable(ADS_TAG))
        ads_tag.click()

    # Link
    @allure.step("Enter link in to 'Source' field")
    def enter_source_link(self):
        source_link = self.get_wait().until(EC.visibility_of_element_located(INPUT_SOURCE))
        source_link.clear()
        source_link.send_keys(LINK)
        return self

    # Upload image
    def upload_image(self):
        pass

    # Buttons
    def click_submit_picture_button(self):
        pass

    def click_cancel_picture_button(self):
        pass

    # Content field
    @allure.step("Enter text in to 'Content' field")
    def enter_news_text(self):
        enter_content = self.get_wait().until(EC.visibility_of_element_located(CONTENT_FIELD))
        enter_content.clear()
        enter_content.send_keys(CONTENT_TEXT)
        return self

    @allure.step("Click 'Publish' button")
    def click_publish_button(self):
        publish_btn = self.get_wait().until(EC.element_to_be_clickable(PUBLISH_BUTTON))
        publish_btn.click()

    def click_preview_button(self):
        pass

    @allure.step("Check text 'Please wait while loading'")
    def check_loading_message(self):
        loading_text = self.get_wait().until(EC.presence_of_element_located(lOADING_MESSAGE))
        actual_text = loading_text.text
        assert actual_text == "Please wait while loading..."

    @allure.step("Verify 'News title' on tile")
    def verify_news_title(self):
        verify_title_text = self.get_wait().until(EC.presence_of_element_located(TITLE_ON_NEWS))
        actual_title = verify_title_text.text
        assert actual_title == TITLE_TEXT

    @allure.step("Verify 'News tag' on tile")
    def verify_news_tag(self):
        verify_news_tag = self.get_wait().until(EC.presence_of_element_located(TAG_ON_NEWS))
        actual_tag = verify_news_tag.text
        assert actual_tag == "NEWS"

    @allure.step("Verify 'News content' on tile")
    def verify_news_content(self):
        verify_news_content = self.get_wait().until(EC.presence_of_element_located(TEXT_ON_NEWS))
        actual_content = verify_news_content.text
        assert actual_content == "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

    @allure.step("Verify 'Username' on tile")
    def verify_username_on_news_tile(self):
        verify_username = self.get_wait().until(EC.presence_of_element_located(AUTHOR_ON_NEWS))
        actual_name = verify_username.text
        assert actual_name == EXPECTED_USERNAME
