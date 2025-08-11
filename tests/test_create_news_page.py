import pytest
from seleniumbase import Driver
from pages.login import LoginPage
from config.resources import EXPECTED_USERNAME, DOMAIN, USER_EMAIL, USER_PASSWORD
from pages.create_news_page import CreateNewsPage


@pytest.mark.login
def test_positive_login():
    driver = Driver(uc=True, headless=False)

    # Login
    login_page = LoginPage(driver)
    login_page.open_login_page(DOMAIN) \
        .enter_email(USER_EMAIL) \
        .enter_password(USER_PASSWORD) \
        .click_login()

    displayed_name = login_page.get_displayed_username()
    assert displayed_name == EXPECTED_USERNAME

    # Navigation to Create News
    login_page.click_green_city_button()
    login_page.click_eco_news_button()
    login_page.click_create_news_button()

    # Check title
    create_news_page = CreateNewsPage(driver)
    create_news_page.check_page_title()

    # Input title
    input_text_title = CreateNewsPage(driver)
    input_text_title.enter_news_title()

    # Click 'News' tag
    click_news_tag = CreateNewsPage(driver)
    click_news_tag.click_news_tag()

    # Click 'Education' tag
    click_education_tag = CreateNewsPage(driver)
    click_education_tag.click_education_tag()

    # Enter Source link
    source_link = CreateNewsPage(driver)
    source_link.enter_source_link()

    # Enter Content text
    content = CreateNewsPage(driver)
    content.enter_news_text()

    # Click publish button
    publish_btn = CreateNewsPage(driver)
    publish_btn.click_publish_button()

    driver.quit()
