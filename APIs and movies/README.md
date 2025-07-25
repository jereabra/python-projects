# Movie Database CLI

## Context / Contexto

**English:**  
This project is a Python-based command-line application to search, organize, and manage information about movies and series. It uses the [OMDb API](http://www.omdbapi.com/) to retrieve detailed data about movies, TV shows, and more.

**Español:**  
Este proyecto es una aplicación de línea de comandos en Python para buscar, organizar y gestionar información sobre películas y series. Utiliza la [OMDb API](http://www.omdbapi.com/) para obtener datos detallados de películas, series y más.

---

## Strengths & Weaknesses / Fortalezas y Debilidades

**English:**

### Strengths
- Modular and extensible code structure.
- Clean separation of logic (API, search, user data).
- Works fully offline once data is saved locally (except for new API searches).
- CLI interface is user-friendly and guides through all options.
- All user data is stored in personal files, enabling multiple users.

### Weaknesses / Limitations
- No GUI: the project is fully command-line based.
- No concurrency or async API calls (might be slow for large batch operations).
- Error handling is basic (focus is on result logic, not advanced resilience).
- No advanced movie recommendation system (relies on OMDb API only).
- Needs an API key and internet connection for new data.
- Currently English-only for data, CLI prompts are in English and Spanish.

---

**Español:**

### Fortalezas
- Código modular y extensible.
- Separación clara de lógica (API, búsquedas, datos de usuario).
- Funciona totalmente offline una vez guardados los datos (excepto nuevas búsquedas).
- Interfaz de línea de comandos amigable y guiada.
- Manejo de múltiples usuarios mediante archivos personales.

### Debilidades / Limitaciones
- No tiene interfaz gráfica (sólo CLI).
- Sin concurrencia ni asincronía (puede ser lento con operaciones masivas).
- Manejo de errores simple (enfocado en la lógica principal, no en fallos de red o API).
- No incluye recomendaciones inteligentes, sólo las de OMDb.
- Necesita clave de API y conexión a internet para búsquedas nuevas.
- Los datos de las películas están sólo en inglés (por limitación de la API).

---

## About this project / Sobre el proyecto

**English:**  
This project is part of a personal learning path to strengthen Python skills in software architecture, OOP, and API integration.  
It’s one in a series of small projects developed to reinforce best practices, modularization, and real-world code testing, with a special focus on code that can be reused in other domains.

**Español:**  
Este proyecto forma parte de una serie de desarrollos personales para reforzar habilidades de Python en arquitectura, POO e integración de APIs.  
Es uno de varios proyectos realizados para poner en práctica buenas prácticas, modularización y testing real, siempre pensando en reusar el código en otros ámbitos y futuros desarrollos.

---

## How does it work? / ¿Cómo funciona?

**English:**  
- The main entry point is `main.py` (in `/src`).
- When running, the program will prompt for a username and create/load a personal favorites/history file for each user.
- The user can search for movies/series using different criteria. Results are shown in the console with options to filter, sort, expand, and save.
- All API requests are handled via `ApiClient.py`.
- Favorites and history are managed with the `Favorites.py` class, which handles JSON and CSV storage.
- Utility functions for formatting, filtering, and extracting data are in `search.py` and `utils.py`.
- All data is stored locally in the `/data` folder.
- Logging is enabled (see `/data/logs.log`).

**Español:**  
- El punto de entrada es `main.py` (en `/src`).
- Al ejecutarlo, el programa pide un nombre de usuario y crea/carga archivos personales de favoritos e historial para cada usuario.
- El usuario puede buscar películas/series de distintas formas. Los resultados se muestran por consola con opciones para filtrar, ordenar, expandir y guardar.
- Todas las consultas a la API se gestionan en `ApiClient.py`.
- Favoritos e historial se manejan con la clase `Favorites.py`, que guarda datos en JSON y CSV.
- Las utilidades para formatear, filtrar y extraer datos están en `search.py` y `utils.py`.
- Todos los datos se guardan localmente en la carpeta `/data`.
- El sistema de logs está activado (ver `/data/logs.log`).

---

## Main files, classes and functions / Archivos, clases y funciones principales

**English:**

### Files / Archivos

### Files / Archivos

- `main.py`: The entry point. Handles user interaction, navigation menus and overall workflow.
- `ApiClient.py`: Handles all interactions with the OMDb API (HTTP requests, parsing, and error management).
- `Favorites.py`: Manages favorites and history per user. Handles local JSON/CSV storage.
- `search.py`: Provides search, filter, order, format and validation utilities for movie/series data.
- `utils.py`: General helper functions for user interaction, random selections, and menu handling.
- `add_favorites.py`: Script for batch-adding a list of movies/series to a user's favorites, using the existing codebase. Reads a list of titles, searches each in the API, and adds them to the user's favorites file, avoiding duplicates.

### Main Classes

- **ApiClient**:  
  Class to manage all API requests: search by title, ID, keyword, advanced search and series details.

- **Favorites**:  
  Class for saving, loading and managing the user's favorites and search/history data. Handles saving and removing items, and exporting to JSON/CSV.

### Main Functions

#### In `search.py`:
- `search_title(results, title)`: Finds a movie/series in a list of results by title.
- `filter_genre(results, genre)`: Filters a list by genre.
- `filter_year(results, year)`: Filters by release year.
- `filter_type(results, type)`: Filters by type (movie, series, game).
- `filter_actor(results, actor)`: Filters by actor name.
- `order_year(results, des=True)`: Orders a list by year (desc/asc).
- `order_rating(results)`: Orders by IMDB rating.
- `format_results(results)`: Formats a list of results for display.
- `format_title(item)`: Formats one result in detail.
- `extract_title(results)`: Extracts only the titles from a list.
- `extract_actors(title)`: Gets actors from a result.
- `validate(results)`: Validates result data structure.

#### In `utils.py`:
- `random_search()`: Picks a random keyword from a file for random searches.
- `random_select(search_results)`: Picks a random title from search results.
- `select_choice(max_number)`: Handles menu selection from user input.
- `quit()`: Prints a goodbye message.

---

**Español:**

### Archivos

- `main.py`: Punto de entrada. Maneja la interacción con el usuario, menús y flujo general.
- `ApiClient.py`: Maneja todas las interacciones con la API de OMDb (requests, parseo, gestión de errores).
- `Favorites.py`: Maneja favoritos e historial por usuario. Guarda en archivos JSON/CSV.
- `search.py`: Utilidades para buscar, filtrar, ordenar, formatear y validar datos de películas/series.
- `utils.py`: Funciones de ayuda general para interacción, selección aleatoria y manejo de menús.
- `add_favorites.py`: Script para agregar en lote una lista de películas/series a los favoritos de un usuario, usando el mismo sistema del proyecto. Lee una lista de títulos, busca cada uno en la API y los agrega al archivo de favoritos del usuario, evitando duplicados.

### Clases principales

- **ApiClient**:  
  Clase para gestionar todas las búsquedas y requests a la API: búsqueda por título, ID, palabra clave, búsqueda avanzada y series.

- **Favorites**:  
  Clase para guardar, cargar y manejar los favoritos y el historial del usuario. Permite agregar y quitar items y exportar a JSON/CSV.

### Funciones principales

#### En `search.py`:
- `search_title(results, title)`: Busca una película/serie en una lista de resultados por título.
- `filter_genre(results, genre)`: Filtra una lista por género.
- `filter_year(results, year)`: Filtra por año de estreno.
- `filter_type(results, type)`: Filtra por tipo (película, serie, juego).
- `filter_actor(results, actor)`: Filtra por nombre de actor.
- `order_year(results, des=True)`: Ordena una lista por año (desc/asc).
- `order_rating(results)`: Ordena por rating de IMDB.
- `format_results(results)`: Formatea una lista de resultados para mostrar.
- `format_title(item)`: Formatea el detalle de un resultado.
- `extract_title(results)`: Extrae solo los títulos de una lista.
- `extract_actors(title)`: Obtiene los actores de un resultado.
- `validate(results)`: Valida la estructura de los datos recibidos.

#### En `utils.py`:
- `random_search()`: Elige una palabra al azar de un archivo para búsquedas aleatorias.
- `random_select(search_results)`: Elige un título al azar de los resultados.
- `select_choice(max_number)`: Maneja la selección de menús por input.
- `quit()`: Muestra un mensaje de despedida.

---

## Usage / Uso

**English:**  
1. Get a free API key from [OMDb API](http://www.omdbapi.com/apikey.aspx).
2. Set your API key in a `.env` file at the root of the project:  
OMDB_API_KEY=your_api_key_here
3. Install the required dependencies:
pip install -r requirements.txt
4. Run the application:
python src/main.py


**Español:**  
1. Conseguí una clave de API gratuita desde [OMDb API](http://www.omdbapi.com/apikey.aspx).
2. Guardá tu clave en un archivo `.env` en la raíz del proyecto:  
OMDB_API_KEY=your_api_key_here
3. Instalá las dependencias necesarias:
pip install -r requirements.txt
4. Ejecutá la aplicación:
python src/main.py


---

## Tests

**English:**  
- Automated tests are in `/tests/tests.py`.
- Run with:
pytest tests/tests.py


**Español:**  
- Los tests automáticos están en `/tests/tests.py`.
- Ejecutalos con:
pytest tests/tests.py


---

## About the author / Sobre el autor

Made with 💻 and 🎬 by jereabra.

