from typing import Generator

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from seleniumbase import Driver
from seleniumbase.core.sb_driver import DriverMethods
from webdriver_manager.chrome import ChromeDriverManager

from config.resources import (HOME_GREEN_CITY_UI,
                              LOCALSTORAGE,
                              IMPLICITLY_WAIT)


@pytest.fixture()
def driver() -> Generator[webdriver.Chrome, None, None]:
    print("generate driver")
    chrome_options = webdriver.ChromeOptions()

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(IMPLICITLY_WAIT)
    driver.maximize_window()
    yield driver

    driver.quit()


@pytest.fixture()
def driver_uc() -> Generator[DriverMethods]:
    driver = Driver(uc=True, headless=False)
    yield driver
    driver.quit()


@pytest.fixture()
def login_driver(driver) -> Generator[webdriver.Chrome, None, None]:
    driver.get(HOME_GREEN_CITY_UI)
    for key, value in LOCALSTORAGE.items():
        if value:
            driver.execute_script(f"window.localStorage.setItem('{key}', '{value}');")
    driver.refresh()
    yield driver
    for key in LOCALSTORAGE.keys():
            driver.execute_script(f"localStorage.removeItem('{key}');")

    driver.quit()