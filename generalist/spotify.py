"""Functions for communicating with the Spotify API."""

import urllib.parse

from generalist.config import REDIRECT_URI


def get_login_url(client_id: str) -> str:
    """Get the login URL."""
    base_url = 'https://accounts.spotify.com/authorize?'
    query_params = {
        'client_id': client_id,
        'response_type': 'code',
        'scopes': 'user-library-read',
        'redirect_uri': REDIRECT_URI
    }

    return base_url + urllib.parse.urlencode(query_params)
