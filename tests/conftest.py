"""Test config."""

import pytest


EXAMPLE_ARTISTS = [
    {
        "external_urls": {
            "spotify": "https://open.spotify.com/artist/0OTnx2X2FDXeewcm72lavT"
        },
        "followers": {"href": None, "total": 129276},
        "genres": ["bluegrass", "folk", "progressive bluegrass"],
        "href": "https://api.spotify.com/v1/artists/0OTnx2X2FDXeewcm72lavT",
        "id": "0OTnx2X2FDXeewcm72lavT",
        "images": [
            {
                "height": 750,
                "url": "https://i.scdn.co/image/6a03e3a6d54734c074359147022bd62b01490c06",
                "width": 1000,
            },
            {
                "height": 480,
                "url": "https://i.scdn.co/image/742c79f195dd42ab7eb44ccdb57b968d1b401326",
                "width": 640,
            },
            {
                "height": 150,
                "url": "https://i.scdn.co/image/15c821ed41c2101e495608474cc888bdbe64c936",
                "width": 200,
            },
            {
                "height": 48,
                "url": "https://i.scdn.co/image/1a01ecd672999e8d42af00176e87de4494b9849f",
                "width": 64,
            },
        ],
        "name": "Alison Krauss & Union Station",
        "popularity": 57,
        "type": "artist",
        "uri": "spotify:artist:0OTnx2X2FDXeewcm72lavT",
    },
    {
        "external_urls": {
            "spotify": "https://open.spotify.com/artist/0qzgOvNnbHiArRuXgkJfFI"
        },
        "followers": {"href": None, "total": 92},
        "genres": [],
        "href": "https://api.spotify.com/v1/artists/0qzgOvNnbHiArRuXgkJfFI",
        "id": "0qzgOvNnbHiArRuXgkJfFI",
        "images": [
            {
                "height": 640,
                "url": "https://i.scdn.co/image/d208d8bcdb0ac75f3a7a3638b9f478c3d2f720fa",
                "width": 640,
            },
            {
                "height": 320,
                "url": "https://i.scdn.co/image/da40951a12bb4cb8d60184f2979aabde25de7151",
                "width": 320,
            },
            {
                "height": 160,
                "url": "https://i.scdn.co/image/c0784f7f00e470ef95032684c38102c755b65d78",
                "width": 160,
            },
        ],
        "name": "Beyond The Barricade",
        "popularity": 3,
        "type": "artist",
        "uri": "spotify:artist:0qzgOvNnbHiArRuXgkJfFI",
    },
]

