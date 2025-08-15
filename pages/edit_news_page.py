from selenium.webdriver.support import expected_conditions as EC
from pages.locators.create_news_page_locators import *
import allure

from pages.locators.edit_news_page_locators import EDIT_NEWS_BTN, WARNING_MESSAGE1, WARNING_MESSAGE2, EDIT_CONTENT, \
    EDIT_NEWS
from pages.news_page import NewsPage


class EditNewsPage(NewsPage):

    @allure.step("Open News Page")
    def open_news_page(self):
        self.open_page_by_link(NEWS_LINK)
        return self

    @allure.step("Click 'Edit news' button")
    def edit_news_btn(self):
        edit_news_btn = self.get_wait().until(EC.element_to_be_clickable(EDIT_NEWS))
        edit_news_btn.click()

    @allure.step("Edit 'Content' field to 19 symbols")
    def edit_content_field(self):
        enter_content = self.get_wait().until(EC.element_to_be_clickable(EDIT_CONTENT))
        assert enter_content.is_enabled()
        enter_content.clear()
        enter_content.send_keys(EDITED_CONTENT)
        return self

    @allure.step("Check 'Edit news' button disabled")
    def check_edit_news_btn(self):
        edit_news_btn = self.get_wait().until(EC.visibility_of_element_located(EDIT_NEWS_BTN))
        assert not edit_news_btn.is_enabled()

    @allure.step("Verify warning message 1")
    def verify_warning_msg1(self):
        warning_msg = self.get_wait().until(EC.visibility_of_element_located(WARNING_MESSAGE1))
        actual_title = warning_msg.text
        assert actual_title == WARNING_MSG1

    @allure.step("Verify warning message 2")
    def verify_warning_msg2(self):
        warning_msg = self.get_wait().until(EC.visibility_of_element_located(WARNING_MESSAGE2))
        actual_title = warning_msg.text
        assert actual_title == WARNING_MSG2

    @allure.step("Check 'Edit news' button disabled")
    def click_edit_news_btn(self):
        until = self.get_wait().until(EC.visibility_of_element_located(EDIT_NEWS_BTN))
        click_news_btn = until
        assert click_news_btn.get_attribute("disabled") is not None
        assert not click_news_btn.is_enabled()
