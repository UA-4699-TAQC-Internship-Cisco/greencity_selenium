from dotenv import load_dotenv
import os

load_dotenv()

USER_EMAIL = os.getenv("USER_EMAIL")
USER_PASSWORD = os.getenv("USER_PASSWORD")
EXPECTED_USERNAME = os.getenv("EXPECTED_USERNAME")
DOMAIN = "https://www.greencity.cx.ua/#/ubs"
CONTENT_TEXT = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
TITLE_TEXT = "What is Lorem Ipsum?"
LINK = "https://www.lipsum.com/"
NEWS_TAG = "NEWS"
