import json
import pandas as pd
from pathlib import Path
import os

class Storage:

    def __init__(self, file):
        self.file=file
        self.json_file= Path(__file__).parent.parent/'data'/(file+'.json')
        self.csv_file= Path(__file__).parent.parent/'data'/(file+'.csv')
       
    def load(self):
        try:
            self.json_file.parent.mkdir(parents=True, exist_ok=True)
            if self.json_file.exists() and self.json_file.stat().st_size > 0:
                with open(self.json_file, 'r', encoding='utf-8') as f:
                    try:
                        elements = json.load(f)
                    except json.JSONDecodeError:
                        elements = []
            else:
                elements = []
        except OSError:
            print("Error, could not open JSON file")
        return elements
        
    def export_csv(self, list):
        try:
            header = not self.csv_file.exists() or os.stat(self.csv_file).st_size == 0
            df=pd.DataFrame(list)
            self.csv_file.parent.mkdir(parents=True, exist_ok=True)
            df.to_csv(self.csv_file,mode='a', header=header, index=False)
            print('Saved')
        except OSError: 
            print("Error, could not open CSV file")
        return
    
    def save_json(self, list):
        try:
            with open(self.json_file, 'w', encoding='utf-8') as f:
                json.dump(list, f, indent=2, ensure_ascii=False)
                print('Saved')
        except OSError:
            print("Error, could not open JSON file")
        return
    
    

    