from dotenv import load_dotenv
import os

load_dotenv()

USER_EMAIL = os.getenv("USER_EMAIL")
USER_PASSWORD = os.getenv("USER_PASSWORD")
EXPECTED_USERNAME = os.getenv("EXPECTED_USERNAME")
DOMAIN = "https://www.greencity.cx.ua/#/ubs"
