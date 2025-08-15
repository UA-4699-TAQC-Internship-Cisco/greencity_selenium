import pytest

from pages.eco_news_list_page import EcoNewsListPage


@pytest.mark.eco_news_filter_by_tags
def test_eco_news_filter_by_tags(login_driver):
    page = EcoNewsListPage(login_driver)
    page.go_to_eco_news_page()

    # step_1
    page.click_news_filter()
    assert page.is_tag_in_list("NEWS") == True
    assert page.is_tag_filter_active("NEWS") == True
    page.click_news_filter()

    # step_2
    page.click_events_filter()
    assert page.is_tag_in_list("EVENTS") == True
    assert page.is_tag_filter_active("EVENTS") == True
    page.click_events_filter()

    # step_3
    page.click_education_filter()
    assert page.is_tag_in_list("EDUCATION") == True
    assert page.is_tag_filter_active("EDUCATION") == True
    page.click_education_filter()

    # step_4
    page.click_initiatives_filter()
    assert page.is_tag_in_list("INITIATIVES") == True
    assert page.is_tag_filter_active("INITIATIVES") == True
    page.click_initiatives_filter()

    # step_5
    page.click_ads_filter()
    assert page.is_tag_in_list("ADS") == True
    assert page.is_tag_filter_active("ADS") == True
    page.click_ads_filter()
