from selenium.webdriver.common.by import By

CREATE_NEWS = (By.XPATH, "//span[@id='create-button-text']")
#tag buttons
news_tag_button='//*[@id="main-content"]/div/div[2]/div/app-tag-filter/div/div/button[1]/a'
events_tag_button='//*[@id="main-content"]/div/div[2]/div/app-tag-filter/div/div/button[2]/a'
education_tag_button='//*[@id="main-content"]/div/div[2]/div/app-tag-filter/div/div/button[3]/a'
initiatives_tag_button='//*[@id="main-content"]/div/div[2]/div/app-tag-filter/div/div/button[4]/a'
ads_tag_button= '//*[@id="main-content"]/div/div[2]/div/app-tag-filter/div/div/button[5]/a'
#news
first_news_on_eco_news_page='//*[@id="main-content"]/div/div[4]/ul/li[1]/a/app-news-list-gallery-view/div/div/div[2]/div[1]/h3'
first_news_tags_list='//*[@id="main-content"]/div/div[4]/ul/li[1]/a/app-news-list-gallery-view/div/div/div[1]'
second_news_tags_list='//*[@id="main-content"]/div/div[4]/ul/li[2]/a/app-news-list-gallery-view/div/div/div[1]'