EXAMPLE_SAVED_TRACKS_ONE = {
    "href": "https://api.spotify.com/v1/me/tracks?offset=0&limit=3",
    "items": [
        {
            "added_at": "2020-09-04T16:43:19Z",
            "track": {
                "album": {
                    "album_type": "single",
                    "artists": [
                        {
                            "external_urls": {
                                "spotify": "https://open.spotify.com/artist/0qzgOvNnbHiArRuXgkJfFI"
                            },
                            "href": "https://api.spotify.com/v1/artists/0qzgOvNnbHiArRuXgkJfFI",
                            "id": "0qzgOvNnbHiArRuXgkJfFI",
                            "name": "Beyond The Barricade",
                            "type": "artist",
                            "uri": "spotify:artist:0qzgOvNnbHiArRuXgkJfFI",
                        }
                    ],
                    "available_markets": ["..."],
                    "external_urls": {
                        "spotify": "https://open.spotify.com/album/0STdARrArJi55I4zbeSbx6"
                    },
                    "href": "https://api.spotify.com/v1/albums/0STdARrArJi55I4zbeSbx6",
                    "id": "0STdARrArJi55I4zbeSbx6",
                    "images": [
                        {
                            "height": 640,
                            "url": "https://i.scdn.co/image/ab67616d0000b2734fbf0642c674ea17daba8a7a",
                            "width": 640,
                        },
                        {
                            "height": 300,
                            "url": "https://i.scdn.co/image/ab67616d00001e024fbf0642c674ea17daba8a7a",
                            "width": 300,
                        },
                        {
                            "height": 64,
                            "url": "https://i.scdn.co/image/ab67616d000048514fbf0642c674ea17daba8a7a",
                            "width": 64,
                        },
                    ],
                    "name": "The Grey",
                    "release_date": "2018-05-03",
                    "release_date_precision": "day",
                    "total_tracks": 5,
                    "type": "album",
                    "uri": "spotify:album:0STdARrArJi55I4zbeSbx6",
                },
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/0qzgOvNnbHiArRuXgkJfFI"
                        },
                        "href": "https://api.spotify.com/v1/artists/0qzgOvNnbHiArRuXgkJfFI",
                        "id": "0qzgOvNnbHiArRuXgkJfFI",
                        "name": "Beyond The Barricade",
                        "type": "artist",
                        "uri": "spotify:artist:0qzgOvNnbHiArRuXgkJfFI",
                    }
                ],
                "available_markets": ["..."],
                "disc_number": 1,
                "duration_ms": 388906,
                "explicit": False,
                "external_ids": {"isrc": "NOJKW1801020"},
                "external_urls": {
                    "spotify": "https://open.spotify.com/track/0K9v3Jq3mI0phzWbeKAiqc"
                },
                "href": "https://api.spotify.com/v1/tracks/0K9v3Jq3mI0phzWbeKAiqc",
                "id": "0K9v3Jq3mI0phzWbeKAiqc",
                "is_local": False,
                "name": "The Grey",
                "popularity": 3,
                "preview_url": "https://p.scdn.co/mp3-preview/f7bf29379d5cd635c437cccabb05c6d0f46a3c39?cid=774b29d4f13844c495f206cafdad9c86",
                "track_number": 2,
                "type": "track",
                "uri": "spotify:track:0K9v3Jq3mI0phzWbeKAiqc",
            },
        },
        {
            "added_at": "2020-09-04T16:43:12Z",
            "track": {
                "album": {
                    "album_type": "album",
                    "artists": [
                        {
                            "external_urls": {
                                "spotify": "https://open.spotify.com/artist/0OTnx2X2FDXeewcm72lavT"
                            },
                            "href": "https://api.spotify.com/v1/artists/0OTnx2X2FDXeewcm72lavT",
                            "id": "0OTnx2X2FDXeewcm72lavT",
                            "name": "Alison Krauss & Union Station",
                            "type": "artist",
                            "uri": "spotify:artist:0OTnx2X2FDXeewcm72lavT",
                        }
                    ],
                    "available_markets": ["..."],
                    "external_urls": {
                        "spotify": "https://open.spotify.com/album/6FfrJoeF2HYdMsMLChPVVM"
                    },
                    "href": "https://api.spotify.com/v1/albums/6FfrJoeF2HYdMsMLChPVVM",
                    "id": "6FfrJoeF2HYdMsMLChPVVM",
                    "images": [
                        {
                            "height": 640,
                            "url": "https://i.scdn.co/image/ab67616d0000b2735ba239901f0f0ff80937460f",
                            "width": 640,
                        },
                        {
                            "height": 300,
                            "url": "https://i.scdn.co/image/ab67616d00001e025ba239901f0f0ff80937460f",
                            "width": 300,
                        },
                        {
                            "height": 64,
                            "url": "https://i.scdn.co/image/ab67616d000048515ba239901f0f0ff80937460f",
                            "width": 64,
                        },
                    ],
                    "name": "New Favorite",
                    "release_date": "2001-08-14",
                    "release_date_precision": "day",
                    "total_tracks": 13,
                    "type": "album",
                    "uri": "spotify:album:6FfrJoeF2HYdMsMLChPVVM",
                },
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/0OTnx2X2FDXeewcm72lavT"
                        },
                        "href": "https://api.spotify.com/v1/artists/0OTnx2X2FDXeewcm72lavT",
                        "id": "0OTnx2X2FDXeewcm72lavT",
                        "name": "Alison Krauss & Union Station",
                        "type": "artist",
                        "uri": "spotify:artist:0OTnx2X2FDXeewcm72lavT",
                    }
                ],
                "available_markets": ["..."],
                "disc_number": 1,
                "duration_ms": 280706,
                "explicit": False,
                "external_ids": {"isrc": "USRO20149502"},
                "external_urls": {
                    "spotify": "https://open.spotify.com/track/5CJ1xQCFywhEryVUPJup5T"
                },
                "href": "https://api.spotify.com/v1/tracks/5CJ1xQCFywhEryVUPJup5T",
                "id": "5CJ1xQCFywhEryVUPJup5T",
                "is_local": False,
                "name": "The Boy Who Wouldn't Hoe Corn",
                "popularity": 43,
                "preview_url": "https://p.scdn.co/mp3-preview/ed7ba16c1f6474cfac1ad26d19eb7c47b7392b38?cid=774b29d4f13844c495f206cafdad9c86",
                "track_number": 2,
                "type": "track",
                "uri": "spotify:track:5CJ1xQCFywhEryVUPJup5T",
            },
        },
    ],
    "limit": 2,
    "next": "https://api.spotify.com/v1/me/tracks?offset=3&limit=3",
    "offset": 0,
    "previous": None,
    "total": 5,
}

