import json
import pandas as pd
from pathlib import Path
import os
import logging


class Favorites:

    def __init__(self, client):
        self.client=client
        self.json_file=Path(__file__).parent.parent/'data'/(client+'.json')
        self.csv_file=Path(__file__).parent.parent/'data'/(client+'.csv')
        self.memory=self.load()

    def load(self):
        try:
            self.json_file.parent.mkdir(parents=True, exist_ok=True)
            if self.json_file.exists() and self.json_file.stat().st_size > 0:
                with open(self.json_file, 'r', encoding='utf-8') as f:
                    try:
                        elements = json.load(f)
                        logging.info('elements loaded from json file')
                    except json.JSONDecodeError as e:
                        elements = []
                        logging.warning(f'{e} : no elements loaded, starting from cero')
            else:
                elements = []
                logging.info('Creating file and starting from cero')
        except OSError:
            logging.error("Error, could not open JSON file")
            elements=[]
        return elements
    
    def save_csv(self):
        try:
            header = not self.csv_file.exists() or os.stat(self.csv_file).st_size == 0
            df=pd.DataFrame(self.memory)
            self.csv_file.parent.mkdir(parents=True, exist_ok=True)
            df.to_csv(self.csv_file,mode='a', header=header, index=False)
            logging.info('csv saved')
        except OSError: 
            logging.error("Error, could not open CSV file")
        return
    
    def save_json(self):
        try:
            with open(self.json_file, 'w', encoding='utf-8') as f:
                json.dump(self.memory, f, indent=2, ensure_ascii=False)
                logging.info('json file Saved')
        except OSError:
            logging.error("Error, could not open JSON file")
        return
    
    def save_all(self):
        self.save_csv()
        self.save_json()
        return
    
    def add_favorite(self, item):
        logging.info(f' adding {item.get("Title")} to {self.client} list')
        self.memory.append(item)
        logging.info('Added')
        return
    
    def remove_favorite(self, item):
        for fav in self.memory:
            if item.get('Title')==fav.get('Title'):
                self.memory.remove(fav)
                logging.info( f'{item.get("Title")} removed from {self.client} list')
                return 
        else:
            logging.error(f'{item.get("Title")} not in {self.client} list')
            return