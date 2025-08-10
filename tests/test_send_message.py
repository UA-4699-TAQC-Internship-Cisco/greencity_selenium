import pytest
from pages.news_page import NewsPage


@pytest.fixture
def send_comment_and_get_comment_data():
    def _sender_getter(text):
        page=NewsPage()
        page.open_page_by_link("https://www.greencity.cx.ua/#/greenCity")
        #sing_in
        page.go_to_first_news()
        page.send_message(text)
        return page.get_first_comment_data()
    return _sender_getter

@pytest.fixture
def get_news_title():
    page=NewsPage()
    page.open_page_by_link("https://www.greencity.cx.ua/#/greenCity")
    page.go_to_first_news()
    title=page.get_news_title()
    return title


def test_check_news_title_text(get_news_title):
    assert send_comment_and_get_comment_data == 'UpdatedTitleOR'


def test_send_message(send_comment_and_get_comment_data):
    comment_data=send_comment_and_get_comment_data("some valid text for the test")
    assert comment_data == {
            'author': "user from .env",     #change user
            'text': "some valid text for the test"
        }


