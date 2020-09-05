"""Functions for communicating with the Spotify API."""

from base64 import b64encode
from typing import List
from typing import Optional
import urllib.parse

import requests

from generalist import config


def _get(
        uri: str, access_token: str,
        query_params: Optional[dict] = None) -> dict:
    """Send a GET request to the Spotify API."""
    url = f'https://api.spotify.com/v1{uri}'
    response = requests.get(
        url,
        params=query_params,
        headers={'Authorization': f'Bearer {access_token}'})

    data = response.json()
    if response.status_code != 200:
        raise Exception(data['error_description'])

    return data


def get_artists(access_token: str, artist_ids: List[str]) -> list:
    """Get a paginated list of the user's saved tracks."""
    return _get(f'/artists', access_token, {'ids': ','.join(artist_ids)})


def get_login_url() -> str:
    """Get the login URL."""
    base_url = 'https://accounts.spotify.com/authorize?'
    query_params = {
        'client_id': config.SPOTIFY_CLIENT_ID,
        'response_type': 'code',
        'scope': 'user-library-read',
        'redirect_uri': config.REDIRECT_URI
    }

    return base_url + urllib.parse.urlencode(query_params)


def get_saved_tracks(
        access_token: str, offset: int = 0, limit: int = 50) -> list:
    """Get a paginated list of the user's saved tracks."""
    return _get('/me/tracks', access_token, {'offset': offset, 'limit': limit})


def request_access_token(code: str) -> str:
    """Request an access token based on an authorization code."""
    url = 'https://accounts.spotify.com/api/token'
    payload = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': config.REDIRECT_URI
    }
    auth = b64encode(bytes(
        f'{config.SPOTIFY_CLIENT_ID}:{config.SPOTIFY_CLIENT_SECRET}', 'utf-8'))

    response = requests.post(
        url, data=payload, headers={'Authorization': b'Basic ' + auth})

    data = response.json()

    if response.status_code != 200:
        error = data['error_description']
        raise Exception(f'Unable to get access token: {error}')

    return data['access_token']
