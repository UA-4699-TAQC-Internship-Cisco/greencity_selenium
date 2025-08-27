import pytest

from pages.eco_news_list_page import EcoNewsListPage


@pytest.mark.check_items_count_by_tags
def test_check_items_count_by_tags(login_driver):
    page = EcoNewsListPage(login_driver).get_header().click_eco_news_button()
    tags = ["NEWS", "EVENTS", "EDUCATION", "INITIATIVES", "ADS"]

    # TOTAL
    tiles_count = len(page.get_news_items_titles())
    string_count = page.get_news_count_from_string()
    assert tiles_count == string_count

    for tag in tags:
        page.click_tag_filter(tag)
        tiles_count = len(page.get_news_items_titles())
        news_count = page.get_news_count_from_string()
        assert tiles_count == news_count
        page.click_tag_filter(tag)
