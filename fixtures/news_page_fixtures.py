import pytest

from pages.eco_news_list_page import EcoNewsListPage
from pages.news_page import NewsPage

__all__ = ["send_comment_and_get_comment_data"]


@pytest.fixture
def send_comment_and_get_comment_data(login_driver):
    """Fixture to send a comment and retrieve the comment data."""

    def _sender_getter(text):
        comment = EcoNewsListPage(login_driver).go_to_first_news().send_message(text).get_first_comment_data()
        return comment

    return _sender_getter
