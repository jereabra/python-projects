# Music Library CLI / Biblioteca Musical CLI

## Context / Contexto

**English:**  
This project is a Python-based command-line application to manage, organize, and explore information about songs, albums, artists, and playlists. The system is fully local (no external API needed), and designed for building, editing, and consulting your personal music collection.

**Español:**  
Este proyecto es una aplicación de línea de comandos en Python para gestionar, organizar y explorar información sobre canciones, álbumes, artistas y playlists. El sistema funciona totalmente offline (no requiere API externa) y está diseñado para crear, editar y consultar tu propia colección musical.

---

## Strengths & Weaknesses / Fortalezas y Debilidades

**English:**

### Strengths
- Modular and extensible code structure.
- Clear separation between data, logic, and storage.
- All user data is stored locally in JSON and CSV formats.
- CLI interface is simple and interactive.
- Manages songs, albums, artists, and playlists.
- Codebase is ideal for learning OOP and data management.

### Weaknesses / Limitations
- No graphical interface (CLI only).
- No integration with music streaming services or APIs.
- Single user and manual data entry.
- Basic error handling.
- No audio playback or music file support.
- No smart recommendations (relies on user input).

---

**Español:**

### Fortalezas
- Código modular y extensible.
- Separación clara entre datos, lógica y almacenamiento.
- Todos los datos se guardan localmente en formato JSON y CSV.
- Interfaz de línea de comandos sencilla e interactiva.
- Permite gestionar canciones, álbumes, artistas y playlists.
- Código ideal para aprender POO y gestión de datos.

### Debilidades / Limitaciones
- No tiene interfaz gráfica (sólo CLI).
- Sin integración con servicios de música o APIs externas.
- Uso de un solo usuario y carga manual de datos.
- Manejo de errores básico.
- No reproduce audio ni administra archivos de música.
- No incluye recomendaciones inteligentes (depende del usuario).

---

## About this project / Sobre el proyecto

**English:**  
This project is part of a personal learning path to strengthen Python skills, especially in OOP, file management, and building CRUD (Create, Read, Update, Delete) applications.  
It belongs to a series of projects developed to practice best practices, modularization, and real-world code testing, with the idea that code can be reused or extended in future projects.

**Español:**  
Este proyecto forma parte de una serie de desarrollos personales para reforzar habilidades de Python en POO, manejo de archivos y construcción de aplicaciones CRUD.  
Es uno de varios proyectos realizados para practicar buenas prácticas, modularización y testing real, siempre pensando en reusar o ampliar el código en futuros desarrollos.

---

## How does it work? / ¿Cómo funciona?

**English:**  
- The main entry point is `main.py`.
- When running, the program displays a menu to let you add, remove, modify, search or filter songs, albums, artists, and playlists.
- All data is stored locally in the `/data` folder, in JSON and CSV format.
- User can build playlists, add songs/albums/artists, and filter/search by various criteria.
- The application is fully interactive via the command line.

**Español:**  
- El punto de entrada es `main.py`.
- Al ejecutarlo, el programa muestra un menú para agregar, quitar, modificar, buscar o filtrar canciones, álbumes, artistas y playlists.
- Todos los datos se almacenan localmente en la carpeta `/data`, en formato JSON y CSV.
- El usuario puede armar playlists, agregar canciones/álbumes/artistas y buscar o filtrar por distintos criterios.
- La aplicación es totalmente interactiva desde la línea de comandos.

---

## Main files, classes and functions / Archivos, clases y funciones principales

**English:**

### Files

- `main.py`: The entry point. Handles user interaction, menus and workflow.
- `Library.py`: Core class to load, save, search, modify and filter the entire collection (songs, albums, artists, playlists).
- `Song.py`: Defines the Song class, with validation and display methods.
- `Album.py`: Defines the Album class, manages its song list and validation.
- `Artist.py`: Defines the Artist class, handles its albums.
- `Playlist.py`: Defines the Playlist class, manages its list of songs.
- `Storage.py`: Handles all data saving/loading in JSON/CSV.

### Main Classes

- **Library**:  
  Loads the entire music library from files, and manages adding, removing, searching, modifying and filtering songs, albums, artists and playlists.

- **Song**:  
  Represents a song, with title, artist, genre, duration and album. Includes validation and display methods.

- **Album**:  
  Represents an album with title, artist, year, genre, duration, and a list of songs. Can add/remove songs.

- **Artist**:  
  Represents an artist with name, country, genre, and a list of albums.

- **Playlist**:  
  Represents a playlist, storing a list of songs (by reference or object).

- **Storage**:  
  Handles loading and saving data in JSON/CSV files for each entity.

### Main Functions (by file)

- `Library.add_element(file, info)`: Add new item to library.
- `Library.remove_element(file, info)`: Remove item from library.
- `Library.change_element(file, name, info)`: Modify existing item.
- `Library.search_element(file, name)`: Find item by name/title.
- `Library.filter_elements(file, criteria, specific)`: Filter items by criteria (e.g., artist, genre).
- `Library.save(file)`: Save changes to disk.

- `Song.validate()`, `Album.validate()`: Validate fields before saving.
- `show()`: Display details of a song, album, artist or playlist.

---

**Español:**

### Archivos

- `main.py`: Punto de entrada. Maneja la interacción con el usuario, menús y flujo principal.
- `Library.py`: Clase central que carga, guarda, busca, modifica y filtra toda la colección (canciones, álbumes, artistas, playlists).
- `Song.py`: Define la clase Canción, con métodos de validación y muestra.
- `Album.py`: Define la clase Álbum, maneja su lista de canciones y validación.
- `Artist.py`: Define la clase Artista, maneja su lista de álbumes.
- `Playlist.py`: Define la clase Playlist, gestiona su lista de canciones.
- `Storage.py`: Maneja el guardado/carga de datos en JSON/CSV.

### Clases principales

- **Library**:  
  Carga la biblioteca musical completa desde archivos y permite agregar, quitar, buscar, modificar y filtrar canciones, álbumes, artistas y playlists.

- **Song (Canción)**:  
  Representa una canción, con título, artista, género, duración y álbum. Incluye validación y métodos de muestra.

- **Album (Álbum)**:  
  Representa un álbum con título, artista, año, género, duración y una lista de canciones. Permite agregar/quitar canciones.

- **Artist (Artista)**:  
  Representa un artista con nombre, país, género y lista de álbumes.

- **Playlist**:  
  Representa una playlist, guardando una lista de canciones (por referencia u objeto).

- **Storage**:  
  Maneja la carga y guardado de datos en archivos JSON/CSV por entidad.

### Funciones principales (por archivo)

- `Library.add_element(file, info)`: Agrega un elemento a la biblioteca.
- `Library.remove_element(file, info)`: Quita un elemento.
- `Library.change_element(file, name, info)`: Modifica un elemento.
- `Library.search_element(file, name)`: Busca por nombre/título.
- `Library.filter_elements(file, criteria, specific)`: Filtra por criterio (artista, género).
- `Library.save(file)`: Guarda los cambios en disco.

- `Song.validate()`, `Album.validate()`: Valida los campos antes de guardar.
- `show()`: Muestra detalles de una canción, álbum, artista o playlist.

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

Made with 💻 and 🎵 by jereabra.
