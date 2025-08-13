from selenium.webdriver.common.by import By
from config.resources import*

# Create news page locators
PAGE_TITLE = (By.XPATH, "//h2[@class='title-header' and text()='Create news']")
INPUT_TITLE = \
    (By.XPATH, "//textarea[@formcontrolname='title']")

NEWS_TAG = (By.XPATH, "//span[@class='text' and text()='News']")
EVENTS_TAG = (By.XPATH, "//span[@class='text' and text()='Events']")
EDUCATION_TAG = (By.XPATH, "//span[@class='text' and text()='Education']")
INITIATIVES_TAG = (By.XPATH, "//span[@class='text' and text()='Initiatives']")
ADS_TAG = (By.XPATH, "//span[@class='text' and text()='Ads']")

INPUT_SOURCE = (By.XPATH, "//input[@placeholder='Link to external source']")
#UPLOAD_PICTURE
CONTENT_FIELD = (By.XPATH, "//div[@class='ql-editor ql-blank']")

CANCEL_PICTURE = (By.XPATH, "//button[@class='secondary-global-button s-btn']")
SUBMIT_PICTURE = (By.XPATH, "//button[@class='primary-global-button s-btn']")

PUBLISH_BUTTON = (By.XPATH, "//button[@class='primary-global-button']")
PREVIEW_BUTTON = (By.XPATH, "//button[@class='secondary-global-button']")
CANCELL_BUTTON = (By.XPATH, "//button[@class='tertiary-global-button']")

lOADING_MESSAGE = (By.XPATH, "//p[@class='header' and text()='Please wait while loading...']")

TITLE_ON_NEWS = \
     (By.XPATH, f"(//div[@class='title-list word-wrap']/h3[contains(normalize-space(), '{TITLE_TEXT}')])[1]")

TAG_ON_NEWS = \
    (By.XPATH, "(//app-news-list-gallery-view//span[contains(text(), 'News')])[1]")

TEXT_ON_NEWS = \
     (By.XPATH,
      f"(//li[.//h3[contains(normalize-space(), \
      'What is Lorem Ipsum?')]]//p[contains(normalize-space(), \
      '{CONTENT_TEXT}')])[1]")


AUTHOR_ON_NEWS = (By.XPATH, "(//app-news-list-gallery-view//span[contains(text(), 'Marta')])[1]")
