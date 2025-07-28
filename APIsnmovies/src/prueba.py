from . import analysis
from . import ml_model
from .Suggestions import Suggestion
import os
import joblib


# Base path desde la raíz del proyecto
BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Ruta absoluta a los archivos
jere_path = os.path.join(BASE_PATH, 'data', 'Jere.json')
base_path = os.path.join(BASE_PATH, 'data', 'base.json')
model_path= os.path.join(BASE_PATH, 'data', 'models', 'model_knn.pkl')
mlb_path=os.path.join(BASE_PATH, 'data', 'models', 'mlb_knn.pkl')


# 1. Cargar y limpiar favoritos
favoritos_df = analysis.load_fav(jere_path)
favoritos_df = analysis.clean_data(favoritos_df)

# 2. Cargar y limpiar base de datos
base_df = analysis.load_fav(base_path)
base_df = analysis.clean_data(base_df)

# 3. Preprocesar y entrenar modelo
base_features, mlb = ml_model.preprocessing(base_df)
modelo = ml_model.model(base_features)
ml_model.save_model(modelo)
#favoritos_pre=ml_model.preprocessing(favoritos_df, mlb)
joblib.dump(mlb, mlb_path)
# 4. Crear instancia del recomendador y pedir sugerencias
mlb = joblib.load(mlb_path)
reco = Suggestion(base_df, model_path)
sugerencias = reco.recommend(favoritos_df, mlb)

# 5. Mostrar resultados
for peli in sugerencias:
    print("🎬", peli)
