import time
import pytest
from pages.eco_news_list_page import EcoNewsListPage


@pytest.mark.test_check_search_field_on_the_eco_news_page
def test_test_check_search_field(login_driver):
    page = EcoNewsListPage(login_driver)
    page.open_page_by_link("https://www.greencity.cx.ua/#/greenCity/news")
    search_words = ["Tigers", "Test", "Сміття"]

    for word in search_words:

        word_tiles_count = 0
        tiles = page.get_news_tiles_count()
        for tile in tiles:
            if word in tile.text:
                word_tiles_count += 1

        page.search(word)
        time.sleep(5)


        word_count_after_search = page.get_news_count_from_string()
        assert int(word_tiles_count) == int(word_count_after_search)
        page.driver.refresh()
