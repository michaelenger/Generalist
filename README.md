# Generalist

Script for generating playlists based on the genres of your liked songs in Spotify.

## Requirements

* [Python 3.7+](https://www.python.org/)
* A [Spotify](https://www.spotify.com/) account
* A Spotify application API key (see the [developer documentation](https://developer.spotify.com/))


## Usage

Create an application in the [Spotify Developer portal](https://developer.spotify.com/) and make sure that one of the redirect URIs is: `http://localhost:1337/auth`

Install the dependencies:

```shell
pip install -r requirements.txt
```

Create an environment file and fill it with your API credentials:

```shell
cp .env.shadow .env
```

Run the script:

```shell
python main.py
```
