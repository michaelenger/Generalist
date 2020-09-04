"""Tests for the Spotify helper functions."""

import json
from unittest.mock import patch

import pytest
import requests

from generalist import config
from generalist import spotify


def _mock_response(status_code: int, data: object) -> requests.Response:
    """Make a mock Response object."""
    response = requests.Response()
    response.status_code = status_code
    response._content = json.dumps(data).encode()
    return response


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
    requests_mock.post.return_value = _mock_response(
        200, {'access_token': 'hereiskeyok'})

    result = spotify.request_access_token('letmein')

    assert result == 'hereiskeyok'


@patch('generalist.spotify.requests')
def test_request_access_token_fail(requests_mock):
    requests_mock.post.return_value = _mock_response(
        400, {'error_description': 'no'})

    with pytest.raises(Exception) as err:
        spotify.request_access_token('letmein')

    assert str(err.value) == 'Unable to get access token: no'
