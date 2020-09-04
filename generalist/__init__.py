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
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        query = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)

        if 'error' in query:
            self.wfile.write(bytes(
                'Error! Got error: ' + query['error'][0], 'utf-8'))
            return

        if 'code' not in query:
            self.wfile.write(b'Error! Missing code query parameter')
            return

        try:
            code = query['code'][0]
            access_token = spotify.request_access_token(code)

            self.wfile.write(b'You can go back to the CLI script now.')

            print('ACCESS TOKEN', access_token)

            with open(config.ACCESS_TOKEN_FILE, 'w') as file:
                file.write(access_token)

            threading.Thread(target=self.server.shutdown, daemon=True).start() 

        except Exception as e:
            self.wfile.write(bytes('Error! ' + str(e), 'utf-8'))

    def log_message(self, format, *args):
        """Be quiet."""
        return


def _read_access_token() -> Optional[str]:
    """Read the access token from the file."""
    try:
        with open(config.ACCESS_TOKEN_FILE, 'r') as file:
            access_token = file.readline()
        return access_token
    except Exception:
        return None


def login_user() -> Optional[str]:
    """Login the user, if need be, returning the access token."""
    access_token = _read_access_token()
    if access_token is not None:
        return access_token

    url = spotify.get_login_url()

    server = HTTPServer(('localhost', config.SERVER_PORT), AuthServer)

    print('Opening Spotify login page...')
    webbrowser.open(url, new=2)

    server.serve_forever()

    return _read_access_token()  # assumes it all works
