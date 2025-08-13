from selenium.webdriver.common.by import By

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
