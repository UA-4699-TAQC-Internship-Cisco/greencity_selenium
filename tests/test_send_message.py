from config.resources import EXPECTED_USERNAME


def test_check_news_title_text(get_news_title):
    assert get_news_title == 'OlyaNews3'       #change title or link


def test_send_message(send_comment_and_get_comment_data):
    comment_data=send_comment_and_get_comment_data("some valid text for the test")
    assert comment_data == {
            'author': EXPECTED_USERNAME,     #change user
            'text': "some valid text for the test"
        }


