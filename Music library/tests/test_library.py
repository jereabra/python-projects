import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.Library import Library

def test_add_and_search_element():
    lib = Library('songs', 'artists', 'albums', 'playlists')
    song = {"title": "Imagine", "artist": "John Lennon", "genre": "Rock", "duration": 3.1, "album": "Imagine"}
    lib.add_element("songs", song)
    result = lib.search_element("songs", "Imagine")
    assert result is not None
    assert result["artist"] == "John Lennon"

def test_remove_element():
    lib = Library('songs', 'artists', 'albums', 'playlists')
    song = {"title": "Imagine", "artist": "John Lennon", "genre": "Rock", "duration": 3.1, "album": "Imagine"}
    lib.add_element("songs", song)
    lib.remove_element("songs", song)
    result = lib.search_element("songs", "Imagine")
    assert result is None

def test_change_element():
    lib = Library('songs', 'artists', 'albums', 'playlists')
    song = {"title": "Imagine", "artist": "John Lennon", "genre": "Rock", "duration": 3.1, "album": "Imagine"}
    lib.add_element("songs", song)
    updated = {"title": "Imagine", "artist": "John Lennon", "genre": "Rock", "duration": 4.0, "album": "Imagine"}
    lib.change_element("songs", "Imagine", updated)
    result = lib.search_element("songs", "Imagine")
    assert result["duration"] == 4.0 # type: ignore

def test_filter_elements():
    lib = Library('songs', 'artists', 'albums', 'playlists')
    song1 = {"title": "Imagine", "artist": "John Lennon", "genre": "Rock", "duration": 3.1, "album": "Imagine"}
    song2 = {"title": "Yesterday", "artist": "The Beatles", "genre": "Pop", "duration": 2.3, "album": "Help!"}
    lib.add_element("songs", song1)
    lib.add_element("songs", song2)
    filtered = lib.filter_elements("songs", "artist", "John Lennon")
    assert len(filtered) == 1
    assert filtered[0]["title"] == "Imagine"
