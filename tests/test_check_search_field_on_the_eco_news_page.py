import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.eco_news_list_page import EcoNewsListPage


@pytest.mark.test_check_search_field_on_the_eco_news_page
def test_check_search_field(login_driver):
    """Test search field functionality on the eco news page.

    This test verifies that the search functionality correctly filters news items
    based on the search terms entered.
    """
    page = EcoNewsListPage(login_driver)
    page.open_page_by_link("https://www.greencity.cx.ua/#/greenCity/news")

    # Wait for page to load
    wait = WebDriverWait(login_driver, 10)
    wait.until(EC.presence_of_element_located(page.NEWS_COUNT_STRING))

    search_words = ["Test", "Tigers", "Сміття", "What"]

    for word in search_words:
        word_tiles_count = 0
        titles = page.get_news_items_titles()

        for title in titles:
            if word.lower() in title.text.lower():
                word_tiles_count += 1

        page.search_enter_text(word)

        # Wait for search results to load
        wait.until(EC.presence_of_element_located(page.NEWS_COUNT_STRING))

        word_count_after_search = page.get_news_count_from_string()
        assert int(word_tiles_count) == int(word_count_after_search)

        login_driver.refresh()
        # Wait for page refresh to complete
        wait.until(EC.presence_of_element_located(page.NEWS_COUNT_STRING))
