import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from src.Song import Song

def test_song_creation():
    song = Song("Imagine", "John Lennon", "Rock", 3.1, "Imagine")
    assert song.title == "Imagine"
    assert song.artist == "John Lennon"
    assert song.genre == "Rock"
    assert song.duration == 3.1
    assert song.album == "Imagine"

def test_song_validation_ok():
    song = Song("Imagine", "John Lennon", "Rock", 3.1, "Imagine")
    assert song.validate() is True

def test_song_validation_no_title():
    song = Song("", "John Lennon", "Rock", 3.1, "Imagine")
    assert song.validate() is False

def test_song_validation_duration():
    song = Song("Imagine", "John Lennon", "Rock", -2, "Imagine")
    assert song.validate() is False

def test_song_validation_no_artist():
    song = Song("Imagine", "", "Rock", 3.1, "Imagine")
    assert song.validate() is False
    
def test_song_to_dict():
    song = Song("Imagine", "John Lennon", "Rock", 3.1, "Imagine")
    d = song.to_dict()
    assert d["title"] == "Imagine"
    assert d["artist"] == "John Lennon"

def test_song_show(capsys):
    song = Song("Imagine", "John Lennon", "Rock", 3.1, "Imagine")
    song.show()
    captured = capsys.readouterr()
    output_lines = captured.out.strip().splitlines()
    assert any('Imagine  by  John Lennon :' ==line for line in output_lines), output_lines
