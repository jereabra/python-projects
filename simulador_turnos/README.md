# Gestor de Turnos CLI

Aplicación de línea de comandos en Python para gestionar turnos médicos:

- Crear, listar y filtrar turnos  
- Persistencia en JSON (`data/turnos.json`)  
- Exportación a CSV (`data/turnos.csv`) y TXT (`data/turnos.txt`)  
- Registro de operaciones y errores en `data/app.log`  

---

## Instalación

```bash
git clone <URL_DEL_REPOSITORIO>
cd gestor-turnos
python3 -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows PowerShell
.venv\Scripts\activate
pip install -r requirements.txt


Uso
python src/main.py
El menú ofrece estas opciones:

Agregar turno
Solicita nombre, edad y especialidad; guarda en JSON.

Mostrar todos los turnos
Carga data/turnos.json y muestra cada registro con índice.

Filtrar por especialidad
Pide una letra (A/B/C) y muestra solo los turnos de esa especialidad.

Filtrar por edad
Pide una edad y muestra los turnos mayores o menores, según opción.

Exportar a CSV
Genera data/turnos.csv con columnas separadas por comas.

Generar reporte TXT
Crea data/reporte.txt con una línea legible por cada turno.

Salir
Guarda cambios en JSON y registra en el log antes de cerrar.

Estructura

simulador_turnos/
├── src/
│   ├── main.py       # Punto de entrada y menú
│   ├── logic.py      # Funciones CRUD y filtros
│   └── storage.py    # I/O, exportación y logging
├── data/             # Archivos generados por la app
│   ├── turnos.json
│   ├── turnos.csv
│   ├── reporte.txt
│   └── app.log
├── tests/            # (opcional) pruebas unitarias con pytest
├── requirements.txt  # Librerías externas necesarias
└── README.md         # Documentación del proyecto


