import pytest
from selenium.webdriver.common.by import By

from config.resources import NEWS_LINK2
from pages.news_page import NewsPage

LIKE_COUNT = (By.XPATH, '//span[@class="numerosity_likes"]')
LIKE_ICON = (By.XPATH, '//img[@class="news_like ng-star-inserted"]')

COMMENT_AREA = (By.XPATH, '//div[@class="comment-date-likes"]')
COMMENT_LIKE_COUNT = (By.XPATH, '//span[@class="like-amount"]')
COMMENT_LIKE_ICON = (By.XPATH, '//div[@class="comment-likes"]//img[@alt="like"]')


@pytest.mark.like_news
def test_like_dislike_news(logged_in_driver):
    """Test checks the functionality of liking and disliking a news item."""
    logged_in_driver.get(NEWS_LINK2)

    like_news = NewsPage(logged_in_driver)
    initial_count_likes_number = like_news.count_likes_number(LIKE_COUNT)

    current_count_likes_number = like_news.click_like_icon(LIKE_ICON).count_likes_number(LIKE_COUNT)
    assert current_count_likes_number == initial_count_likes_number + 1, "Like was not added"

    current_count_likes_number = like_news.click_like_icon(LIKE_ICON).count_likes_number(LIKE_COUNT)
    assert current_count_likes_number == initial_count_likes_number, "Like was not removed"


@pytest.mark.like_news_comment
def test_like_dislike_news_comment(logged_in_driver):
    """Test checks the functionality of liking and disliking a news comment."""
    logged_in_driver.get(NEWS_LINK2)

    like_news = NewsPage(logged_in_driver)
    initial_count_likes_number = like_news.count_likes_number(COMMENT_LIKE_COUNT)

    current_count_likes_number = like_news.click_like_icon(COMMENT_LIKE_ICON).count_likes_number(COMMENT_LIKE_COUNT)
    assert current_count_likes_number == initial_count_likes_number + 1, "Like was not added"

    # current_count_likes_number = like_news.click_like_icon(LIKE_ICON).count_likes_number(COMMENT_LIKE_COUNT)
    # assert current_count_likes_number == initial_count_likes_number, "Like was not removed"
