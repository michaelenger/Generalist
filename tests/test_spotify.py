"""Tests for the Spotify helper functions."""

import json
from unittest.mock import patch

import pytest
import requests

from generalist import config
from generalist import spotify


def test_get_login_url():
    result = spotify.get_login_url()
    expected = 'https://accounts.spotify.com/authorize' \
        '?client_id=' + config.SPOTIFY_CLIENT_ID + \
        '&response_type=code' \
        '&scope=user-library-read' \
        '&redirect_uri=http%3A%2F%2Flocalhost%3A1337%2Fauth'

    assert result == expected


@patch('generalist.spotify.requests')
def test_request_access_token(requests_mock):
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = json.dumps(
        {'access_token': 'hereiskeyok'}).encode()

    requests_mock.post.return_value = mock_response

    result = spotify.request_access_token('letmein')

    assert result == 'hereiskeyok'


@patch('generalist.spotify.requests')
def test_request_access_token_fail(requests_mock):
    mock_response = requests.Response()
    mock_response.status_code = 400
    mock_response._content = json.dumps(
        {'error_description': 'no'}).encode()

    requests_mock.post.return_value = mock_response

    with pytest.raises(Exception) as err:
        spotify.request_access_token('letmein')

    assert str(err.value) == 'Unable to get access token: no'
