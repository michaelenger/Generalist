"""Generalist."""

from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import threading
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

            file = open(config.ACCESS_TOKEN_FILE, 'w')
            file.write(access_token)
            file.close()

            threading.Thread(target=self.server.shutdown, daemon=True).start() 

        except Exception as e:
            self.wfile.write(bytes('Error! ' + str(e), 'utf-8'))

    def log_message(self, format, *args):
        """Be quiet."""
        return


def login_user():
    """Login the user."""
    url = spotify.get_login_url()

    server = HTTPServer(('localhost', config.SERVER_PORT), AuthServer)

    print('Opening Spotify login page...')
    webbrowser.open(url, new=2)

    server.serve_forever()
