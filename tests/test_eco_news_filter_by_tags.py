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
        all_tags = [item for element in page.get_all_tags_after_press_tag() for item in element.split('|\n')]
        assert all_tags.count(tag) == page.get_news_count_from_string()
        assert page.is_tag_filter_active(tag)
        page.click_tag_filter(tag)
