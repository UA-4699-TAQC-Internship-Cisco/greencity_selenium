from typing import Optional, Union

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

try:
    from seleniumbase.core.sb_driver import DriverMethods
except ImportError:
    DriverMethods = None

from pages.base import Base


class BaseComponent(Base):
    """Base class for page components with optional WebElement context."""

    def __init__(self, driver: Union[WebDriver, "DriverMethods"], element: Optional[WebElement] = None):
        """Initialize component with driver and optional element context.

        Args:
            driver: WebDriver or DriverMethods instance.
            element: Optional WebElement for component context.
        """
        super().__init__(driver)
        self.element = element
