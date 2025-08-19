import pytest

from config.resources import NEWS_LINK1
from pages import BasePage
from pages.edit_news_page import EditNewsPage
from pages.news_page import NewsPage


@pytest.mark.edit_news_content
def test_edit_news_content_field(logged_in_driver):
    base_page = BasePage(logged_in_driver).get_header()

    news = EditNewsPage(logged_in_driver)
    news.open_page_by_link(NEWS_LINK1)

    first_news = NewsPage(logged_in_driver)
    first_news.get_first_news_title()

    first_news.click_interesting_news()
    first_news.compare_news_titles()
