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


@patch('generalist.spotify.requests')
def test_get_artist(requests_mock, artist_btb):
    requests_mock.get.return_value = _mock_response(200, artist_btb)

    result = spotify.get_artist('token', 'id123')

    assert result == artist_btb

    requests_mock.get.assert_called_with(
        'https://api.spotify.com/v1/artists/id123',
        headers={'Authorization': 'Bearer token'})


@patch('generalist.spotify.requests')
def test_get_artist_fail(requests_mock):
    requests_mock.get.return_value = _mock_response(
        500, {'error_description': 'Go away now.'})

    with pytest.raises(Exception) as err:
        spotify.get_artist('token', 'id123')

    assert str(err.value) == 'Go away now.'


def test_get_login_url():
    result = spotify.get_login_url()
    expected = 'https://accounts.spotify.com/authorize' \
        '?client_id=' + config.SPOTIFY_CLIENT_ID + \
        '&response_type=code' \
        '&scope=user-library-read' \
        '&redirect_uri=http%3A%2F%2Flocalhost%3A1337%2Fauth'

    assert result == expected


@patch('generalist.spotify.requests')
def test_get_saved_tracks(requests_mock):
    track_data = [
        {'id': '3U7puaLpj9buAdKd9QnuqD', 'name': 'Shameless self promotion'},
        {'id': '2jpDioAB9tlYXMdXDK3BGl', 'name': 'Good Enough For Granddad'}
    ]
    response_data = {
        'href': 'https://api.spotify.com/v1/me/tracks?offset=0&limit=20',
        'items': track_data,
        'limit': 20,
        'next': 'https://api.spotify.com/v1/me/tracks?offset=20&limit=20',
        'offset': 0,
        'previous': None,
        'total': 53
    }

    requests_mock.get.return_value = _mock_response(200, response_data)

    result = spotify.get_saved_tracks('token')

    assert result == track_data

    requests_mock.get.assert_called_with(
        'https://api.spotify.com/v1/me/tracks',
        headers={'Authorization': 'Bearer token'})


@patch('generalist.spotify.requests')
def test_get_saved_tracks_fail(requests_mock):
    requests_mock.get.return_value = _mock_response(
        500, {'error_description': 'Something bad'})

    with pytest.raises(Exception) as err:
        spotify.get_saved_tracks('token')

    assert str(err.value) == 'Something bad'


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
