"""Test generalist functionality."""

from unittest.mock import patch

import generalist


@patch("generalist.open")
def test_read_access_token(open_mock):
    open_mock().__enter__().readline.return_value = "sometoken"

    result = generalist._read_access_token()

    assert result == "sometoken"


@patch("generalist.open")
def test_read_access_token_fail(open_mock):
    open_mock.side_effect = Exception("failol")

    result = generalist._read_access_token()

    assert result is None


@patch("generalist.spotify")
def test_get_saved_tracks(spotify_mock, mock_artists, mock_saved_tracks):
    spotify_mock.get_saved_tracks.side_effect = mock_saved_tracks
    spotify_mock.get_artists.return_value = mock_artists

    result = generalist.get_saved_tracks("token")

    assert result == [
        {
            "id": "0K9v3Jq3mI0phzWbeKAiqc",
            "name": "The Grey",
            "artists": ["Beyond The Barricade"],
            "genres": [],
        },
        {
            "id": "5CJ1xQCFywhEryVUPJup5T",
            "name": "The Boy Who Wouldn't Hoe Corn",
            "artists": ["Alison Krauss & Union Station"],
            "genres": ["bluegrass", "folk", "progressive bluegrass"],
        },
        {
            "id": "0K9v3Jq3mI0phzWbeKAiqc",
            "name": "The Grey",
            "artists": ["Beyond The Barricade"],
            "genres": [],
        },
        {
            "id": "5CJ1xQCFywhEryVUPJup5T",
            "name": "The Boy Who Wouldn't Hoe Corn",
            "artists": ["Alison Krauss & Union Station"],
            "genres": ["bluegrass", "folk", "progressive bluegrass"],
        },
        {
            "id": "0K9v3Jq3mI0phzWbeKAiqc",
            "name": "The Grey",
            "artists": ["Beyond The Barricade"],
            "genres": [],
        },
    ]


@patch("generalist._read_access_token")
@patch("generalist.HTTPServer")
@patch("generalist.spotify")
@patch("generalist.webbrowser")
def test_login_user(
    webbrowser_mock, spotify_mock, HTTPServer_mock, _read_access_token_mock
):
    _read_access_token_mock.side_effect = [None, "nowitworks"]
    spotify_mock.verify_access_token.return_value = False

    result = generalist.login_user()

    assert result == "nowitworks"

    webbrowser_mock.open.assert_called()
    HTTPServer_mock().serve_forever.assert_called()


@patch("generalist._read_access_token")
@patch("generalist.HTTPServer")
@patch("generalist.spotify")
@patch("generalist.webbrowser")
def test_login_user_file_exists(
    webbrowser_mock, spotify_mock, HTTPServer_mock, _read_access_token_mock
):
    _read_access_token_mock.return_value = "supersecure"
    spotify_mock.verify_access_token.return_value = True

    result = generalist.login_user()

    assert result == "supersecure"

    webbrowser_mock.open.assert_not_called()
    HTTPServer_mock().serve_forever.assert_not_called()


@patch("generalist._read_access_token")
@patch("generalist.HTTPServer")
@patch("generalist.spotify")
@patch("generalist.webbrowser")
def test_login_user_not_verified(
    webbrowser_mock, spotify_mock, HTTPServer_mock, _read_access_token_mock
):
    _read_access_token_mock.return_value = "supersecure"
    spotify_mock.verify_access_token.return_value = False

    result = generalist.login_user()

    assert result == "supersecure"

    webbrowser_mock.open.assert_called()
    HTTPServer_mock().serve_forever.assert_called()
