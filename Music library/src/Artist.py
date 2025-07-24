#import pandas as pd
#import os
#from pathlib import Path
#import json

#json_file= Path(__file__).parent.parent/'data'/'artists.json'
#csv_file= Path(__file__).parent.parent/'data'/'artists.csv'

class Artist:

    def __init__(self, name, country, genre, albums=None):
        self.name=name
        self.country=country
        self.genre=genre
        self.albums=albums if albums is not None else []

    def add_album(self, album):
     
       # title=input('What is the name of the album: ')
        #duration=float(input('What is the duration of the album in minutes?'))
        #genre=input('What is the genre?')
        #year=int(input('What is the year of launch?'))

        #newalbum=album(title, duration, self.name, genre, year)

        #active=True
        #while active==True:
         #   choice=input('Do you want to add songs to the album?\n A. Yes  B. No')
          #  if choice=='A' or choice=='a' or choice=='B' or choice=='b':
           #     if choice=='a' or choice=='A':
            #        newalbum.addsong()
             #   else:
              #      active=False
            #else:
             #   print('Sorry, try again')
        self.albums.append(album)
        return

    def show(self):
        print(self.name)
        print("Country: ", self.country)
        print("Genre: ", self.genre)
        print("Albums: ")

        for i, album in enumerate(self.albums, 1):
            print(i, album)
        
        return 
            
    def to_dict(self):
        return {
            'Name': self.name,
            'Country':self.country,
            'Genre':self.genre,
            "Albums": [album for album in self.albums]
        }
    """
    def save_to_json(self):
            try:
                json_file.parent.mkdir(parents=True, exist_ok=True)
                if json_file.exists() and json_file.stat().st_size > 0:
                    with open(json_file, 'r', encoding='utf-8') as f:
                        try:
                            artists = json.load(f)
                        except json.JSONDecodeError:
                            artists = []
                else:
                    artists = []
    
                artists.append(self.to_dic())
                with open(json_file, 'w', encoding='utf-8') as f:
                    json.dump(artists, f, indent=2, ensure_ascii=False)

            except OSError:
                print("Error, could not open JSON file")
            return

    def save_to_csv(self):
        try: 
            header = not csv_file.exists() or os.stat(csv_file).st_size == 0
            df=pd.DataFrame([self.to_dic()])
            csv_file.parent.mkdir(parents=True, exist_ok=True)
            df.to_csv(csv_file,mode='a', header=header, index=False)
        except OSError: 
            print("Error, could not open CSV file")
        return
    
    """
