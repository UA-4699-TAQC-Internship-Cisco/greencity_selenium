from config.resources import EXPECTED_USERNAME


def test_send_message(send_comment_and_get_comment_data):
    """Test the accuracy of the information in the sent message."""
    comment_data = send_comment_and_get_comment_data("some valid text for the test")
    assert comment_data == {"author": EXPECTED_USERNAME, "text": "some valid text for the test"}  # change user
