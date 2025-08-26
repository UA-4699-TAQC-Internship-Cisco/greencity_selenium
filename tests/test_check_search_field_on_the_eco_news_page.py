import time
from time import sleep

import pytest
from pages.eco_news_list_page import EcoNewsListPage


@pytest.mark.test_check_search_field_on_the_eco_news_page
def test_test_check_search_field(login_driver):
    page = EcoNewsListPage(login_driver)
    page.open_page_by_link("https://www.greencity.cx.ua/#/greenCity/news")
    search_words = ["Test", "Tigers", "Сміття", "What"]

    for word in search_words:

        word_tiles_count = 0
        titles = page.get_news_items_titles()
        for title in titles:
            if word.lower() in title.text.lower():
                word_tiles_count += 1
        page.search_enter_text(word)

        word_count_after_search = page.get_news_count_from_string()
        assert int(word_tiles_count) == int(word_count_after_search)
        page.driver.refresh()