EXAMPLE_SAVED_TRACKS_TWO = {
    "href": "https://api.spotify.com/v1/me/tracks?offset=0&limit=3",
    "items": [
        {
            "added_at": "2020-09-04T16:43:19Z",
            "track": {
                "album": {
                    "album_type": "single",
                    "artists": [
                        {
                            "external_urls": {
                                "spotify": "https://open.spotify.com/artist/0qzgOvNnbHiArRuXgkJfFI"
                            },
                            "href": "https://api.spotify.com/v1/artists/0qzgOvNnbHiArRuXgkJfFI",
                            "id": "0qzgOvNnbHiArRuXgkJfFI",
                            "name": "Beyond The Barricade",
                            "type": "artist",
                            "uri": "spotify:artist:0qzgOvNnbHiArRuXgkJfFI",
                        }
                    ],
                    "available_markets": ["..."],
                    "external_urls": {
                        "spotify": "https://open.spotify.com/album/0STdARrArJi55I4zbeSbx6"
                    },
                    "href": "https://api.spotify.com/v1/albums/0STdARrArJi55I4zbeSbx6",
                    "id": "0STdARrArJi55I4zbeSbx6",
                    "images": [
                        {
                            "height": 640,
                            "url": "https://i.scdn.co/image/ab67616d0000b2734fbf0642c674ea17daba8a7a",
                            "width": 640,
                        },
                        {
                            "height": 300,
                            "url": "https://i.scdn.co/image/ab67616d00001e024fbf0642c674ea17daba8a7a",
                            "width": 300,
                        },
                        {
                            "height": 64,
                            "url": "https://i.scdn.co/image/ab67616d000048514fbf0642c674ea17daba8a7a",
                            "width": 64,
                        },
                    ],
                    "name": "The Grey",
                    "release_date": "2018-05-03",
                    "release_date_precision": "day",
                    "total_tracks": 5,
                    "type": "album",
                    "uri": "spotify:album:0STdARrArJi55I4zbeSbx6",
                },
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/0qzgOvNnbHiArRuXgkJfFI"
                        },
                        "href": "https://api.spotify.com/v1/artists/0qzgOvNnbHiArRuXgkJfFI",
                        "id": "0qzgOvNnbHiArRuXgkJfFI",
                        "name": "Beyond The Barricade",
                        "type": "artist",
                        "uri": "spotify:artist:0qzgOvNnbHiArRuXgkJfFI",
                    }
                ],
                "available_markets": ["..."],
                "disc_number": 1,
                "duration_ms": 388906,
                "explicit": False,
                "external_ids": {"isrc": "NOJKW1801020"},
                "external_urls": {
                    "spotify": "https://open.spotify.com/track/0K9v3Jq3mI0phzWbeKAiqc"
                },
                "href": "https://api.spotify.com/v1/tracks/0K9v3Jq3mI0phzWbeKAiqc",
                "id": "0K9v3Jq3mI0phzWbeKAiqc",
                "is_local": False,
                "name": "The Grey",
                "popularity": 3,
                "preview_url": "https://p.scdn.co/mp3-preview/f7bf29379d5cd635c437cccabb05c6d0f46a3c39?cid=774b29d4f13844c495f206cafdad9c86",
                "track_number": 2,
                "type": "track",
                "uri": "spotify:track:0K9v3Jq3mI0phzWbeKAiqc",
            },
        },
        {
            "added_at": "2020-09-04T16:43:12Z",
            "track": {
                "album": {
                    "album_type": "album",
                    "artists": [
                        {
                            "external_urls": {
                                "spotify": "https://open.spotify.com/artist/0OTnx2X2FDXeewcm72lavT"
                            },
                            "href": "https://api.spotify.com/v1/artists/0OTnx2X2FDXeewcm72lavT",
                            "id": "0OTnx2X2FDXeewcm72lavT",
                            "name": "Alison Krauss & Union Station",
                            "type": "artist",
                            "uri": "spotify:artist:0OTnx2X2FDXeewcm72lavT",
                        }
                    ],
                    "available_markets": ["..."],
                    "external_urls": {
                        "spotify": "https://open.spotify.com/album/6FfrJoeF2HYdMsMLChPVVM"
                    },
                    "href": "https://api.spotify.com/v1/albums/6FfrJoeF2HYdMsMLChPVVM",
                    "id": "6FfrJoeF2HYdMsMLChPVVM",
                    "images": [
                        {
                            "height": 640,
                            "url": "https://i.scdn.co/image/ab67616d0000b2735ba239901f0f0ff80937460f",
                            "width": 640,
                        },
                        {
                            "height": 300,
                            "url": "https://i.scdn.co/image/ab67616d00001e025ba239901f0f0ff80937460f",
                            "width": 300,
                        },
                        {
                            "height": 64,
                            "url": "https://i.scdn.co/image/ab67616d000048515ba239901f0f0ff80937460f",
                            "width": 64,
                        },
                    ],
                    "name": "New Favorite",
                    "release_date": "2001-08-14",
                    "release_date_precision": "day",
                    "total_tracks": 13,
                    "type": "album",
                    "uri": "spotify:album:6FfrJoeF2HYdMsMLChPVVM",
                },
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/0OTnx2X2FDXeewcm72lavT"
                        },
                        "href": "https://api.spotify.com/v1/artists/0OTnx2X2FDXeewcm72lavT",
                        "id": "0OTnx2X2FDXeewcm72lavT",
                        "name": "Alison Krauss & Union Station",
                        "type": "artist",
                        "uri": "spotify:artist:0OTnx2X2FDXeewcm72lavT",
                    }
                ],
                "available_markets": ["..."],
                "disc_number": 1,
                "duration_ms": 280706,
                "explicit": False,
                "external_ids": {"isrc": "USRO20149502"},
                "external_urls": {
                    "spotify": "https://open.spotify.com/track/5CJ1xQCFywhEryVUPJup5T"
                },
                "href": "https://api.spotify.com/v1/tracks/5CJ1xQCFywhEryVUPJup5T",
                "id": "5CJ1xQCFywhEryVUPJup5T",
                "is_local": False,
                "name": "The Boy Who Wouldn't Hoe Corn",
                "popularity": 43,
                "preview_url": "https://p.scdn.co/mp3-preview/ed7ba16c1f6474cfac1ad26d19eb7c47b7392b38?cid=774b29d4f13844c495f206cafdad9c86",
                "track_number": 2,
                "type": "track",
                "uri": "spotify:track:5CJ1xQCFywhEryVUPJup5T",
            },
        },
    ],
    "limit": 2,
    "next": "https://api.spotify.com/v1/me/tracks?offset=3&limit=3",
    "offset": 2,
    "previous": None,
    "total": 5,
}

