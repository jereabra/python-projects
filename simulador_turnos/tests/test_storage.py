import json
import pytest
from pathlib import Path
import src.storage as storage
import pandas as pd

def test_guardar_cargar(tmp_path):
    storage.DATA_FILE = tmp_path / "turnos.json" 
    turnos_original = [
        {"nombre": "Test", "edad": 99, "especialidad": "Clínica"}
    ]
    storage.guardar_turnos(turnos_original)
    assert storage.guardar_turnos(turnos_original)
    turnos_cargados=storage.cargar_turnos()
    assert turnos_cargados==turnos_original
    return

def test_exportar(tmp_path):
    fakedata=tmp_path /'data'
    fakedata.mkdir(parents=True, exist_ok=True)
    storage.csv_file=fakedata/'turnos.csv'
    storage.txt_file=fakedata/'turnos.txt'


    turnos = [
        {"nombre": "Ana", "edad": 30, "especialidad": "Clínica"},
        {"nombre": "Luis", "edad": 45, "especialidad": "Cardiología"}
    ]

    storage.exportar_csv(turnos)
    assert storage.csv_file.exists()
    storage.exportar_txt(turnos)
    assert storage.txt_file.exists()

    df = pd.read_csv(storage.csv_file)
    assert list(df.columns) == ["nombre", "edad", "especialidad"]
    assert df.iloc[0]["nombre"] == "Ana"
    assert df.iloc[0]["edad"] == 30
    assert df.iloc[1]["especialidad"] == "Cardiología"
