
#import pandas as pd
#import os
#from pathlib import Path
#import json


#json_file= Path(__file__).parent.parent/'data'/'albums.json'
#csv_file= Path(__file__).parent.parent/'data'/'albums.csv'

class Album():

    def __init__(self, title, duration, artist, genre, year, slist=None):
        self.title=title
        self.duration= duration
        self.artist= artist
        self.genre= genre
        self.slist=slist if slist is not None else []
        self.year=year
    
    def validate(self):
        if self.duration>0:
            if self.year>1800 and self.year<2026:
                if len(self.title)!=0 and len(self.artist)!=0 and len(self.genre)!=0:
                    print("Validated and OK")
                    return True
                else:
                    print("Validated and not OK")
            else:
                print("Validated and not OK")
                print("Year not OK")
        else:
            print("Validated and not OK")
            print("Duration not OK")
        return False
    
    def addsong(self, song):
        #title=input('What is the name of the song: ')
        #duration=float(input('What is the duration of the song in minutes?'))
        #genre=input('What is the genre?')
        #newsong=song(title, self.artist, genre, duration, self.title)

        self.slist.append(song)
        return

    def removesong(self, song):
        #if len(self.slist)!=0:
            #print('Which song do you want to remove?')
            #i=1
            #for song in self.slist:
             #   print(i, self.slist[i-1])
              #  i=+1
            #choice=int(input('Please choose the number: '))
            #self.slist=self.slist.remove(self.slist[choice-1])
        
        #else:
         #   print('There are no songs in this album')
        
        self.slist.remove(song)
        return self.slist

    def show(self):
        print( self.title, " by ", self.artist, ":")
        print("Year: ", self.year)
        print("Duration: ", self.duration)
        print("Genre: ", self.genre)
        print('This is the list of songs in the album:')
        for i, song in enumerate(self.slist, 1):
            print(i, song)#ver bien
        return
    
    def to_dict(self):
         return {
            'title': self.title,
            'duration':self.duration,
            'genre':self.genre,
            'artist':self.artist,
            'year': self.year,
            "slist": [song for song in self.slist]
        }
"""   
    def save_to_json(self):
            try:
                json_file.parent.mkdir(parents=True, exist_ok=True)
                if json_file.exists() and json_file.stat().st_size > 0:
                    with open(json_file, 'r', encoding='utf-8') as f:
                        try:
                            albums = json.load(f)
                        except json.JSONDecodeError:
                            albums = []
                else:
                    albums = []
    
                albums.append(self.to_dic())
                with open(json_file, 'w', encoding='utf-8') as f:
                    json.dump(albums, f, indent=2, ensure_ascii=False)

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
        return"""