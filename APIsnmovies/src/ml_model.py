from sklearn.preprocessing import MultiLabelBinarizer
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
import joblib
import os

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

model_path= os.path.join(BASE_PATH, 'data', 'models', 'model_knn.pkl')

def preprocessing(df, mlb=None):
    if mlb is None:
        mlb = MultiLabelBinarizer()
        binary_genre = np.array(mlb.fit_transform(df["Genre"]))
    else:
        binary_genre = np.array(mlb.transform(df["Genre"]))
    df_genre=pd.DataFrame(binary_genre, columns=mlb.classes_)
    df=pd.concat([df, df_genre], axis=1)
    df.drop(columns=['Genre', 'Type', 'Title'], inplace=True)
    df.dropna(inplace=True)
    return df,mlb

def model(df, n=5):
    model=NearestNeighbors(n_neighbors=n, metric='euclidean')
    model.fit(df)
    return model

def save_model(model, route=model_path):
    joblib.dump(model, route)

def load_model(route=model_path):
    return joblib.load(route)