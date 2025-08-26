import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config.resources import *
from pages.base_page import BasePage


class NewsPage(BasePage):
    EDIT_NEWS = (By.XPATH, "//div[@class='edit-news']")
    EDIT_NEWS_BTN = (By.XPATH, "//button[contains(@class,'primary-global-button') and @disabled]")
    navbar_eco_news = (By.XPATH, '/html/body/app-root/app-main/div/app-header/header/div[2]/div/div/nav/ul/li[1]/a')
    edit_news_button = (By.XPATH, '//*[@id="main-content"]/div/div[1]/div[2]/a/div')
    news_autor = (By.XPATH, '//*[@id="main-content"]/div/div[3]/div[2]/div[3]')
    news_title = (By.XPATH, '//*[@id="main-content"]/div/div[3]/div[1]/div')
    NEWS_TITLE = (By.XPATH, "//div[@class='news-title word-wrap']")
    NEWS_CONTENT = (By.XPATH, "//div[@class='ql-editor']")
    like_news_button = (By.XPATH, '//*[@id="main-content"]/div/div[3]/div[2]/div[4]/img')
    like_news_count = (By.XPATH, '//*[@id="main-content"]/div/div[3]/div[2]/div[4]/span')
    news_content = (By.XPATH, '//*[@id="main-content"]/div/div[3]/div[3]/div[2]/div/div')
    FIRST_NEWS_FROM_INTERESTING = (By.XPATH, '(//div[@class="title-list word-wrap"])[1]')
    LIKE_ICON = (By.XPATH, '//img[@alt="like"]')
    LIKE_COUNT = (By.XPATH, '//span[@class="numerosity_likes"]')
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
        edit_news_btn = self.get_wait(60).until(EC.element_to_be_clickable(self.EDIT_NEWS))
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

    @allure.step("Check 'Eco news' title")
    def check_news_title(self):
        title_element = self.get_wait(60).until(EC.visibility_of_element_located(self.NEWS_TITLE))
        actual_text = title_element.text
        # assert actual_text == TITLE_TEXT
        print(" in def Test title == ", actual_text)
        return actual_text

    @allure.step("Check 'Eco news' content")
    def check_news_content(self):
        title_element = self.get_wait().until(EC.presence_of_element_located(self.NEWS_CONTENT))
        actual_text = title_element.text
        assert actual_text == CONTENT_TEXT

    @allure.step("Click 'Interesting' news")
    def click_interesting_news(self):
        news_tile = self.get_wait().until(EC.element_to_be_clickable(self.FIRST_NEWS_FROM_INTERESTING))
        news_tile.click()

    @allure.step("Get 'Interesting' news title")
    def get_first_news_title(self):
        title_element = self.get_wait().until(EC.presence_of_element_located(self.FIRST_NEWS_FROM_INTERESTING))
        actual_text = title_element.text
        print(actual_text)
        return actual_text

    @allure.step("Compare news titles from main and 'Interesting' sections")
    def compare_news_titles(self):
        main_title = self.get_first_news_title()
        print("first title:", main_title)

        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(self.NEWS_TITLE))

        print(self.driver.current_url)
        interesting_title = self.check_news_title()
        print("second title:", interesting_title)
        assert main_title == interesting_title
        return True

    @allure.step("Count likes number")
    def count_likes_number(self):
        like_count_element = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(self.LIKE_COUNT))
        current_likes = int(like_count_element.text)
        return current_likes

    @allure.step("Click like icon")
    def click_like_icon(self):
        like_icon = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(self.LIKE_ICON))
        like_icon.click()

    @allure.step("Check like added")
    def check_like_added(self, initial_likes):
        current_likes = self.count_likes_number()
        assert current_likes == initial_likes + 1
        return self

    @allure.step("Check like removed")
    def check_like_removed(self, initial_likes):
        current_likes = self.count_likes_number()
        assert current_likes == initial_likes - 1
        return self
