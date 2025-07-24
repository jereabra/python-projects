from .Library import Library
from .Song import Song
from .Album import Album
from .Artist import Artist
from .Playlist import Playlist

def main():
    lib=Library('songs', 'artists', 'albums', 'playlists')
    print('welcome to the music library')
    while True:
        print('What would you like to do?')
        print('1. Add a song, playlist, album or artist')
        print('2. Remove a song, playlist, album or artist')
        print('3. Modify a song, playlist, album or artist')
        print('4. Search for a specific song, playlist, album or artist')
        print('5. Search for different songs, playlists, albums or artists')
        print('6. Save and close')
        while True:
            try:
                choose = int(input('Select a number from the list: '))
                break
            except ValueError:
                print("Please enter a valid number.")

        if choose==1:
            active=True
            while active:
                print('What would you like to add?')
                print('1. Song\n2. Album\n3. Artist\n4. Playlist')
                while True:
                    try:
                        subchoose= int(input('Select a number from the list'))
                        break
                    except ValueError:
                        print("Please enter a valid number.")
                if subchoose==1:
                    loop=True
                    while loop:
                        name=input('What is the name of the song?')
                        artist=input('What is the name of the artist?')
                        album=input('What is the name of the album?')
                        genre=input('What is the genre?')
                        while True:
                            try:
                                duration=float(input('what is the duration of the song in minuts?'))
                                break
                            except ValueError:
                                print('Please enter a valid number')
                        new_song=Song(name, artist, genre, duration, album)
                        if new_song.validate()==True:
                            lib.add_element('songs', new_song.to_dict())
                            print('New song added to library')
                            existing_album=lib.search_element('albums', album)
                            if existing_album is not None:
                                existing_album=Album(album, existing_album['duration'], existing_album['artist'], existing_album['genre'],  existing_album['year'], existing_album['slist'])
                                existing_album.addsong(new_song)
                                print('song added to album')
                                existing_album.show()
                            else:
                                loop2=True
                                p=input('If you want to create the album press 1')
                                if p=='1':
                                    while loop2:
                                        print('complete the data')   
                                        name=input('What is the name of the album?')
                                        artist=input('What is the name of the artist?')
                                        while True:
                                            try:
                                                year=int(input('What is the year of the album?'))
                                                break
                                            except ValueError:
                                                print("Please enter a valid number.")
                                        genre=input('What is the genre?')
                                        while True:    
                                            try:
                                                duration=float(input('what is the duration of the song in minuts?'))
                                                break
                                            except ValueError:
                                              print('Please enter a valid number')
                                        new_album=Album(name, duration, artist, genre, year, [new_song])
                                        if new_album.validate()==True:
                                            lib.add_element('albums', new_album.to_dict())
                                            print('Album created and song added')
                                            loop2=False
                                        else:
                                            print('Try again')
                                            loop2=True 
                            
                            q=input('If you want to add another song press 1')
                            if q=='1':
                                continue
                            else:
                                print('Thank you')
                                loop=False
                                active=False
                        else:
                            loop=True         
                        active=False        
                if subchoose==2:
                    loop=True
                    while loop:
                        name=input('What is the name of the album?')
                        artist=input('What is the name of the artist?')
                        while True:
                            try:
                                year=int(input('What is the year of the album?'))
                                break
                            except ValueError:
                                print('Please enter a valid number')
                        genre=input('What is the genre?')
                        while True:
                            try:
                                duration=float(input('what is the duration of the song in minuts?'))
                                break
                            except:
                                print('Please enter a valid number')
                        new_album=Album(name, duration, artist, genre, year)
                        if new_album.validate()==True:
                            #Añadir canciones?
                            loop2=True
                            while loop2:
                                    q=input('If you want to add a song press 1')
                                    if q=='1':
                                        name2=input('What is the name of the song?')
                                        if lib.search_element('songs', name2) is not None:
                                            new_album.addsong(name2)
                                        else: 
                                            loop3=True
                                            while loop3:  
                                                artist=input('What is the name of the artist?')
                                                genre=input('What is the genre?')
                                                while True:
                                                    try:
                                                        duration=float(input('what is the duration of the song in minuts?'))
                                                        break
                                                    except ValueError:
                                                        print('Please enter a valid number')
                                                new_song=Song(name2, artist, genre, duration, name)
                                                new_song.validate()
                                                if new_song.validate()==True:
                                                    lib.add_element('songs', new_song.to_dict())
                                                    print('New song added to library') 
                                                    new_album.addsong(name2)    
                                                    loop3=False  
                                                else:                                                
                                                    loop3=True
                                    else:
                                        loop2=False
                        else:
                            loop=True 
                        
                        #añadir album
                        lib.add_element('albums', new_album.to_dict())
                        print('Album added succesfully')
                        new_album.show()
                        existing_artist=lib.search_element('artists', artist)
                        if existing_artist is not None:
                            existing_artist=Artist(artist, existing_artist['country'], existing_artist['genre'], existing_artist['albums'])
                            existing_artist.add_album(name)
                            print('album added to artist')
                            existing_artist.show()
                        else:
                            new_artist=Artist(artist, 'Uknown', 'Unknown',  albums=[name])
                        loop=False
                        active=False
                if subchoose==3:
                    name=input('What is the name of the artist?')
                    country=input('Where is the artist from?')
                    genre=input('What is the genre?')
                    new_artist=Artist(name, country, genre)
                    q=input('Press 1 if you want to add albums to the artist')
                    if q=='1':
                        print('complete the data')   
                        album=input('What is the name of the album?')
                        existing_album=lib.search_element('albums', album)
                        if existing_album is not None:
                            existing_album=Album(album, existing_album['duration'], existing_album['artist'], existing_album['genre'],  existing_album['year'], existing_album['slist'])
                            new_artist.add_album(album)
                            print('album added to artist')
                            existing_album.show()
                        
                        else:
                            loop2=True
                            while loop2:
                                while True:
                                    try:
                                        year=int(input('What is the year of the album?'))
                                        break
                                    except ValueError:
                                        print('Please enter a valid number')
                                genre=input('What is the genre?')
                                while True:
                                    try:
                                        duration=float(input('what is the duration of the song in minuts?'))
                                        break
                                    except ValueError:
                                        print('Please enter a valid number')
                                new_album=Album(album, duration, new_artist, genre, year)
                                if new_album.validate()==True:
                                    lib.add_element('albums', new_album.to_dict())
                                    new_artist.add_album(album)
                                    print('Album created and added to artist')
                                    loop2=False
                                else:
                                    print('Try again')
                                    loop2=True 
                    lib.add_element('artists', new_artist.to_dict())
                    print('artist added')    
                    active=False        
                if subchoose==4:
                    name=input('What is the name of the new playlist')
                    new_playlist=Playlist(name)
                    loop=True
                    while loop:
                        q=input('Press 1 if you want to add a song')
                        if q=='1':
                            print('This is the list of songs')
                            for i, song in enumerate(lib.songs,1): print(i, song['title'])
                            song1=input('what is the name of the song?')
                            if lib.search_element('songs', song1) is not None:
                                new_playlist.addsong(song1)
                            else:
                                print('Song not found in library')
                        else: loop=False
                    
                    lib.add_element('playlists', new_playlist.to_dict())
                    print('Playlist added')
                    new_playlist.show()
                    active=False
                else:
                    print('select one of the options')
                    active=True


        if choose==2:
            active=True
            while active:
                print('What would you like to Remove?')
                print('1. Song\n2. Album\n3. Artist\n4. Playlist')
                while True:
                    try:
                        subchoose= int(input('Select a number from the list'))
                        break
                    except ValueError:
                        print('Please enter a valid number')
                if subchoose==1:
                    print('These are the songs in library:')
                    for i, song in enumerate(lib.songs,1): print(i, song['title'])
                    loop=True
                    while loop:
                        name=input('What is the name of the song you want to remove?')
                        song_to_remove=lib.search_element('songs', name)
                        if song_to_remove is not None:
                            lib.remove_element('songs', song_to_remove )
                            print('Song removed')
                            for i, song in enumerate(lib.songs,1): print(i, song['title'])
                            loop=False
                            active=False
                        else:
                            print('song not found')
                            loop=True
                if subchoose==2:
                    print('These are the albums in library:')
                    for i, album in enumerate(lib.albums,1): print(i, album['title'])
                    loop=True
                    while loop:
                        name=input('What is the name of the album you want to remove?')
                        album_to_remove=lib.search_element('albums', name)
                        if album_to_remove is not None:
                            lib.remove_element('albums', album_to_remove )
                            print('album removed')
                            for i, album in enumerate(lib.albums,1): print(i, album['title'])
                            loop=False
                            active=False
                        else:
                            print('album not found')
                            loop=True
                if subchoose==3:
                    print('These are the artists in library:')
                    for i, artist in enumerate(lib.artists,1): print(i, artist['name'])
                    loop=True
                    while loop:
                        name=input('What is the name of the artist you want to remove?')
                        artist_to_remove=lib.search_element('artists', name)
                        if artist_to_remove is not None:
                            lib.remove_element('artists', artist_to_remove )
                            print('Artist removed')
                            for i, artist in enumerate(lib.artists,1): print(i, artist['name'])
                            loop=False
                            active=False
                        else:
                            print('Artist not found')
                            loop=True
                if subchoose==4:
                    print('These are the playlists in library:')
                    for i, playlist in enumerate(lib.playlists,1): print(i, playlist['name'])
                    loop=True
                    while loop:
                        name=input('What is the name of the playlist you want to remove?')
                        pl_to_remove=lib.search_element('playlists', name)
                        if pl_to_remove is not None:
                            lib.remove_element('playlists', pl_to_remove )
                            print('playlist removed')
                            for i, playlist in enumerate(lib.playlists,1): print(i, playlist['name'])
                            loop=False
                            active=False
                        else:
                            print('playlist not found')
                            loop=True
                else:
                    print('select one of the options')
                    active=True
            
        if choose==3:
            active=True
            while active:
                print('What would you like to modify?')
                print('1. Song\n2. Album\n3. Artist\n4. Playlist')
                while True:
                    try:
                        subchoose= int(input('Select a number from the list'))
                        break
                    except ValueError:
                        print('Please enter a valid number')
                if subchoose==1:
                    print('These are the songs in library:')
                    for i, song in enumerate(lib.songs,1): print(i, song['title'])
                    loop=True
                    while loop:
                        name=input('What is the name of the song you want to modify?')
                        song_to_modify=lib.search_element('songs', name)
                        if song_to_modify is not None:
                            loop2=True
                            info=Song(song_to_modify['title'], song_to_modify['artist'], song_to_modify['genre'], song_to_modify['duration'], song_to_modify['album'])
                            while loop2:
                                while True:
                                    try:
                                        q=int(input('What do you want to change?\n1.Title\n2.Album\n3.Artist\n4.Duration\n5.Genre'))
                                        break
                                    except ValueError:
                                        print('Please enter a valid number')

                                if q==1:
                                    new_name=input('What is the new name?\n')
                                    info.title=new_name
                                    if info.validate()==True: loop2=False
                                    else: info.title=song_to_modify['title']; print('not modify')
                                if q==2:
                                    new_album=input('What is the new album?\n')
                                    info.album=new_album
                                    if info.validate()==True: loop2=False
                                    else: info.album=song_to_modify['album']; print('not modify')
                                if q==3:
                                    new_artist=input('What is the new Artist?\n')
                                    info.artist=new_artist
                                    if info.validate()==True: loop2=False
                                    else: info.artist=song_to_modify['artist']; print('not modify')
                                if q==4:
                                    while True:
                                        try:
                                            new_duration=float(input('What is the new duration?\n'))
                                            break
                                        except ValueError:
                                            print('Please enter a valid number')
                                    info.duration=new_duration
                                    if info.validate()==True: loop2=False
                                    else: info.duration=song_to_modify['duration']; print('not modify')                               
                                if q==5:
                                    new_genre=input('What is the new genre?\n')
                                    info.genre=new_genre
                                    loop2=False    
                                else:
                                    print('Select a choice')
                           
                            lib.change_element('songs', song_to_modify, info)
                            print('Song modified')
                            loop=False
                            active=False
                        else:
                            print('song not found')
                            loop=True
                if subchoose==2:
                    name=input('What is the name of the album you want to modify?')
                    album_to_modify=lib.search_element('albums', name)
                    if album_to_modify is not None:
                            loop2=True
                            info=Album(album_to_modify['title'], album_to_modify['duration'], album_to_modify['artist'], album_to_modify['genre'], album_to_modify['year'], album_to_modify['slist'])
                            while loop2:
                                q=input('What do you want to change?\n1.Title\n2.Year\n3.Artist\n4.Duration\n5.Genre')
                                if q=='1':
                                    new_name=input('What is the new title?\n')
                                    info.title=new_name
                                    if info.validate()==True: loop2=False
                                    else: info.title=album_to_modify['title']; print('not modify')
                                if q=='2':
                                    while True:
                                        try:
                                            new_year=int(input('What is the new album?\n'))
                                            break
                                        except ValueError:
                                            print('Please enter a valid year')
                                    info.year=new_year
                                    if info.validate()==True: loop2=False
                                    else: info.year=album_to_modify['year']; print('not modify')
                                if q=='3':
                                    new_artist=input('What is the new Artist?\n')
                                    info.artist=new_artist
                                    if info.validate()==True: loop2=False
                                    else: info.artist=album_to_modify['artist']; print('not modify')
                                if q=='4':
                                    while True:
                                        try:
                                            new_duration=float(input('What is the new duration?\n'))
                                            break
                                        except ValueError:
                                            print('Please enter a valid number')
                                    info.duration=new_duration
                                    if info.validate()==True: loop2=False
                                    else: info.duration=album_to_modify['duration']; print('not modify')                               
                                if q=='5':
                                    new_genre=input('What is the new genre?\n')
                                    info.genre=new_genre
                                    loop2=False    
                                else:
                                    print('Select a choice')
                           
                            lib.change_element('albums', album_to_modify, info)
                            print('album modified')
                            loop=False
                            active=False
                    else:
                        print('album not found')
                        loop=True     
                if subchoose==3:
                    name=input('What is the name of the artist you want to modify?')
                    artist_to_modify=lib.search_element('artists', name)
                    if artist_to_modify is not None:
                            loop2=True
                            info=Artist(artist_to_modify['name'], artist_to_modify['country'], artist_to_modify['genre'], artist_to_modify['albums'])
                            while loop2:
                                q=input('What do you want to change?\n1.Name\n2.Country\n3.Genre')
                                if q=='1':
                                    new_name=input('What is the new name?\n')
                                    info.name=new_name
                                    loop2=False
                                if q=='2':
                                    new_country=input('What is the new country?\n')
                                    info.country=new_country
                                    loop2=False
                                if q=='3':
                                    new_genre=input('What is the new genre?\n')
                                    info.genre=new_genre
                                    loop2=False 
                                else:
                                    print('Select a choice')
                           
                            lib.change_element('artists', artist_to_modify, info)
                            print('artist modified')
                            loop=False
                            active=False
                    else:
                        print('artist not found')
                        loop=True
                if subchoose==4:
                    name=input('What is the name of the playlist you want to modify?')
                    playlist_to_modify=lib.search_element('playlists', name)
                    if playlist_to_modify is not None:
                            loop2=True
                            info=Playlist(playlist_to_modify['name'], playlist_to_modify['songs'])
                            while loop2:
                                q=input('What do you want to do?\n1.Change name\n2.Add a song\n3.Remove a song')
                                if q=='1':
                                    new_name=input('What is the new name?\n')
                                    info.name=new_name
                                    loop2=False
                                if q=='2':
                                    loop3=True
                                    while loop3:
                                        print('These are the songs in the library:')
                                        for i, song in enumerate(lib.songs,1): print(i, song['title'])
                                        new_song=(input('What is the new song?\n'))
                                        new=lib.search_element('songs', new_song)
                                        if new is not None:
                                            info.addsong(new_song)
                                            loop3=False
                                            loop2=False
                                        else:
                                            print('Not an option')
                                            loop3=True
                                if q=='3':
                                    print('These are the songs in the playlist:')
                                    for i, song in enumerate(info.songs,1): print(i, song)
                                    loop3=True
                                    while loop:
                                        name2=input('What is the name of the song you want to remove?')
                                        song_to_remove=lib.search_element('songs', name2)
                                        if song_to_remove is not None:
                                            info.removesong(name2)
                                            print('Song removed')
                                            loop3=False
                                            loop2=False
                                        else:
                                            print('Not an option')
                                            loop3=True
                                else:
                                    print('Select a choice')
                           
                            lib.change_element('playlists', playlist_to_modify, info)
                            print('playlist modified')
                            loop=False
                            active=False
                    else:
                        print('playlist not found')
                        loop=True
                else:
                    print('select one of the options')
                    active=True

        if choose==4:
            loop=True
            while loop:
                print('What would you like to search?')
                print('1. Song\n2. Album\n3. Artist\n4. Playlist')
                while True:
                    try:
                        subchoose= int(input('Select a number from the list'))
                        break
                    except ValueError:
                        print('Please enter a valid number')
                if subchoose==1:
                    title=input('What is the title of the song')
                    search=lib.search_element('songs', title)
                    if search is not None:
                        show=Song(search['title'], search['artist'], search['genre'], search['duration'], search['album'])
                        show.show()
                    else:
                        print('Not found')
                    loop=False
                if subchoose==2:
                    title=input('What is the title of the album')
                    search=lib.search_element('albums', title)
                    if search is not None:
                        show=Album(search['title'], search['duration'], search['artist'], search['genre'], search['year'], search['slist'])
                        show.show()
                    else:
                        print('not found')
                    loop=False
                if subchoose==3:
                    title=input('What is the name of the artist')
                    search=lib.search_element('artists', title)
                    if search is not None:
                        show=Artist(search['name'], search['country'], search['genre'], search['albums'])
                        show.show()
                    else:
                        print('not found')
                    loop=False              
                if subchoose==4:
                    title=input('What is the name of the playlist')
                    search=lib.search_element('playlists', title)
                    if search is not None:
                        show=Playlist(search['name'], search['songs'])
                        show.show()
                    else:
                        print('not found')
                    loop=False
            else:
                print('select a choice')
                loop=True
        
        if choose==5:
            loop=True
            while loop:
                print('What would you like to filter?')
                print('1. Song\n2. Album\n3. Artist\n')
                while True:
                    try:
                        subchoose= int(input('Select a number from the list'))
                        break
                    except ValueError:
                        print('Please enter a valid number')
                if subchoose==1:
                    loop2=True
                    while loop2:
                        cri=input('select the criteria:\n1.Artist  2.Genre')
                        if cri=='1':
                            specific=input('Name of the artist')
                            lib.filter_elements('songs', 'artist', specific)
                            loop2=False
                            loop=False
                        if cri=='2':
                            specific=input('Name of the genre')
                            lib.filter_elements('songs', 'genre', specific)
                            loop2=False
                            loop=False
                        else:
                            print('select an option')          
                if subchoose==2:
                    loop2=True
                    while loop2:
                        cri=input('select the criteria:\n1.Artist  2.Genre')
                        if cri=='1':
                            specific=input('Name of the artist')
                            lib.filter_elements('albums', 'artist', specific)
                            loop2=False
                            loop=False
                        if cri=='2':
                            specific=input('Name of the genre')
                            lib.filter_elements('albums', 'genre', specific)
                            loop2=False
                            loop=False
                        else:
                            print('select an option')   
                if subchoose==3:
                    loop2=True
                    while loop2:
                        cri=input('select the criteria:\n1.Country  2.Genre')
                        if cri=='1':
                            specific=input('Name of the country')
                            lib.filter_elements('artists', 'country', specific)
                            loop2=False
                            loop=False
                        if cri=='2':
                            specific=input('Name of the genre')
                            lib.filter_elements('artists', 'genre', specific)
                            loop2=False
                            loop=False
                        else:
                            print('select an option')   
                else:
                    print('select a choice')
                    loop=True

        if choose==6:
            print('Thank you')
            lib.save('songs')
            lib.save('artists')
            lib.save('albums')
            lib.save('playlists')
            active=False

        else:
            print('select a choice')
            active=True

        
if __name__=='__main__':
    main()

