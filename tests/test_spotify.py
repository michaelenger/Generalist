"""Tests for the Spotify helper functions."""

from generalist import spotify


def test_get_login_url():
    result = spotify.get_login_url('client')
    expected = 'https://accounts.spotify.com/authorize' \
        '?client_id=client' \
        '&response_type=code' \
        '&scopes=user-library-read' \
        '&redirect_uri=http%3A%2F%2Flocalhost%3A1337'

    assert result == expected
