import pytest



def test_check_news_title_text(get_news_title):
    assert get_news_title == 'What is Lorem Ipsum?'       #change title or link


# def test_send_message(send_comment_and_get_comment_data):
#     comment_data=send_comment_and_get_comment_data("some valid text for the test")
#     assert comment_data == {
#             'author': "user from .env",     #change user
#             'text': "some valid text for the test"
#         }


