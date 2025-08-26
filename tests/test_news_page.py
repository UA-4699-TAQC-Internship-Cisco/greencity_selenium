import time

import pytest
import unittest

from config.resources import NEWS_LINK2
from pages.edit_news_page import EditNewsPage
from pages.news_page import NewsPage


@pytest.mark.like_news
def test_like_dislike_news(logged_in_driver):
    news = EditNewsPage(logged_in_driver)
    news.open_page_by_link(NEWS_LINK2)

    like_news = NewsPage(logged_in_driver)
    initial_likes = like_news.count_likes_number()
    like_news.click_like_icon()
    time.sleep(3)
    like_news.check_like_added(initial_likes)
    like_news.click_like_icon()
    initial_likes = like_news.count_likes_number()
    time.sleep(3)
    like_news.check_like_removed(initial_likes)

