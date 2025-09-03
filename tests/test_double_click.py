import pytest

from pages.news_page import NewsPage


@pytest.mark.double_click_on_like
def test_double_click_on_like(login_driver):
    """Double click comment like test."""
    page = NewsPage(login_driver)
    page.open_page_by_link("https://www.greencity.cx.ua/#/greenCity/news/42")
    before_double_like_click = page.get_comment_likes_count()
    page.double_click_comment_like()
    after_double_like_count = page.get_comment_likes_count()
    assert before_double_like_click == (after_double_like_count - 1)
