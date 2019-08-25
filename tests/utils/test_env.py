from unittest.mock import patch

from utils.env import env


@patch('utils.env.os')
def test_os_environ(mock_os):
    expected_value = 'environment_value'

    mock_os.environ.__contains__.return_value = True  # patch in statement
    mock_os.environ.__getitem__.return_value = expected_value

    os_variable = env('a_key')

    assert expected_value == os_variable
    mock_os.environ.__getitem__.assert_called_with('a_key')


def test_os_environ_key_missing():
    expected_value = None
    os_variable = env('a_key')

    assert expected_value == os_variable


def test_os_environ_key_missing_with_default():
    expected_value = 'a_default'
    os_variable = env('a_key', default=expected_value)

    assert expected_value == os_variable
