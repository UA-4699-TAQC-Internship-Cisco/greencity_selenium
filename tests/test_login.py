import pytest
from pages.login import LoginPage
from config.resources import EXPECTED_USERNAME, DOMAIN, USER_EMAIL, USER_PASSWORD


@pytest.mark.login
def test_positive_login(driver_uc):
    login_page = LoginPage(driver_uc)

    login_page.open_login_page(DOMAIN) \
        .enter_email(USER_EMAIL) \
        .enter_password(USER_PASSWORD) \
        .click_login()

    displayed_name = login_page.get_displayed_username()
    assert displayed_name == EXPECTED_USERNAME

    driver_uc.save_screenshot("login_success.png")

