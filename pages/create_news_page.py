import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from config.resources import CONTENT_TEXT, TITLE_TEXT, EXPECTED_USERNAME, LINK
from pages.base_page import BasePage
from pages.preview_create_news_page import PreviewNewsPage


class CreateNewsPage(BasePage):
    PAGE_TITLE = (By.XPATH, "//h2[@class='title-header']")
    INPUT_TITLE = (By.XPATH, "//textarea[@formcontrolname='title']")

    NEWS_TAG = (By.XPATH, "//span[@class='text' and text()='News']")
    EVENTS_TAG = (By.XPATH, "//span[@class='text' and text()='Events']")
    EDUCATION_TAG = (By.XPATH, "//span[@class='text' and text()='Education']")
    INITIATIVES_TAG = (By.XPATH, "//span[@class='text' and text()='Initiatives']")
    ADS_TAG = (By.XPATH, "//span[@class='text' and text()='Ads']")

    INPUT_SOURCE = (By.XPATH, "//input[@placeholder='Link to external source']")
    # UPLOAD_PICTURE
    CONTENT_FIELD = (By.XPATH, "//div[@class='ql-editor ql-blank']")

    CANCEL_PICTURE = (By.XPATH, "//button[@class='secondary-global-button s-btn']")
    SUBMIT_PICTURE = (By.XPATH, "//button[@class='primary-global-button s-btn']")

    PUBLISH_BUTTON = (By.XPATH, "//button[@class='primary-global-button']")
    PREVIEW_BUTTON = (By.XPATH, "//button[@class='secondary-global-button']")
    CANCELL_BUTTON = (By.XPATH, "//button[@class='tertiary-global-button']")

    lOADING_MESSAGE = (By.XPATH, "//p[@class='header' and text()='Please wait while loading...']")

    TITLE_ON_NEWS = (By.XPATH,
                     f"(//div[@class='title-list word-wrap']/h3[contains(normalize-space(), '{TITLE_TEXT}')])[1]")

    TAG_ON_NEWS = (By.XPATH, "(//app-news-list-gallery-view//span[contains(text(), 'News')])[1]")

    TEXT_ON_NEWS = (By.XPATH, f"(//li[.//h3[contains(normalize-space(), \
          'What is Lorem Ipsum?')]]//p[contains(normalize-space(), \
          '{CONTENT_TEXT}')])[1]")

    AUTHOR_ON_NEWS = (By.XPATH, "(//app-news-list-gallery-view//span[contains(text(), 'Marta')])[1]")
    ECO_NEWS_BTN = (By.XPATH, "//a[contains(@class,'url-name') and normalize-space()='Eco news']")

    @allure.step("Check 'Create news' page title")
    def check_page_title(self):
        title_element = self.get_wait().until(EC.presence_of_element_located(self.PAGE_TITLE))
        actual_text = title_element.text
        assert actual_text == "Create news"

    @allure.step("Enter text in to 'Title' field")
    def enter_news_title(self):
        input_title = self.get_wait().until(EC.visibility_of_element_located(self.INPUT_TITLE))
        input_title.clear()
        input_title.send_keys(TITLE_TEXT)
        return self

    # Tags
    @allure.step("Click 'News' tag")
    def click_news_tag(self):
        news_tag = self.get_wait().until(EC.element_to_be_clickable(self.NEWS_TAG))
        news_tag.click()

    @allure.step("Click 'Events' tag")
    def click_events_tag(self):
        events_tag = self.get_wait().until(EC.element_to_be_clickable(self.EVENTS_TAG))
        events_tag.click()

    @allure.step("Click 'Education' tag")
    def click_education_tag(self):
        education_tag = self.get_wait().until(EC.element_to_be_clickable(self.EDUCATION_TAG))
        education_tag.click()

    @allure.step("Click 'Initiatives' tag")
    def click_initiatives_tag(self):
        initiatives_tag = self.get_wait().until(EC.element_to_be_clickable(self.INITIATIVES_TAG))
        initiatives_tag.click()

    @allure.step("Click 'Ads' tag")
    def click_ads_tag(self):
        ads_tag = self.get_wait().until(EC.element_to_be_clickable(self.ADS_TAG))
        ads_tag.click()

    # Link
    @allure.step("Enter link in to 'Source' field")
    def enter_source_link(self):
        source_link = self.get_wait().until(EC.visibility_of_element_located(self.INPUT_SOURCE))
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
        enter_content = self.get_wait().until(EC.visibility_of_element_located(self.CONTENT_FIELD))
        enter_content.clear()
        enter_content.send_keys(CONTENT_TEXT)
        return self

    @allure.step("Click 'Publish' button")
    def click_publish_button(self):
        publish_btn = self.get_wait().until(EC.element_to_be_clickable(self.PUBLISH_BUTTON))
        publish_btn.click()

    @allure.step("Check text 'Please wait while loading'")
    def check_loading_message(self):
        loading_text = self.get_wait().until(EC.presence_of_element_located(self.lOADING_MESSAGE))
        actual_text = loading_text.text
        assert actual_text == "Please wait while loading..."

    @allure.step("Verify 'News title' on tile")
    def verify_news_title(self):
        verify_title_text = self.get_wait().until(EC.presence_of_element_located(self.TITLE_ON_NEWS))
        actual_title = verify_title_text.text
        assert actual_title == TITLE_TEXT

    @allure.step("Verify 'News tag' on tile")
    def verify_news_tag(self):
        verify_news_tag = self.get_wait().until(EC.presence_of_element_located(self.TAG_ON_NEWS))
        actual_tag = verify_news_tag.text
        assert actual_tag == "NEWS"

    @allure.step("Verify 'News content' on tile")
    def verify_news_content(self):
        verify_news_content = self.get_wait().until(EC.presence_of_element_located(self.TEXT_ON_NEWS))
        actual_content = verify_news_content.text
        assert actual_content == CONTENT_TEXT

    @allure.step("Verify 'Username' on tile")
    def verify_username_on_news_tile(self):
        verify_username = self.get_wait().until(EC.presence_of_element_located(self.AUTHOR_ON_NEWS))
        actual_name = verify_username.text
        assert actual_name == EXPECTED_USERNAME

    @allure.step("Enter text in to 'Title' field")
    def enter_title(self, title):
        enter_title = self.driver.find_element(*self.INPUT_TITLE)
        enter_title.clear()
        enter_title.send_keys(title)
        return self

    def press_tag(self, tag_name):
        tags_index = {"NEWS":1, "EVENTS":2, "EDUCATION":3, "INITIATIVES":4, "ADS":5}
        self.driver.find_element(By.XPATH, f"//app-tags-select/button[{tags_index[tag_name.upper()]}]/a/span").click()
        return self

    def enter_link(self, link):
        link_fild = self.driver.find_element(*self.INPUT_SOURCE)
        link_fild.clear()
        link_fild.send_keys(link)
        return self

    def enter_body_text(self, text):
        enter_content = self.driver.find_element(*self.CONTENT_FIELD)
        enter_content.clear()
        enter_content.send_keys(text)
        return self

    def click_preview_button(self) -> PreviewNewsPage:
        self.driver.find_element(*self.PREVIEW_BUTTON).click()
        return PreviewNewsPage(self.driver)

