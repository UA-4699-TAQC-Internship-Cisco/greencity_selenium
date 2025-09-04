import pytest

from config.resources import NEWS_LINK2
from pages.edit_news_page import EditNewsPage
from pages.news_page import NewsPage


@pytest.mark.edit_news_content
def test_edit_news_content_field(logged_in_driver):
    """This function checks edit news content."""
    edit_news = EditNewsPage(logged_in_driver)

    edit_news.open_news_page()
    news = NewsPage(logged_in_driver)
    news.edit_news_btn()

    edit_news.edit_content_field()
    edit_news.check_edit_news_btn()
    edit_news.verify_warning_msg1()
    edit_news.verify_warning_msg2()
    edit_news.click_edit_news_btn()


@pytest.mark.like_news_comment
def test_comment_with_image(logged_in_driver):
    """Test checks the functionality of liking and disliking a news comment."""
    logged_in_driver.get(NEWS_LINK2)

    edit_comment = EditNewsPage(logged_in_driver)

    edit_comment.add_news_comment()
    edit_comment.click_add_image_icon()
    edit_comment.click_comment_button()
    # edit_comment.check_image_present()
    # edit_comment.verify_comment_text()
    # edit_comment.verify_commenter()
