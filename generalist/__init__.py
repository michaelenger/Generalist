"""Generalist functionality."""

from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import threading
from typing import Optional
import webbrowser

from generalist import config
from generalist import spotify


class AuthServer(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests."""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        query = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)

        if "error" in query:
            self.wfile.write(bytes("Error! Got error: " + query["error"][0], "utf-8"))
            return

        if "code" not in query:
            self.wfile.write(b"Error! Missing code query parameter")
            return

        try:
            code = query["code"][0]
            access_token = spotify.request_access_token(code)

            self.wfile.write(b"You can go back to the CLI script now.")

            with open(config.ACCESS_TOKEN_FILE, "w") as file:
                file.write(access_token)

            threading.Thread(target=self.server.shutdown, daemon=True).start()

        except Exception as e:
            self.wfile.write(bytes("Error! " + str(e), "utf-8"))

    def log_message(self, format, *args):
        """Be quiet."""
        return


def _read_access_token() -> Optional[str]:
    """Read the access token from the file."""
    try:
        with open(config.ACCESS_TOKEN_FILE, "r") as file:
            access_token = file.readline()
        return access_token
    except Exception:
        return None


def get_saved_tracks(access_token: str):
    """Get a list of all the user's saved tracks with their genres."""
    tracks = []
    artist_ids = set()
    total = 0
    offset = 0

    while True:
        response = spotify.get_saved_tracks(access_token, offset)
        total = response["total"]
        items = response["items"]

        for item in items:
            track = item["track"]
            track_artists = {
                artist["id"]: artist["name"] for artist in track["artists"]
            }
            tracks.append(
                {
                    "id": track["id"],
                    "name": track["name"],
                    "artists": track_artists,
                    "genres": [],
                }
            )

            artist_ids.update(track_artists.keys())

        offset = offset + len(items)

        if len(tracks) >= total:
            break

    artist_ids = list(artist_ids)
    artist_genres = {}
    bunch_amount = 50  # the API supports max 50 artists per request

    for i in range(0, len(artist_ids), bunch_amount):
        artists = spotify.get_artists(access_token, artist_ids[i : i + bunch_amount])
        artist_genres = {
            **artist_genres,
            **{artist["id"]: artist["genres"] for artist in artists},
        }

    for track in tracks:
        genres = set()
        for artist_id in track["artists"]:
            genres.update(artist_genres[artist_id])
        track["genres"] = sorted(genres)
        track["artists"] = list(track["artists"].values())

    return tracks


def login_user() -> Optional[str]:
    """Login the user, if need be, returning the access token."""
    access_token = _read_access_token()
    if access_token and spotify.verify_access_token(access_token):
        return access_token

    url = spotify.get_login_url()

    server = HTTPServer(("localhost", config.SERVER_PORT), AuthServer)

    print("Opening Spotify login page...")
    webbrowser.open(url, new=2)

    server.serve_forever()

    return _read_access_token()  # assumes it all works
