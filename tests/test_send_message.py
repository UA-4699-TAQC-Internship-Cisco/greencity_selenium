from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.news_page import NewsPage



#driver = webdriver.Chrome()

NewsPage().open_news_by_link("https://www.greencity.cx.ua/#/greenCity")
#driver.get('https://www.greencity.cx.ua/#/greenCity')
#elem = driver.find_element(By.XPATH, "/html/body/app-root/app-main/div/app-header/header/div[2]/div/div/nav/ul/li[1]")
#driver.quit()