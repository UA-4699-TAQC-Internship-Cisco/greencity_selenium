from selenium.webdriver.common.by import By

EDIT_NEWS = (By. XPATH, "//div[@class='edit-news']")
EDIT_NEWS_BTN = (By. XPATH, "//button[contains(@class,'primary-global-button') and @disabled]")
EDIT_CONTENT = (By. XPATH, "//div[@class='ql-editor']")
WARNING_MESSAGE1 = (By. XPATH, "//p[@class='field-info warning']")
WARNING_MESSAGE2 = (By. XPATH, "//p[@class='quill-counter warning']")
