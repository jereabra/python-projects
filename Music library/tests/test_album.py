import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from src.Album import Album
from src.Song import Song

def test_album_creation():
    album = Album("Abbey Road", 47.23, "The Beatles", "Rock", 1969)
    assert album.title == "Abbey Road"
    assert album.artist == "The Beatles"
    assert album.genre == "Rock"
    assert album.duration == 47.23
    assert album.year == 1969

def test_album_addsong():
    album = Album("Abbey Road", 47.23, "The Beatles", "Rock", 1969)
    #song = Song("Come Together", "The Beatles", "Rock", 4.2, "Abbey Road")
    album.addsong("Come Together")
    assert album.slist[0] == "Come Together"

def test_album_validate():
    album = Album("Abbey Road", 47.23, "The Beatles", "Rock", 1969)
    assert album.validate() is True
    album2 = Album("", 47.23, "The Beatles", "Rock", 1969)
    assert album2.validate() is False
    album3 = Album("Abbey Road", -47.23, "The Beatles", "Rock", 1969)
    assert album3.validate() is False
    album4 = Album("Abbey Road", 47.23, "The Beatles", "Rock", 1600)
    assert album4.validate() is False    
    album5 = Album("Abbey Road", 47.23, "", "Rock", 1969)
    assert album5.validate() is False
    album6 = Album("Abbey Road", 47.23, "The Beatles", "", 1969)
    assert album6.validate() is False

def test_album_to_dict():
    album = Album("Abbey Road", 47.23, "The Beatles", "Rock", 1969)
    song = Song("Come Together", "The Beatles", "Rock", 4.2, "Abbey Road")
    album.addsong(song.title)
    d = album.to_dict()
    assert d["title"] == "Abbey Road"
    assert isinstance(d["slist"], list)
    assert d["slist"][0] == "Come Together"

def test_album_show(capsys):
    album = Album("Abbey Road", 47.23, "The Beatles", "Rock", 1969)
    album.show()
    captured = capsys.readouterr()
    output_lines = captured.out.strip().splitlines()
    assert any('Abbey Road  by  The Beatles :' ==line for line in output_lines), output_lines

def test_remove_song():
    album = Album("Abbey Road", 47.23, "The Beatles", "Rock", 1969, ['Come Together'])
    assert album.slist[0]=='Come Together'
    album.removesong('Come Together')
    assert len(album.slist)==0