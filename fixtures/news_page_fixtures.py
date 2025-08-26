import pytest

from config.resources import HOME_GREEN_CITY_UI
from pages.news_page import NewsPage


@pytest.fixture
def send_comment_and_get_comment_data(login_driver):
    def _sender_getter(text):
        page=NewsPage(login_driver)
        page.go_to_first_news()
        page.send_message(text)
        return page.get_first_comment_data()
    return _sender_getter

