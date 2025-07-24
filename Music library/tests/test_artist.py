import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from src.Artist import Artist
from src.Album import Album

def test_artist_creation():
    artist = Artist("Queen", "UK", "Rock")
    assert artist.name == "Queen"
    assert artist.country == "UK"
    assert artist.genre == "Rock"

def test_artist_add_album():
    artist = Artist("Queen", "UK", "Rock")
    album = Album("A Night at the Opera", 43.08, "Queen", "Rock", 1975)
    artist.add_album(album.title)
    assert artist.albums[0] == "A Night at the Opera"

def test_artist_to_dict():
    artist = Artist("Queen", "UK", "Rock", ['A Night at the Opera'])
    #album = Album("A Night at the Opera", 43.08, "Queen", "Rock", 1975)
    #artist.add_album(album.title)
    
    assert artist.to_dict()["Name"] == "Queen"
    assert isinstance(artist.to_dict()["Albums"], list)
    print(artist.to_dict)
    #assert artist.to_dict()["Albums"][0] == "A Night at the Opera"

def test_artist_show(capsys):
    artist = Artist("Queen", "UK", "Rock")
    artist.show()
    captured = capsys.readouterr()
    output_lines = captured.out.strip().splitlines()
    assert any('Country:  UK'==line for line in output_lines), output_lines

