import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tempfile
import json
import pandas as pd
from src.Storage import Storage

def test_storage_save_and_load_json(tmp_path):
    # Preparo datos de prueba
    data = [{"title": "Imagine", "artist": "John Lennon"}]
    file = "test_songs"
    # Uso una carpeta temporal para no ensuciar tu disco
    storage = Storage(file)
    storage.json_file = tmp_path / (file + ".json")
    # Testeo guardar
    storage.save_json(data)
    assert storage.json_file.exists()
    # Testeo cargar
    loaded = storage.load()
    assert loaded == data

def test_storage_export_csv(tmp_path):
    data = [{"title": "Imagine", "artist": "John Lennon"}]
    file = "test_songs"
    storage = Storage(file)
    storage.csv_file = tmp_path / (file + ".csv")
    storage.export_csv(data)
    assert storage.csv_file.exists()
    # Verifico que el CSV tiene la info correcta
    df = pd.read_csv(storage.csv_file)
    assert df.iloc[0]["title"] == "Imagine" # type: ignore
    assert df.iloc[0]["artist"] == "John Lennon" # type: ignore
