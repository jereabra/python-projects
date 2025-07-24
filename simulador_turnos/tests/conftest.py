# tests/conftest.py

import sys
import pathlib

# Añade la carpeta raíz del proyecto al path de Python
root = pathlib.Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(root))
