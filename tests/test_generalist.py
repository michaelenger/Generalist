"""Test generalist functionality."""

from unittest.mock import patch

import generalist


@patch('generalist.open')
def test_read_access_token(open_mock):
    open_mock().__enter__().readline.return_value = 'sometoken'

    result = generalist._read_access_token()

    assert result == 'sometoken'


@patch('generalist.open')
def test_read_access_token_fail(open_mock):
    open_mock.side_effect = Exception('failol')

    result = generalist._read_access_token()

    assert result is None


@patch('generalist._read_access_token')
@patch('generalist.HTTPServer')
@patch('generalist.webbrowser')
def test_login_user(webbrowser_mock, HTTPServer_mock, _read_access_token_mock):
    _read_access_token_mock.side_effect = [
        None, 'nowitworks']

    result = generalist.login_user()

    assert result == 'nowitworks'

    webbrowser_mock.open.assert_called()
    HTTPServer_mock().serve_forever.assert_called()


@patch('generalist._read_access_token')
@patch('generalist.HTTPServer')
@patch('generalist.webbrowser')
def test_login_user_file_exists(
        webbrowser_mock, HTTPServer_mock, _read_access_token_mock):
    _read_access_token_mock.return_value = 'supersecure'

    result = generalist.login_user()

    assert result == 'supersecure'

    webbrowser_mock.open.assert_not_called()
    HTTPServer_mock().serve_forever.assert_not_called()
