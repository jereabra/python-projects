import json
import pandas as pd
from pathlib import Path
from datetime import datetime

json_file= Path(__file__).parent.parent/'data'/'turnos.json'
csv_file= Path(__file__).parent.parent/'data'/'turnos.csv'
txt_file= Path(__file__).parent.parent/'data'/'turnos.txt'
log_file=Path(__file__).parent.parent/'data'/'app.log'

def log(mensaje):
    try:
        log_file.parent.mkdir(parents=True, exist_ok=True) #me aseguro que existe
        timestamp= datetime.now().isoformat(sep=' ', timespec='seconds')
        linea=f"[{timestamp}] {mensaje}\n"
        with log_file.open('a', encoding='utf-8') as f: #a para appendear
            f.write(linea)
    except OSError:
        print("Hubo un error inesperado")


def cargar_turnos():
    try:
        json_file.parent.mkdir(parents=True, exist_ok=True)
        with open(json_file, 'r', encoding='utf-8') as f:
            turnos=json.load(f)
            log('Se cargaron correctamente los turnos')
    except FileNotFoundError:
        turnos=[]
        log('No se cargaron correctamente los turnos, no se encontró el archivo')
    except json.JSONDecodeError:
        log('Problema en la lectura del archivo, la lista se volverá a hacer')
        turnos=[]
    return turnos
   
def guardar_turnos(turnos):
    try:
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(turnos, f, indent=2, ensure_ascii=False)
            log('Se guardaron los turnos')
    except OSError:
        log('Error en el archivo, no se pudieron guardar los turnos')
    return turnos
    
def exportar_csv(turnos):
    try:
        df=pd.DataFrame(turnos)
        csv_file.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(csv_file, index=False)
        log('Se exportó el CSV')
    except OSError:
       log("No se pudo convertir a CSV")
    return

def exportar_txt(turnos):
    try:
        txt_file.parent.mkdir(parents=True, exist_ok=True)
        with txt_file.open('w', encoding='utf-8') as f:
            i=1
            for i, t in enumerate(turnos, start=1):
                linea = f"{i}. {t['nombre']}, {t['edad']} años, {t['especialidad']}\n"
                f.write(linea)
        log('Se exportó el TXT')
    except OSError:
        log('No se pudo generar el texto')
    return