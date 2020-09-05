"""Script configuration."""

import os

import dotenv


script_dir = os.path.join(os.path.dirname(__file__), os.path.pardir)

# Load environment variables from a .env file if present
dotenv_path = os.path.abspath(os.path.join(script_dir, ".env"))
dotenv.load_dotenv(dotenv_path)


ACCESS_TOKEN_FILE = os.path.abspath(os.path.join(script_dir, ".access_token"))


# Environment variables
SERVER_PORT = int(os.environ.get("SERVER_PORT"))
REDIRECT_URI = f"http://localhost:{SERVER_PORT}/auth"

SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
