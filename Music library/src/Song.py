#from pathlib import Path
#import json
#import pandas as pd
#import os

#json_file= Path(__file__).parent.parent/'data'/'songs.json'
#csv_file= Path(__file__).parent.parent/'data'/'songs.csv'

class Song():

    def __init__(self, title, artist, genre, duration, album='Single'):
        self.title= title
        self.artist=artist
        self.genre=genre
        self.duration=duration
        self.album=album

    def validate(self):
        if self.duration>0:
            if len(self.title)!=0:
                    if len(self.artist)!=0:
                        print("Validated and OK")
                        return True
                    else:
                        print("Validate and not OK, there is no artist name")
            else:
                print("Validate and not OK, there is no title")
        else:
            print("Validate and not OK, there is no duration")
        return False

    def show(self):
        print(self.title, " by ", self.artist, ":")
        print("Album: ", self.album)
        print("Duration: ", self.duration)
        print("Genre: ", self.genre)

    def to_dict(self):
        return {
            'title': self.title,
            'duration': self.duration,
            'artist': self.artist,
            'genre': self.genre,
            'album':self.album
        }

"""   
    def save_to_json(self):
        try:
            json_file.parent.mkdir(parents=True, exist_ok=True)
            if json_file.exists() and json_file.stat().st_size > 0:
                with open(json_file, 'r', encoding='utf-8') as f:
                    try:
                        songs = json.load(f)
                    except json.JSONDecodeError:
                        songs = []
            else:
                songs = []
   
            songs.append(self.__dict__)
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(songs, f, indent=2, ensure_ascii=False)

        except OSError:
            print("Error, could not open JSON file")
        return

    def save_to_csv(self):
        try: 
            header = not csv_file.exists() or os.stat(csv_file).st_size == 0
            df=pd.DataFrame([self.__dict__])
            csv_file.parent.mkdir(parents=True, exist_ok=True)
            df.to_csv(csv_file,mode='a', header=header, index=False)
        except OSError: 
            print("Error, could not open CSV file")
        return
    
      """