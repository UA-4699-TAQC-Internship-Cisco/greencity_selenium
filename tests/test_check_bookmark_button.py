import pytest
import time
from pages.eco_news_list_page import EcoNewsListPage


@pytest.mark.check_bookmark_button
def test_check_bookmark_button(login_driver):
    page = EcoNewsListPage(login_driver)
    page.open_page_by_link("https://www.greencity.cx.ua/#/greenCity/news")

    time.sleep(3)
    page.click_bookmark_button()
    bookmark_items = len(page.get_news_items())
    page.click_bookmark_button()
    count_news_with_bookmark = len(page.news_with_bookmark())

    assert count_news_with_bookmark == bookmark_items

