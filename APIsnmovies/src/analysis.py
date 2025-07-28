import pandas as pd
import re

def load_fav(path):
    df=pd.read_json(path)
    return df

def clean_data(df):
    df_clean=df[['Title', 'Runtime', 'Genre', 'Metascore', 'imdbRating', 'Type']].copy()
    #df_clean.loc[:,'Released']=pd.to_datetime(df_clean['Released'],format='%d %b %Y', errors='coerce')
    #df_clean = df_clean[df_clean['Released'].notna()]
    #df_clean.loc[:,'Released']=df_clean['Released'].dt.year
    for (i, row) in df_clean.iterrows():
        df_clean.loc[i, 'Genre']=row['Genre'].split(', ')
        match=re.search(r'\d+', row['Runtime'])
        if match:
            df_clean.loc[i, 'Runtime']=int(match.group())
    df_clean['Metascore'] = pd.to_numeric(df_clean['Metascore'], errors='coerce')
    df_clean['imdbRating'] = pd.to_numeric(df_clean['imdbRating'], errors='coerce')
    df_clean['Runtime'] = pd.to_numeric(df_clean['Runtime'], errors='coerce')

    return df_clean

def resume_data(df):
    return print(df.describe())

