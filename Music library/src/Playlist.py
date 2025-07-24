class Playlist:


    def __init__(self, name, songs=None):
        self.name=name
        self.songs=songs if songs is not None else []


    def addsong(self, song):
      #  title=input('What is the name of the song: ')
       # duration=float(input('What is the duration of the song in minutes?'))
        #genre=input('What is the genre?')
        #newsong=song(title, self.artist, genre, duration, self.title)
        self.songs.append(song)
        return self.songs

    def removesong(self, song):
        #if len(self.slist)!=0:
         #   print('Which song do you want to remove?')
          #  i=1
           # for song in self.slist:
            #    print(i, self.slist[i-1])
             #   i=+1
            #choice=int(input('Please choose the number: '))
            #self.songs=self.songs.remove(self.songs[choice-1])
        
       # else:
        #    print('There are no songs in this playlist')
        self.songs.remove(song)
        return self.songs

    def show(self):
        print("Title: ", self.name)
        print('This is the list of songs in the playlist:')
        for i, song in enumerate(self.songs, 1):
            print(i, song)
                    
        return
    
    def to_dict(self):
         return {
            'name': self.name,
            "songs": [song.to_dict() for song in self.songs]
        }