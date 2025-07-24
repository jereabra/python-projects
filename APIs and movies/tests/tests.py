import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import io
from ApiClient import ApiClient
from Favorites import Favorites
import utils as u
import search as s
from dotenv import load_dotenv

# Configurar API Key para los tests
load_dotenv()
API_KEY = os.getenv("OMDB_API_KEY", None)
if not API_KEY:
    raise Exception("OMDB_API_KEY not set in environment variables")

client = ApiClient(API_KEY)

@pytest.fixture
def titanic_data():
    # Test real sobre una peli que seguro existe
    return client.search_title("Titanic")

@pytest.fixture
def search_multi():
    # Prueba una búsqueda múltiple que dé varios resultados
    return client.search_specifics("matrix", page=1)

def test_search_title_returns_dict(titanic_data):
    assert isinstance(titanic_data, dict)
    assert titanic_data.get("Title", "").lower() == "titanic"

def test_search_id_returns_same_as_title(titanic_data):
    imdb_id = titanic_data.get("imdbID")
    data_by_id = client.search_id(imdb_id)
    assert isinstance(data_by_id, dict)
    assert data_by_id.get("Title") == "Titanic"

def test_search_specifics_contains_search(search_multi):
    assert "Search" in search_multi
    assert isinstance(search_multi["Search"], list)
    assert any("Matrix" in item["Title"] for item in search_multi["Search"])

def test_filter_genre_works(search_multi):
    # Buscar películas de acción en los resultados de Matrix
    items = search_multi["Search"]
    filtered = s.filter_genre(items, "Action")
    assert all("Action" in item.get("Genre", "") for item in filtered)

def test_order_rating_and_year(search_multi):
    # Prueba que ordenar por rating y año no rompe y ordena
    items = search_multi["Search"]
    ordered_by_rating = s.order_rating(items)
    ordered_by_year = s.order_year(items)
    assert isinstance(ordered_by_rating, list)
    assert isinstance(ordered_by_year, list)

def test_format_results_and_title(search_multi):
    items = search_multi["Search"]
    formatted = s.format_results(items)
    assert isinstance(formatted, list)
    assert all(isinstance(line, str) for line in formatted)
    first_item = items[0]
    formatted_title = s.format_title(first_item)
    assert isinstance(formatted_title, list)
    assert any("Titanic" in line or "Matrix" in line for line in formatted_title)

def test_extract_title_and_actors(search_multi):
    items = search_multi["Search"]
    titles = s.extract_title(items)
    assert isinstance(titles, list)
    assert all(isinstance(title, str) for title in titles)
    first_item = items[0]
    actors = s.extract_actors(first_item)
    assert isinstance(actors, str) or actors is None

def test_favorites_add_and_remove(tmp_path):
    # Prueba Favorites usando un directorio temporal para no modificar datos reales
    client_name = "testuser"
    favs = Favorites(client_name)
    favs.json_file = tmp_path / f"{client_name}.json"
    favs.csv_file = tmp_path / f"{client_name}.csv"
    dummy_movie = {"Title": "Dummy Movie", "Year": "2020"}
    favs.add_favorite(dummy_movie)
    assert dummy_movie in favs.memory
    favs.save_all()
    favs.remove_favorite(dummy_movie)
    assert dummy_movie not in favs.memory

def test_utils_random_search_and_select(monkeypatch):
    # Mockea el archivo y resultados
    def fake_open(*args, **kwargs):
        return io.StringIO('batmam\nmatrix\n')
    monkeypatch.setattr("builtins.open", fake_open)
    kword = u.random_search()
    assert isinstance(kword, str)
    sample_results = [{"Title": "A"}, {"Title": "B"}]
    selected = u.random_select(sample_results)
    assert selected in ["A", "B"]

def test_validate_on_full_and_empty():
    # Dict tipo búsqueda múltiple
    search_type = {"Search": [{"Title": "A"}], "totalResults": "1", "Response": "True"}
    single_type = {"Title": "A", "Response": "True"}
    assert s.validate(search_type) is True
    assert s.validate(single_type) is True
    assert s.validate([]) is False
    assert s.validate({}) is False

