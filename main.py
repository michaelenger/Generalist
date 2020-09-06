"""Main entry point for the script."""

import argparse

import generalist
from generalist import utils


def list_artists(args: argparse.Namespace):
    """Show a list of the artists from the saved tracks."""
    token = generalist.login_user()
    tracks = generalist.get_saved_tracks(token)
    artists = {}

    for track in tracks:
        for artist in track["artists"]:
            if artist not in artists:
                artists[artist] = 0
            artists[artist] = artists[artist] + 1

    artists = dict(sorted(artists.items(), key=lambda item: item[0]))
    for artist, amount in artists.items():
        print(f"{artist} ({amount})")


def list_genres(args: argparse.Namespace):
    token = generalist.login_user()
    tracks = generalist.get_saved_tracks(token)
    genres = {}

    for track in tracks:
        for genre in track["genres"]:
            if genre not in genres:
                genres[genre] = 0
            genres[genre] = genres[genre] + 1

    if args.alpha:
        genres = dict(sorted(genres.items(), key=lambda item: item[0]))
    else:
        genres = dict(sorted(genres.items(), key=lambda item: item[1], reverse=True))

    for genre, amount in genres.items():
        print(f"{genre} ({amount})")


def list_tracks(args: argparse.Namespace):
    """Show a list of the saved tracks."""
    token = generalist.login_user()
    tracks = generalist.get_saved_tracks(token)

    if args.alpha:
        tracks = utils.sort_track_list(tracks)

    for track in tracks:
        print("{artists} - {track} ({genres})".format(
            artists=", ".join(track["artists"]),
            track=track["name"],
            genres=", ".join(track["genres"]),
        ))


def list_genre_tracks(args: argparse.Namespace):
    """List all the tracks in a genre."""
    token = generalist.login_user()
    tracks = generalist.get_saved_tracks(token)

    tracks = list(filter(lambda x: args.genre in x["genres"], tracks))

    if args.alpha:
        tracks = utils.sort_track_list(tracks)

    for track in tracks:
        print("{artists} - {track} ({genres})".format(
            artists=", ".join(track["artists"]),
            track=track["name"],
            genres=", ".join(track["genres"]),
        ))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(
        title="subcommands",
        description="valid subcommands",
        metavar="command")

    tracks_parser = subparsers.add_parser("tracks", help="list all saved tracks (default command)")
    tracks_parser.add_argument("-a, --alpha", dest="alpha", help="sort list of tracks alphabetical", action="store_true")
    tracks_parser.set_defaults(handle=list_tracks)

    artists_parser = subparsers.add_parser("artists", help="list artists from the saved tracks")
    artists_parser.set_defaults(handle=list_artists)

    genres_parser = subparsers.add_parser("genres", help="list genres from the saved tracks")
    genres_parser.add_argument("-a, --alpha", dest="alpha", help="sort list of genres alphabetically", action="store_true")
    genres_parser.set_defaults(handle=list_genres)

    list_parser = subparsers.add_parser("list", help="list the tracks in a genre")
    list_parser.add_argument("genre", help="name of the genre")
    list_parser.add_argument("-a, --alpha", dest="alpha", help="sort list of tracks alphabetically", action="store_true")
    list_parser.set_defaults(handle=list_genre_tracks)

    args = parser.parse_args()
    if not hasattr(args, "handle"):
        args = parser.parse_args(["tracks"])  # default to showing tracks

    args.handle(args)
