# Medical Appointment CLI / Turnos Médicos CLI

## Context / Contexto

**English:**  
This project is a Python-based command-line application to manage, organize, and export information about medical appointments ("turnos"). It allows the user to add new appointments, view all existing ones, filter by specialty or age, and export the data in multiple formats (JSON, CSV, TXT). All data is stored locally, making it ideal for small clinics, practices, or as a learning project.

**Español:**  
Este proyecto es una aplicación de línea de comandos en Python para gestionar, organizar y exportar información sobre turnos médicos. Permite al usuario agregar turnos, ver los existentes, filtrar por especialidad o edad, y exportar los datos en varios formatos (JSON, CSV, TXT). Todos los datos se almacenan localmente, por lo que es ideal para consultorios pequeños o como proyecto de aprendizaje.

---

## Strengths & Weaknesses / Fortalezas y Debilidades

**English:**

### Strengths
- Modular and organized code structure.
- Local storage of all data in JSON, CSV, and TXT formats.
- Simple and intuitive CLI interface.
- Includes data export options (CSV and TXT).
- Allows filtering by specialty or age.
- Logging system to track application activity.

### Weaknesses / Limitations
- No graphical interface (CLI only).
- No online multi-user support.
- No database integration (local files only).
- Error handling is basic.
- Data entry is fully manual.

---

**Español:**

### Fortalezas
- Código modular y organizado.
- Almacenamiento local de todos los datos en formatos JSON, CSV y TXT.
- Interfaz de línea de comandos simple e intuitiva.
- Incluye opciones de exportación de datos (CSV y TXT).
- Permite filtrar turnos por especialidad o edad.
- Sistema de logs para registrar la actividad.

### Debilidades / Limitaciones
- No tiene interfaz gráfica (solo CLI).
- No soporta múltiples usuarios en línea.
- No integra base de datos (solo archivos locales).
- Manejo de errores básico.
- La carga de datos es totalmente manual.

---

## About this project / Sobre el proyecto

**English:**  
This project is part of a series of personal developments to reinforce Python skills in file management, modularization, and building CRUD applications.  
It was created as a practical exercise in separating logic, storage, and user interface, and can be extended for larger use cases.

**Español:**  
Este proyecto forma parte de una serie de desarrollos personales para reforzar habilidades en Python sobre manejo de archivos, modularización y creación de aplicaciones CRUD.  
Se desarrolló como ejercicio práctico para separar la lógica, el almacenamiento y la interfaz de usuario, y puede extenderse a casos de uso más grandes.

---

## How does it work? / ¿Cómo funciona?

**English:**  
- The main entry point is `main.py`.
- On startup, it loads appointments from the JSON file.
- The user can add appointments, view all, filter by specialty or age, export to CSV/TXT, or save and exit.
- All data is stored in the `/data` folder.
- Logging is enabled (see `/data/app.log`).

**Español:**  
- El punto de entrada es `main.py`.
- Al iniciar, carga los turnos desde el archivo JSON.
- El usuario puede agregar turnos, ver todos, filtrar por especialidad o edad, exportar a CSV/TXT, o guardar y salir.
- Todos los datos se almacenan en la carpeta `/data`.
- El sistema de logs está activado (ver `/data/app.log`).

---

## Main files, classes and functions / Archivos, clases y funciones principales

**English:**

### Files

- `main.py`: The entry point. Handles the menu, user input, and coordinates all actions.
- `logic.py`: Contains the core functions to add, show, and filter appointments.
- `storage.py`: Handles loading, saving, exporting, and logging for all data.

### Main Functions

#### In `logic.py`:
- `agregar_turnos(turnos)`: Adds a new appointment.
- `mostrar_turnos(turnos)`: Shows all appointments in the list.
- `filtrar_por_especialidad(turnos)`: Filters appointments by medical specialty.
- `filtrar_mayores(turnos)`: Filters appointments by age (greater/less than a value).

#### In `storage.py`:
- `cargar_turnos()`: Loads appointments from a JSON file.
- `guardar_turnos(turnos)`: Saves appointments to a JSON file.
- `exportar_csv(turnos)`: Exports all appointments to CSV format.
- `exportar_txt(turnos)`: Exports all appointments to TXT format.
- `log(mensaje)`: Logs messages to a log file.

---

**Español:**

### Archivos

- `main.py`: Punto de entrada. Maneja el menú, la interacción con el usuario y coordina todas las acciones.
- `logic.py`: Contiene las funciones principales para agregar, mostrar y filtrar turnos.
- `storage.py`: Maneja la carga, guardado, exportación y registro de toda la información.

### Funciones principales

#### En `logic.py`:
- `agregar_turnos(turnos)`: Agrega un nuevo turno.
- `mostrar_turnos(turnos)`: Muestra todos los turnos de la lista.
- `filtrar_por_especialidad(turnos)`: Filtra turnos por especialidad médica.
- `filtrar_mayores(turnos)`: Filtra turnos por edad (mayores/menores a un valor).

#### En `storage.py`:
- `cargar_turnos()`: Carga los turnos desde un archivo JSON.
- `guardar_turnos(turnos)`: Guarda los turnos en un archivo JSON.
- `exportar_csv(turnos)`: Exporta todos los turnos a formato CSV.
- `exportar_txt(turnos)`: Exporta todos los turnos a formato TXT.
- `log(mensaje)`: Registra mensajes en un archivo de logs.

---

## Usage / Uso

**English:**  
1. Install the required dependencies (see `requirements.txt` if available):
pip install -r requirements.txt
2. Run the application:
python main.py


**Español:**  
1. Instalá las dependencias necesarias (ver `requirements.txt` si está disponible):
pip install -r requirements.txt
2. Ejecutá la aplicación:
python main.py


---

## Tests

**English:**  
- This project does not currently include automated tests, but manual testing can be performed via the CLI.

**Español:**  
- El proyecto no incluye tests automáticos por el momento, pero se puede probar manualmente desde la interfaz de línea de comandos.

---

## About the author / Sobre el autor

Made with 💻 and 🩺 by jereabra.
