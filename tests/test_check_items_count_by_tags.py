import pytest

from pages.eco_news_list_page import EcoNewsListPage



@pytest.mark.check_items_count_by_tags
def test_check_items_count_by_tags(login_driver):
    page = EcoNewsListPage(login_driver)
    page.open_page_by_link("https://www.greencity.cx.ua/#/greenCity/news")
    tags = ["NEWS", "EVENTS", "EDUCATION", "INITIATIVES", "ADS"]

    #TOTAL
    tiles_count = page.get_news_tiles_count()
    string_count = page.get_news_count_from_string()
    assert int(tiles_count) == int(string_count)

    for tag in tags:
        page.click_tag_filter(tag)
        tiles_count = page.get_news_tiles_count()
        string_count = page.get_news_count_from_string()
        assert int(tiles_count) == int(string_count)
        page.click_tag_filter(tag)
