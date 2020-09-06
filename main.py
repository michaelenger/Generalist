"""Main entry point for the script."""

import argparse

import generalist
from generalist import utils


def list_tracks(args: argparse.Namespace):
    """Show a list of the saved tracks."""
    token = generalist.login_user()
    tracks = generalist.get_saved_tracks(token)

    if args.sorted:
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
    tracks_parser.add_argument("--sorted", help="sort list of tracks", action="store_true")
    tracks_parser.set_defaults(handle=list_tracks)

    args = parser.parse_args()
    if not hasattr(args, "handle"):
        args = parser.parse_args(["tracks"])  # default to showing tracks

    args.handle(args)
