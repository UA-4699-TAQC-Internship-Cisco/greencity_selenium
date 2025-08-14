import pytest
from pages.eco_news_page import EcoNews

def test_eco_news_filter_by_tags(driver):
    page = EcoNews(driver)
    page.go_to_eco_news_page()
    #step_1
    page.click_news_filter()
    assert page.is_tag_in_list("NEWS") == True

    #step_2
    page.click_events_filter()
    assert page.is_tag_in_list("EVENTS") == True

    #step_3
    page.click_education_filter()
    assert page.is_tag_in_list("EDUCATION") == True

    #step_4
    page.click_initiatives_filter()
    assert page.is_tag_in_list("INITIATIVES") == True

    #step_5
    page.click_ads_filter()
    assert page.is_tag_in_list("ADS") == True