EXAMPLE_SAVED_TRACKS_THREE = {
    "href": "https://api.spotify.com/v1/me/tracks?offset=0&limit=3",
    "items": [
        {
            "added_at": "2020-09-04T16:43:19Z",
            "track": {
                "album": {
                    "album_type": "single",
                    "artists": [
                        {
                            "external_urls": {
                                "spotify": "https://open.spotify.com/artist/0qzgOvNnbHiArRuXgkJfFI"
                            },
                            "href": "https://api.spotify.com/v1/artists/0qzgOvNnbHiArRuXgkJfFI",
                            "id": "0qzgOvNnbHiArRuXgkJfFI",
                            "name": "Beyond The Barricade",
                            "type": "artist",
                            "uri": "spotify:artist:0qzgOvNnbHiArRuXgkJfFI",
                        }
                    ],
                    "available_markets": ["..."],
                    "external_urls": {
                        "spotify": "https://open.spotify.com/album/0STdARrArJi55I4zbeSbx6"
                    },
                    "href": "https://api.spotify.com/v1/albums/0STdARrArJi55I4zbeSbx6",
                    "id": "0STdARrArJi55I4zbeSbx6",
                    "images": [
                        {
                            "height": 640,
                            "url": "https://i.scdn.co/image/ab67616d0000b2734fbf0642c674ea17daba8a7a",
                            "width": 640,
                        },
                        {
                            "height": 300,
                            "url": "https://i.scdn.co/image/ab67616d00001e024fbf0642c674ea17daba8a7a",
                            "width": 300,
                        },
                        {
                            "height": 64,
                            "url": "https://i.scdn.co/image/ab67616d000048514fbf0642c674ea17daba8a7a",
                            "width": 64,
                        },
                    ],
                    "name": "The Grey",
                    "release_date": "2018-05-03",
                    "release_date_precision": "day",
                    "total_tracks": 5,
                    "type": "album",
                    "uri": "spotify:album:0STdARrArJi55I4zbeSbx6",
                },
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/0qzgOvNnbHiArRuXgkJfFI"
                        },
                        "href": "https://api.spotify.com/v1/artists/0qzgOvNnbHiArRuXgkJfFI",
                        "id": "0qzgOvNnbHiArRuXgkJfFI",
                        "name": "Beyond The Barricade",
                        "type": "artist",
                        "uri": "spotify:artist:0qzgOvNnbHiArRuXgkJfFI",
                    }
                ],
                "available_markets": ["..."],
                "disc_number": 1,
                "duration_ms": 388906,
                "explicit": False,
                "external_ids": {"isrc": "NOJKW1801020"},
                "external_urls": {
                    "spotify": "https://open.spotify.com/track/0K9v3Jq3mI0phzWbeKAiqc"
                },
                "href": "https://api.spotify.com/v1/tracks/0K9v3Jq3mI0phzWbeKAiqc",
                "id": "0K9v3Jq3mI0phzWbeKAiqc",
                "is_local": False,
                "name": "The Grey",
                "popularity": 3,
                "preview_url": "https://p.scdn.co/mp3-preview/f7bf29379d5cd635c437cccabb05c6d0f46a3c39?cid=774b29d4f13844c495f206cafdad9c86",
                "track_number": 2,
                "type": "track",
                "uri": "spotify:track:0K9v3Jq3mI0phzWbeKAiqc",
            },
        }
    ],
    "limit": 2,
    "next": None,
    "offset": 4,
    "previous": None,
    "total": 5,
}


