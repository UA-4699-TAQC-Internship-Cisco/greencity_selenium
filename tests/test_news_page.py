import pytest

from config.resources import NEWS_LINK2
from pages.edit_news_page import EditNewsPage
from pages.news_page import NewsPage


@pytest.mark.like_news
def test_like_dislike_news(logged_in_driver):
    """Test checks the functionality of liking and disliking a news item."""
    logged_in_driver.get(NEWS_LINK2)

    like_news = NewsPage(logged_in_driver)
    initial_count_likes_number = like_news.count_likes_number()

    current_count_likes_number = like_news.click_like_icon().count_likes_number()
    assert current_count_likes_number == initial_count_likes_number + 1, "Like was not added"

    current_count_likes_number = like_news.click_like_icon().count_likes_number()
    assert current_count_likes_number == initial_count_likes_number, "Like was not removed"
