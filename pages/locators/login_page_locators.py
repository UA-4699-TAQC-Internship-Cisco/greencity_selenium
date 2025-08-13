from selenium.webdriver.common.by import By

# Login page locators
EMAIL_INPUT = (By.XPATH, "//input[@id='email']")
PASSWORD_INPUT = (By.XPATH, "//input[@id='password']")
LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
USERNAME_DISPLAY = (By.XPATH, "//li[@class='body-2 user-name']")

GREEN_CITY_BTN = (By.XPATH, "//a[@class='url-name ng-star-inserted'][normalize-space()='Green City']")
ECO_NEWS_BTN = (By.XPATH, "//a[contains(@class,'url-name') and normalize-space()='Eco news']")
