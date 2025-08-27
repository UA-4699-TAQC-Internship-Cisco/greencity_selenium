import pytest

from pages import BasePage
from pages.create_news_page import CreateNewsPage
from pages.eco_news_list_page import EcoNewsListPage


@pytest.mark.create_news
def test_create_news(logged_in_driver):
    # Navigation to Create News
    header = BasePage(logged_in_driver).get_header()
    header.click_eco_news_button()

    eco_news = EcoNewsListPage(logged_in_driver)
    eco_news.click_create_news_button()

    create_news_page = CreateNewsPage(logged_in_driver)
    create_news_page.check_page_title()
    create_news_page.enter_news_title()
    create_news_page.click_news_tag()
    create_news_page.click_education_tag()
    create_news_page.enter_source_link()
    create_news_page.enter_news_text()
    create_news_page.click_publish_button()
    create_news_page.check_loading_message()
    create_news_page.verify_news_title()
    create_news_page.verify_news_tag()
    create_news_page.verify_news_content()
    create_news_page.verify_username_on_news_tile()
