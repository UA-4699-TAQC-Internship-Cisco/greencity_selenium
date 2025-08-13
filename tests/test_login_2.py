import pytest
from seleniumbase import Driver
from pages.login import LoginModal
from config.resources import HOME_GREEN_CITY_UI, USER_EMAIL, USER_PASSWORD, EXPECTED_USERNAME


@pytest.fixture(scope="class")
def setup_login():
    driver = Driver(uc=True, headless=False)
    login_page = LoginModal(driver)
    login_page.open_login_page(HOME_GREEN_CITY_UI)
    yield login_page
    driver.save_screenshot("login_success.png")
    driver.quit()


@pytest.mark.login
class TestLoginSteps:

    def test_step_1_enter_email(self, setup_login):
        setup_login.enter_email(USER_EMAIL)

    def test_step_2_enter_password(self, setup_login):
        setup_login.enter_password(USER_PASSWORD)

    def test_step_3_click_login(self, setup_login):
        setup_login.click_login()

    def test_step_4_verify_username_displayed(self, setup_login):
        assert setup_login.get_displayed_username() == EXPECTED_USERNAME
