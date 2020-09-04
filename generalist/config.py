"""Script configuration."""

import os

import dotenv

# Load environment variables from a .env file if present
dotenv_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), os.path.pardir, '.env'))
dotenv.load_dotenv(dotenv_path)


# Environment variables
SERVER_PORT = os.environ.get('SERVER_PORT')
REDIRECT_URI = 'http://localhost:' + SERVER_PORT
