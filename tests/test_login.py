import pytest

from config.resources import EXPECTED_USERNAME, HOME_GREEN_CITY_UI, USER_EMAIL, USER_PASSWORD
from pages.eco_news_list_page import EcoNewsListPage


@pytest.mark.login
def test_positive_login(driver_uc):
    driver_uc.get(HOME_GREEN_CITY_UI)
    displayed_name = (EcoNewsListPage(driver_uc)
                      .get_header()
                      .click_sign_in()
                      .click_captcha()
                      .enter_email(USER_EMAIL)
                      .enter_password(USER_PASSWORD)
                      .click_sign_in_btn()
                      .get_header()
                      .get_displayed_username())

    assert displayed_name == EXPECTED_USERNAME

    driver_uc.save_screenshot("username_check.png")
