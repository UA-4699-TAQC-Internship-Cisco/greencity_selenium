from selenium import webdriver
from selenium.webdriver.common.by import By

class NewsPage():

    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_news_by_link(self, link):
        self.driver.get(f'{link}')

    def send_message(self):
        pass

    def right_like(self):
        pass

    def like_post(self):
        pass


