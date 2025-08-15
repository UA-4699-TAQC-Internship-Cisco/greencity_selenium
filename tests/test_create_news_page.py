import pytest
from pages.login import LoginModal
from pages.create_news_page import CreateNewsPage
from pages.login import LoginModal


@pytest.mark.create_news
def test_create_news(logged_in_driver):
    login_page = LoginModal(logged_in_driver)

    # Navigation to Create News
    login_page.click_eco_news_button()
    login_page.click_create_news_button()

    create_news_page = CreateNewsPage(logged_in_driver)

    # Check title
    create_news_page.check_page_title()

    # Input title
    create_news_page.enter_news_title()

    # Click 'News' tag
    create_news_page.click_news_tag()

    # Click 'Education' tag
    create_news_page.click_education_tag()

    # Enter Source link
    create_news_page.enter_source_link()

    # Enter Content text
    create_news_page.enter_news_text()

    # Click publish button
    create_news_page.click_publish_button()

    # Check loading message
    create_news_page.check_loading_message()

    # Verify news title on tile
    create_news_page.verify_news_title()

    # Verify news tag on tile
    create_news_page.verify_news_tag()

    # Verify news text content on tile
    create_news_page.verify_news_content()

    # Verify username on news tile
    create_news_page.verify_username_on_news_tile()
