from dotenv import load_dotenv
import os

load_dotenv()

USER_EMAIL = os.getenv("USER_EMAIL")
USER_PASSWORD = os.getenv("USER_PASSWORD")
EXPECTED_USERNAME = os.getenv("EXPECTED_USERNAME")

LOCALSTORAGE = {

    "accessToken":os.getenv("LOCALSTORAGE_accessToken"),
    "refreshToken":os.getenv("LOCALSTORAGE_refreshToken"),
    "language":os.getenv("LOCALSTORAGE_language"),
    "name":os.getenv("LOCALSTORAGE_name"),
    "userId":os.getenv("LOCALSTORAGE_userId")
}
IMPLICITLY_WAIT = 10

HOME_GREEN_CITY_UI = "https://www.greencity.cx.ua/#/greenCity"
CONTENT_TEXT = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
EDITED_CONTENT_TEXT = "This is a test message. It's likely being used to check the formatting, content, or functionality of a message before it's sent to a larger audience."
TITLE_TEXT = "What is Lorem Ipsum?"
LINK = "https://www.lipsum.com/"
NEWS_TAG = "NEWS"
NEWS_LINK = "https://www.greencity.cx.ua/#/greenCity/news/10"
NEWS_LINK1 = "https://www.greencity.cx.ua/#/greenCity/news/9"
NEWS_LINK2 = "https://www.greencity.cx.ua/#/greenCity/news/19"
EDITED_CONTENT = "qwertyuiopasdfghj19"
WARNING_MSG1 = "Must be minimum 20 and maximum 63 206 symbols"
WARNING_MSG2 = "Not enough characters. Left: 1"
ECO_NEWS_TITLE_TEXT = "Eco news"