@pytest.fixture
def mock_artists():
    return EXAMPLE_ARTISTS


@pytest.fixture
def mock_saved_tracks():
    return [
        EXAMPLE_SAVED_TRACKS_ONE,
        EXAMPLE_SAVED_TRACKS_TWO,
        EXAMPLE_SAVED_TRACKS_THREE,
    ]


@pytest.fixture
def mock_playlist():
    return {
        'collaborative': False,
        'description': 'Made via Generalist',
        'external_urls': {'spotify': 'https://open.spotify.com/playlist/0BzfcK6UiDxD55YcJBqUsV'},
        'followers': {'href': None, 'total': 0},
        'href': 'https://api.spotify.com/v1/playlists/0BzfcK6UiDxD55YcJBqUsV',
        'id': '0BzfcK6UiDxD55YcJBqUsV',
        'images': [],
        'name': 'Generalist: country rap',
        'owner': {},
        'primary_color': None,
        'public': False,
        'snapshot_id': 'MSw2NzdmODg3ZjYxOWE1N2ZmMzQwZmIxN2Y4NDUyZGM4OWJmYjY1YTRl',
        'tracks': {'href': 'https://api.spotify.com/v1/playlists/0BzfcK6UiDxD55YcJBqUsV/tracks', 'items': [], 'limit': 100, 'next': None, 'offset': 0, 'previous': None, 'total': 0},
        'type': 'playlist',
        'uri': 'spotify:playlist:0BzfcK6UiDxD55YcJBqUsV'
    }


