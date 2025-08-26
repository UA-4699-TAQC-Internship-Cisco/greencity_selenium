

def test_send_message(send_comment_and_get_comment_data):
    comment_data=send_comment_and_get_comment_data("some valid text for the test")
    assert comment_data == {
            'author': "user from .env",     #change user
            'text': "some valid text for the test"
        }


