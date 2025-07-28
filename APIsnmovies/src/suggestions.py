import pandas as pd
from .ml_model import load_model, preprocessing

class Suggestion:
    def __init__(self, base_df, model_path):
        self.base_df=base_df
        self.model=load_model(model_path)

        return
        
    def recommend(self, favorites, mlb, n=5):
        favorites_pre,mlb2=preprocessing(favorites, mlb)
        suggestions=[]
        for i in favorites_pre.index:
            _, indexes=self.model.kneighbors([favorites_pre.loc[i]], n_neighbors=n+1)
            for idx in indexes[0]:
                title=self.base_df.iloc[idx]['Title']
                if title not in favorites['Title'].values:
                    suggestions.append(title)
        
        return list(set(suggestions))