import time

import pytest

from pages.eco_news_list_page import EcoNewsListPage


@pytest.mark.check_bookmark_button
def test_check_bookmark_button(login_driver):
    """Test the current count of news with bookmark."""
    page = EcoNewsListPage(login_driver).get_header().click_eco_news_button()

    time.sleep(3)
    page.click_bookmark_button()
    bookmark_items = len(page.get_news_items_titles())
    page.click_bookmark_button()
    count_news_with_bookmark = len(page.news_with_bookmark())

    assert count_news_with_bookmark == bookmark_items
