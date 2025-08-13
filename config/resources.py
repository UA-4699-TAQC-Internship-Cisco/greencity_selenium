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
TITLE_TEXT = "What is Lorem Ipsum?"
LINK = "https://www.lipsum.com/"
