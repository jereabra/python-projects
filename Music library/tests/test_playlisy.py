import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from src.Playlist import Playlist
from src.Song import Song

def test_playlist_creation():
    pl = Playlist("Roadtrip")
    assert pl.name == "Roadtrip"
    assert pl.songs == []

def test_playlist_addsong():
    pl = Playlist("Roadtrip")
    song = Song("Highway to Hell", "AC/DC", "Rock", 3.2, "Highway to Hell")
    pl.addsong(song.title)
    assert pl.songs[0] == "Highway to Hell"

def test_playlist_to_dict():
    pl = Playlist("Roadtrip")
    song = Song("Highway to Hell", "AC/DC", "Rock", 3.2, "Highway to Hell")
    #pl.addsong(song.title)
    assert pl.to_dict()["name"] == "Roadtrip"

def test_album_show(capsys):
    pl = Playlist("Roadtrip")
    pl.show()
    captured = capsys.readouterr()
    output_lines = captured.out.strip().splitlines()
    assert any("This is the list of songs in the playlist:" ==line for line in output_lines), output_lines

def test_remove_song_from_playlist():
    pl = Playlist("Roadtrip")
    song = Song("Highway to Hell", "AC/DC", "Rock", 3.2, "Highway to Hell")
    pl.addsong(song.title)
    assert pl.songs[0] == "Highway to Hell"
    pl.removesong('Highway to Hell')    
    assert len(pl.songs)==0