import pytest

from pages import BasePage
from pages.eco_news_list_page import EcoNewsListPage
from pages.edit_news_page import EditNewsPage
from pages.header_component import Header
from pages.news_page import NewsPage


@pytest.mark.edit_news_content
def test_edit_news_content_field(logged_in_driver):
    base_page = BasePage(logged_in_driver)

    edit_news = EditNewsPage(logged_in_driver)
    edit_news.open_news_page()

    news = NewsPage(logged_in_driver)
    news.edit_news_btn()
    edit_news.edit_content_text()
    logged_in_driver.save_screenshot("edited_text.png")
    eco_news_btn = Header(logged_in_driver, node=None)
    eco_news_btn.click_eco_news_button()
    edit_news.click_yes_cancel_btn()

    page_title = EcoNewsListPage(logged_in_driver)
    page_title.check_eco_news_title()

    edit_news.open_news_page()
    news.check_news_title()
