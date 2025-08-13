from typing import Generator

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from seleniumbase import Driver
from seleniumbase.core.sb_driver import DriverMethods
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver() -> Generator[webdriver.Chrome, None, None]:
    print("generate driver")
    chrome_options = webdriver.ChromeOptions()

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver

    driver.quit()


@pytest.fixture()
def driver_uc() -> Generator[DriverMethods]:
    driver = Driver(uc=True, headless=False)
    yield driver
    driver.quit()
