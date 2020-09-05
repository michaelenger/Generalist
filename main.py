"""Main entry point for the script."""

import generalist


if __name__ == '__main__':
    token = generalist.login_user()

    tracks = generalist.get_saved_tracks(token)

    print(tracks)
