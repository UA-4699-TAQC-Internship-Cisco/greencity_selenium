import time
from typing import Generator

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from seleniumbase import Driver
from seleniumbase.core.sb_driver import DriverMethods
from webdriver_manager.chrome import ChromeDriverManager

from config.resources import (
    EXPECTED_USERNAME,
    HOME_GREEN_CITY_UI,
    IMPLICITLY_WAIT,
    LOCALSTORAGE,
    USER_EMAIL,
    USER_PASSWORD,
)
from pages import BasePage


@pytest.fixture()
def driver() -> Generator[webdriver.Chrome, None, None]:
    """Provide a Chrome WebDriver instance for testing.

    Yields:
        webdriver.Chrome: Configured Chrome WebDriver instance.
    """
    print("generate driver")
    chrome_options = webdriver.ChromeOptions()

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(IMPLICITLY_WAIT)
    driver.maximize_window()
    yield driver

    driver.quit()


@pytest.fixture()
def driver_uc() -> Generator[DriverMethods, None, None]:
    """Provide a SeleniumBase driver with undetected Chrome mode.

    Yields:
        DriverMethods: SeleniumBase driver instance.
    """
    driver = Driver(uc=True, headless=False)
    driver.maximize_window()
    driver.implicitly_wait(IMPLICITLY_WAIT)
    yield driver
    driver.quit()


@pytest.fixture()
def logged_in_driver(driver_uc: DriverMethods) -> Generator[DriverMethods, None, None]:
    """Provide a logged-in driver session.

    Args:
        driver_uc: SeleniumBase driver instance.

    Yields:
        DriverMethods: Logged-in driver session.
    """
    driver_uc.get(HOME_GREEN_CITY_UI)
    print("test started")

    # Wait for page to load instead of using hardcoded sleep
    wait = WebDriverWait(driver_uc, 10)
    wait.until(EC.presence_of_element_located(("xpath", "//header[@aria-label='Welcome to header']")))

    header = BasePage(driver_uc).get_header()
    print(f"{header=}")
    (header.click_sign_in().click_captcha().enter_email(USER_EMAIL).enter_password(USER_PASSWORD).click_sign_in_btn())

    displayed_name = header.get_displayed_username()
    assert displayed_name == EXPECTED_USERNAME

    yield driver_uc


@pytest.fixture()
def login_driver(driver: webdriver.Chrome) -> Generator[webdriver.Chrome, None, None]:
    """Provide a driver with pre-set localStorage authentication tokens.

    Args:
        driver: Chrome WebDriver instance.

    Yields:
        webdriver.Chrome: Driver with authentication tokens set.
    """
    driver.get(HOME_GREEN_CITY_UI)

    # Set localStorage tokens if they exist
    for key, value in LOCALSTORAGE.items():
        if value:
            driver.execute_script(f"window.localStorage.setItem('{key}', '{value}');")

    driver.refresh()
    yield driver

    # Clean up localStorage tokens
    for key in LOCALSTORAGE.keys():
        driver.execute_script(f"localStorage.removeItem('{key}');")

    driver.quit()
