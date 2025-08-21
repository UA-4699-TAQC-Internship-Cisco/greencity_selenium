import pytest

from pages.eco_news_list_page import EcoNewsListPage


@pytest.mark.eco_news_filter_by_tags
def test_eco_news_filter_by_tags(login_driver):
    page = EcoNewsListPage(login_driver)
    page.open_page_by_link("https://www.greencity.cx.ua/#/greenCity/news")
    tags = ["NEWS", "EVENTS", "EDUCATION", "INITIATIVES", "ADS"]
    # step_1
    for tag in tags:
        page.click_tag_filter(tag)
        assert page.is_tag_in_list(tag) == True
        assert page.is_tag_filter_active(tag) == True
        page.click_tag_filter(tag)
