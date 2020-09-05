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


@pytest.mark.parametrize('uri, token, query_params, response', [
    ('/me', 'token', None, {'id': 123, 'name': 'UserMan'}),
    ('/artists/321', 'safetyfirst', None, {'id': 123, 'name': '🥶'}),
    ('/tracks', 'yes', {'limit': 0}, {'items': []}),
])
@patch('generalist.spotify.requests')
def test_get(requests_mock, uri, token, query_params, response):
    requests_mock.get.return_value = _mock_response(200, response)

    result = spotify._get(uri, token, query_params)

    assert result == response

    requests_mock.get.assert_called_with(
        f'https://api.spotify.com/v1{uri}',
        headers={'Authorization': f'Bearer {token}'},
        params=query_params)


@pytest.mark.parametrize('uri, token, query_params, error', [
    ('/me', 'token', None, 'Something bad'),
    ('/artists/321', 'safetyfirst', None, 'Not today, satan'),
    ('/tracks', 'yes', {'limit': 0}, 'Cannot find it'),
])
@patch('generalist.spotify.requests')
def test_get_fail(requests_mock, uri, token, query_params, error):
    requests_mock.get.return_value = _mock_response(
        400, {'error_description': error})

    with pytest.raises(Exception) as err:
        spotify._get(uri, token, query_params)

    assert str(err.value) == error

    requests_mock.get.assert_called_with(
        f'https://api.spotify.com/v1{uri}',
        headers={'Authorization': f'Bearer {token}'},
        params=query_params)


@patch('generalist.spotify._get')
def test_get_artists(get_mock):
    artist_data = [{'id': '0qzgOvNnbHiArRuXgkJfFI'}]
    get_mock.return_value = {
        'artists': artist_data
    }

    result = spotify.get_artists('token', ['id123', 'lol', '🩰'])

    assert result == artist_data

    get_mock.assert_called_with('/artists', 'token', {'ids': 'id123,lol,🩰'})


def test_get_login_url():
    result = spotify.get_login_url()
    expected = 'https://accounts.spotify.com/authorize' \
        '?client_id=' + config.SPOTIFY_CLIENT_ID + \
        '&response_type=code' \
        '&scope=user-library-read' \
        '&redirect_uri=http%3A%2F%2Flocalhost%3A1337%2Fauth'

    assert result == expected


@patch('generalist.spotify._get')
def test_get_saved_tracks(get_mock):
    track_data = {
        'href': 'https://api.spotify.com/v1/me/tracks?offset=0&limit=20',
        'items': [
            {'id': '3U7puaLpj9buAdKd9QnuqD', 'name': 'Shameless self promotion'},
            {'id': '2jpDioAB9tlYXMdXDK3BGl', 'name': 'Good Enough For Granddad'}
        ],
        'limit': 20,
        'next': 'https://api.spotify.com/v1/me/tracks?offset=20&limit=20',
        'offset': 0,
        'previous': None,
        'total': 53
    }
    get_mock.return_value = track_data

    result = spotify.get_saved_tracks('token', 10)

    assert result == track_data

    get_mock.assert_called_with(
        '/me/tracks', 'token', {'offset': 10, 'limit': 50})


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
