import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base import BasePage


class NewsPage(BasePage):
    EDIT_NEWS = (By.XPATH, "//div[@class='edit-news']")
    EDIT_NEWS_BTN = (By.XPATH, "//button[contains(@class,'primary-global-button') and @disabled]")
    edit_news_button = (By.XPATH, '//*[@id="main-content"]/div/div[1]/div[2]/a/div')
    news_autor = (By.XPATH, '//*[@id="main-content"]/div/div[3]/div[2]/div[3]')
    news_title = (By.XPATH, '//*[@id="main-content"]/div/div[3]/div[1]/div')
    like_news_button = (By.XPATH, '//*[@id="main-content"]/div/div[3]/div[2]/div[4]/img')
    like_news_count = (By.XPATH, '//*[@id="main-content"]/div/div[3]/div[2]/div[4]/span')
    news_content = (By.XPATH, '//*[@id="main-content"]/div/div[3]/div[3]/div[2]/div/div')
    first_from_interesting_news = (By.XPATH,
                                   '//*[@id="main-content"]/div/app-eco-news-widget/div/div/div/div[1]/app-news-list-gallery-view/div')
    comment_textarea = (By.XPATH,
                        '//*[@id="main-content"]/div/app-comments-container/app-add-comment/form/div[2]/app-comment-textarea/div/div')
    comment_button = (By.XPATH, '//*[@id="main-content"]/div/app-comments-container/app-add-comment/form/div[2]/button')
    first_comment_text = (By.XPATH,
                          '//*[@id="main-content"]/div/app-comments-container/app-comments-list/div[1]/div[3]/div[1]')
    first_comment_author = (By.XPATH,
                            '//*[@id="main-content"]/div/app-comments-container/app-comments-list/div[1]/div[2]/span')

    @allure.step("Open page by link")
    def open_page_by_link(self, link):
        self.driver.get(f'{link}')
        self.driver.implicitly_wait(10)

    @allure.step("Click 'Edit news' button")
    def edit_news_btn(self):
        edit_news_btn = self.get_wait().until(EC.element_to_be_clickable(self.EDIT_NEWS))
        edit_news_btn.click()

    @allure.step("Message sent successfully")
    def send_message(self, message):
        self.driver.implicitly_wait(10)
        comment_textarea_fild = self.driver.find_element(*self.comment_textarea)
        comment_textarea_fild.clear()
        comment_textarea_fild.send_keys(message)
        button = self.driver.find_element(*self.comment_button)
        button.click()

    def right_like(self):
        pass

    def like_post(self):
        pass

    @allure.step("Open a first news item in the news list")
    def go_to_first_news(self):
        eco_news = self.driver.find_element(*self.navbar_eco_news)
        eco_news.click()
        self.driver.implicitly_wait(10)
        first_news = self.driver.find_element(*self.first_news_on_eco_news_page)
        first_news.click()
        self.driver.implicitly_wait(10)

    @allure.step("Get first comment data")
    def get_first_comment_data(self):
        data = {'author': self.driver.find_element(self.first_comment_author).text,
                'text': self.driver.find_element(*self.first_comment_text).text}
        return data

    @allure.step("Get news title")
    def get_news_title(self):
        return self.driver.find_element(*self.news_title).text
