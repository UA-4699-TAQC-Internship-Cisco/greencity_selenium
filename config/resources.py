import os
from typing import Dict, Optional

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# User credentials
USERNAME: Optional[str] = os.getenv("LOCALSTORAGE_name")
USER_EMAIL: Optional[str] = os.getenv("USER_EMAIL")
USER_PASSWORD: Optional[str] = os.getenv("USER_PASSWORD")
EXPECTED_USERNAME: Optional[str] = os.getenv("EXPECTED_USERNAME")

# LocalStorage configuration for authenticated sessions
LOCALSTORAGE: Dict[str, Optional[str]] = {
    "accessToken": os.getenv("LOCALSTORAGE_accessToken"),
    "refreshToken": os.getenv("LOCALSTORAGE_refreshToken"),
    "language": os.getenv("LOCALSTORAGE_language"),
    "name": os.getenv("LOCALSTORAGE_name"),
    "userId": os.getenv("LOCALSTORAGE_userId"),
}

# Browser configuration
IMPLICITLY_WAIT: int = 10

# Application URLs
HOME_GREEN_CITY_UI: str = "https://www.greencity.cx.ua/#/greenCity"

# Test data
CONTENT_TEXT: str = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor "
    "incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud "
    "exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure "
    "dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. "
    "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt "
    "mollit anim id est laborum."
)

EDITED_CONTENT_TEXT: str = (
    "This is a test message. It's likely being used to check the formatting, content, "
    "or functionality of a message before it's sent to a larger audience."
)

TITLE_TEXT: str = "What is Lorem Ipsum?"
LINK: str = "https://www.lipsum.com/"
NEWS_TAG: str = "NEWS"

# Comment
COMMENT_TEXT = "This is a test comment"

# News URLs for testing
NEWS_LINK: str = "https://www.greencity.cx.ua/#/greenCity/news/10"
NEWS_LINK1: str = "https://www.greencity.cx.ua/#/greenCity/news/9"
NEWS_LINK2: str = "https://www.greencity.cx.ua/#/greenCity/news/19"

# Validation messages
EDITED_CONTENT: str = "qwertyuiopasdfghj19"
WARNING_MSG1: str = "Must be minimum 20 and maximum 63 206 symbols"
WARNING_MSG2: str = "Not enough characters. Left: 1"

# Page titles
ECO_NEWS_TITLE_TEXT: str = "Eco news"
