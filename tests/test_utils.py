"""Tests for the utility functions."""

import pytest

from generalist import utils


@pytest.mark.parametrize(
    "track_a, track_b, expected",
    [
        ({"artists": ["A"], "name": "First"}, {"artists": ["A"], "name": "Second"}, -1),
        ({"artists": ["A"], "name": "First"}, {"artists": ["A"], "name": "First"}, 0),
        ({"artists": ["A"], "name": "Second"}, {"artists": ["A"], "name": "First"}, 1),
        ({"artists": ["A"], "name": "Same"}, {"artists": ["B"], "name": "Same"}, -1),
        ({"artists": ["A"], "name": "Same"}, {"artists": ["A"], "name": "Same"}, 0),
        ({"artists": ["B"], "name": "Same"}, {"artists": ["A"], "name": "Same"}, 1),
        (
            {"artists": ["A", "B"], "name": "Same"},
            {"artists": ["B", "A"], "name": "Same"},
            -1,
        ),
        (
            {"artists": ["A", "B"], "name": "Same"},
            {"artists": ["A", "B"], "name": "Same"},
            0,
        ),
        (
            {"artists": ["B", "A"], "name": "Same"},
            {"artists": ["A", "B"], "name": "Same"},
            1,
        ),
    ],
)
def test_compare_track(track_a, track_b, expected):
    result = utils._compare_track(track_a, track_b)
    assert result == expected


def test_sort_track_list(mock_tracks, mock_tracks_sorted):
    result = utils.sort_track_list(mock_tracks)

    assert result == mock_tracks_sorted
