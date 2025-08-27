import pytest

from config.resources import USERNAME
from pages.eco_news_list_page import EcoNewsListPage


@pytest.mark.check_personal_event_icon
def test_check_personal_event_icon(login_driver):
    page = EcoNewsListPage(login_driver)
    page.open_page_by_link("https://www.greencity.cx.ua/#/greenCity/news")
    page.click_tag_filter("EVENTS")
    count_users_news = len(page.news_written_by_user(USERNAME))
    page.click_event_icon()
    count_event_news = page.get_news_items_titles()

    assert count_event_news == count_users_news
