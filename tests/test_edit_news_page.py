import pytest

from pages.edit_news_page import EditNewsPage


@pytest.mark.edit_news_content
def test_edit_news_content_field(logged_in_driver):
    edit_news = EditNewsPage(logged_in_driver)

    edit_news.open_news_page()
    edit_news.edit_news_btn()
    edit_news.edit_content_field()
    logged_in_driver.save_screenshot("edited_page.png")
    edit_news.check_edit_news_btn()
    edit_news.verify_warning_msg1()
    edit_news.verify_warning_msg2()
    edit_news.click_edit_news_btn()
