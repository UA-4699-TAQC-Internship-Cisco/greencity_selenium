from config.resources import EXPECTED_USERNAME
from pages.eco_news_list_page import EcoNewsListPage


def test_check_preview_page_button(login_driver):
    """
    Test.

    Check the accuracy of the information in the sent message.
    """
    news_title = "This is a test news title"
    news_link = "https://www.greencity.cx.ua/#/greenCity"
    body_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt \
                ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris \
                nisi ut aliquip ex ea commodo consequat."""

    preview_page = (
        EcoNewsListPage(login_driver)
        .get_header()
        .click_eco_news_button()
        .click_create_news_button()
        .enter_title(news_title)
        .press_tag("News")
        .press_tag("Education")
        .enter_link(news_link)
        .enter_body_text(body_text)
        .click_preview_button()
    )

    title = preview_page.get_title()
    tags = preview_page.get_tags()
    author = preview_page.get_author()
    body = preview_page.get_body_text()
    link = preview_page.get_link()

    assert preview_page.is_create_news_title_present()
    assert title == news_title
    assert f"by {EXPECTED_USERNAME}" == author
    assert body == body_text
    assert link == news_link
    assert "News" in tags
    assert "Education" in tags
