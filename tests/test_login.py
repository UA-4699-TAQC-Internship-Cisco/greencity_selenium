import pytest
from pages.login import LoginModal
from config.resources import EXPECTED_USERNAME, HOME_GREEN_CITY_UI, USER_EMAIL, USER_PASSWORD


@pytest.mark.login
def test_positive_login(driver_uc):
    login_page = LoginModal(driver_uc)

    driver_uc.get(HOME_GREEN_CITY_UI)
    login_page.click_captcha()\
        .enter_email(USER_EMAIL)\
        .enter_password(USER_PASSWORD)\
        .click_login()

    displayed_name = login_page.get_displayed_username()
    assert displayed_name == EXPECTED_USERNAME

    driver_uc.save_screenshot("username_check.png")

