import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from typing import Generator
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from seleniumbase import Driver
from seleniumbase.core.sb_driver import DriverMethods
from webdriver_manager.chrome import ChromeDriverManager
from config.resources import *
from pages.login import LoginPage


@pytest.fixture()
def driver() -> Generator[webdriver.Chrome, None, None]:
    print("generate driver")
    chrome_options = webdriver.ChromeOptions()

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver

    driver.quit()


@pytest.fixture()
def driver_uc() -> Generator[DriverMethods, None, None]:
    driver = Driver(uc=True, headless=False)
    yield driver
    driver.quit()


@pytest.fixture()
def logged_in_driver(driver_uc):
    login_page = LoginPage(driver_uc)
    login_page.open_login_page(DOMAIN) \
        .enter_email(USER_EMAIL) \
        .enter_password(USER_PASSWORD) \
        .click_login()
    displayed_name = login_page.get_displayed_username()
    assert displayed_name == EXPECTED_USERNAME
    yield driver_uc
