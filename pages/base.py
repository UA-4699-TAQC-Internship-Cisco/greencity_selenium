from typing import Union

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

try:
    from seleniumbase.core.sb_driver import DriverMethods
except ImportError:
    # Handle case where seleniumbase is not installed
    DriverMethods = None


class Base:
    """Base class providing common WebDriver functionality."""

    def __init__(self, driver: Union[WebDriver, "DriverMethods"]):
        """Initialize with a WebDriver instance.

        Args:
            driver: WebDriver or DriverMethods instance.
        """
        self.driver = driver

    def get_wait(self, explicit_wait: int = 20) -> WebDriverWait:
        """Get a WebDriverWait instance with specified timeout.

        Args:
            explicit_wait: Timeout in seconds for explicit wait.

        Returns:
            WebDriverWait: Configured wait instance.
        """
        return WebDriverWait(self.driver, explicit_wait)
