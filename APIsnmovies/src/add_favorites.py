import sys
import os

# Ajustar sys.path para importar tus módulos desde src/
sys.path.insert(0, os.path.abspath('src'))

from .ApiClient import ApiClient
from .Favorites import Favorites
import dotenv

# Cargar tu API Key desde .env o variable de entorno
dotenv.load_dotenv()
api_key = os.getenv("OMDB_API_KEY")
if not api_key:
    raise Exception("OMDB_API_KEY not set")

# Usuario al que le vas a agregar favoritos
user = Favorites("Base")

# Lista de películas a agregar (podés leerlas de un archivo)
with open("data/lista_peliculas.txt", "r", encoding="utf-8") as f:
    titles = [line.strip() for line in f if line.strip()]

client = ApiClient(api_key)
for title in titles:
    data = client.search_title(title)
    if data and data.get("Title"):
        # Agregá solo si no está ya en favoritos
        if all(item.get('Title') != data.get('Title') for item in user.memory):
            user.add_favorite(data)
            print(f"Agregado: {data['Title']}")
        else:
            print(f"Ya estaba: {data['Title']}")
    else:
        print(f"No encontrado: {title}")

# Guardar los cambios
user.save_all()
print("Favoritos actualizados.")
