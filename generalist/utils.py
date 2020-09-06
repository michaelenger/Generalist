"""Utilities."""

import functools


def _compare_track(track_a: dict, track_b: dict) -> int:
    """Compare two tracks for sorting them alphabetically."""
    artists_a = (",".join(track_a["artists"])).lower()
    artists_b = (",".join(track_b["artists"])).lower()

    if artists_a == artists_b:
        name_a = track_a["name"].lower()
        name_b = track_b["name"].lower()
        if name_a < name_b:
            return -1
        elif name_a > name_b:
            return 1
        else:
            return 0

    if artists_a < artists_b:
        return -1
    elif artists_a > artists_b:
        return 1

    return 0


def sort_track_list(tracks: list) -> list:
    """Sort a list of tracks."""
    return sorted(tracks, key=functools.cmp_to_key(_compare_track))