@pytest.fixture
def mock_tracks():
    return [
        {
            "id": "7b3MzbGB0aivEID99gCziJ",
            "name": "I Hate Hartley",
            "artists": ["The Amity Affliction"],
            "genres": ["australian metalcore", "melodic metalcore", "metalcore"],
        },
        {
            "id": "4qOeqS6CcGfCqGGiTauPLx",
            "name": "North Atlantic Vs North Carolina",
            "artists": ["Memphis May Fire"],
            "genres": ["melodic metalcore", "metalcore", "post-screamo", "screamo"],
        },
        {
            "id": "4AcFasviRreFQMBVdwo97k",
            "name": "The Biggest Lie",
            "artists": ["ROUGH STONE"],
            "genres": [],
        },
        {
            "id": "3fxHUQGwXjmHxeSx4CxYH4",
            "name": "Freddy Kreuger",
            "artists": ["Reuben"],
            "genres": [
                "british alternative rock",
                "math pop",
                "modern alternative rock",
                "uk post-hardcore",
            ],
        },
    ]


@pytest.fixture
def mock_tracks_sorted():
    return [
        {
            "id": "4qOeqS6CcGfCqGGiTauPLx",
            "name": "North Atlantic Vs North Carolina",
            "artists": ["Memphis May Fire"],
            "genres": ["melodic metalcore", "metalcore", "post-screamo", "screamo"],
        },
        {
            "id": "3fxHUQGwXjmHxeSx4CxYH4",
            "name": "Freddy Kreuger",
            "artists": ["Reuben"],
            "genres": [
                "british alternative rock",
                "math pop",
                "modern alternative rock",
                "uk post-hardcore",
            ],
        },
        {
            "id": "4AcFasviRreFQMBVdwo97k",
            "name": "The Biggest Lie",
            "artists": ["ROUGH STONE"],
            "genres": [],
        },
        {
            "id": "7b3MzbGB0aivEID99gCziJ",
            "name": "I Hate Hartley",
            "artists": ["The Amity Affliction"],
            "genres": ["australian metalcore", "melodic metalcore", "metalcore"],
        },
    ]


@pytest.fixture
def mock_user():
    return {
        "display_name": "michaelenger",
        "external_urls": {"spotify": "https://open.spotify.com/user/michaelenger"},
        "followers": {"href": None, "total": 24},
        "href": "https://api.spotify.com/v1/users/michaelenger",
        "id": "michaelenger",
        "images": [],
        "type": "user",
        "uri": "spotify:user:michaelenger",
    }
