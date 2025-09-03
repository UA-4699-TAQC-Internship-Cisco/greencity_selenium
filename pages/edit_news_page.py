import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config.resources import COMMENT_TEXT, EDITED_CONTENT, EDITED_CONTENT_TEXT, NEWS_LINK, WARNING_MSG1, WARNING_MSG2
from pages.base_page import BasePage


class EditNewsPage(BasePage):
    EDIT_CONTENT = (By.XPATH, "//div[@class='ql-editor']")
    WARNING_MESSAGE1 = (By.XPATH, "//p[@class='field-info warning']")
    WARNING_MESSAGE2 = (By.XPATH, "//p[@class='quill-counter warning']")
    EDIT_NEWS_BTN = (By.XPATH, "//button[contains(@class,'primary-global-button') and @disabled]")
    YES_CANCEL_BTN = (By.XPATH, "//button[@class='m-btn primary-global-button']")
    CONTENT_FIELD = (By.XPATH, "//div[@class='ql-editor ql-blank']")
    COMMENT_FIELD = (By.XPATH, "//div[@class='comment-textarea']")
    ADD_COMMENT_IMAGE = (By.XPATH, "//mat-icon[text()='image']")
    IMAGE_PATH = r"config/test_image.png"

    @allure.step("Open News Page")
    def open_news_page(self):
        self.open_page_by_link(NEWS_LINK)
        return self

    @allure.step("Edit 'Content' field to 19 symbols")
    def edit_content_field(self):
        enter_content = self.get_wait().until(EC.element_to_be_clickable(self.EDIT_CONTENT))
        assert enter_content.is_enabled()
        enter_content.clear()
        enter_content.send_keys(EDITED_CONTENT)
        return self

    @allure.step("Edit 'Content' field")
    def edit_content_text(self):
        enter_content = self.get_wait().until(EC.element_to_be_clickable(self.EDIT_CONTENT))
        assert enter_content.is_enabled()
        enter_content.clear()
        enter_content.send_keys(EDITED_CONTENT_TEXT)
        return self

    @allure.step("Check 'Edit news' button disabled")
    def check_edit_news_btn(self):
        edit_news_btn = self.get_wait().until(EC.visibility_of_element_located(self.EDIT_NEWS_BTN))
        assert not edit_news_btn.is_enabled()

    @allure.step("Verify warning message 1")
    def verify_warning_msg1(self):
        warning_msg = self.get_wait().until(EC.visibility_of_element_located(self.WARNING_MESSAGE1))
        actual_title = warning_msg.text
        assert actual_title == WARNING_MSG1

    @allure.step("Verify warning message 2")
    def verify_warning_msg2(self):
        warning_msg = self.get_wait().until(EC.visibility_of_element_located(self.WARNING_MESSAGE2))
        actual_title = warning_msg.text
        assert actual_title == WARNING_MSG2

    @allure.step("Check 'Edit news' button disabled")
    def click_edit_news_btn(self):
        until = self.get_wait().until(EC.visibility_of_element_located(self.EDIT_NEWS_BTN))
        click_news_btn = until
        assert click_news_btn.get_attribute("disabled") is not None
        assert not click_news_btn.is_enabled()

    @allure.step("Click 'Yes, cancel' button")
    def click_yes_cancel_btn(self):
        cancel_btn = self.get_wait().until(EC.element_to_be_clickable(self.YES_CANCEL_BTN))
        cancel_btn.click()

    @allure.step("Add news comment")
    def add_news_comment(self):
        enter_content = self.get_wait().until(EC.element_to_be_clickable(self.COMMENT_FIELD))
        assert enter_content.is_enabled()
        enter_content.clear()
        enter_content.send_keys(COMMENT_TEXT)
        return self

    @allure.step("Add image to news comment")
    def click_add_image_button(self):
        pass

    @allure.step("Add image to news comment")
    def add_image_to_comment(self):
        file_input = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.ADD_COMMENT_IMAGE))
        file_input.send_keys(self.IMAGE_PATH)
