from .Storage import Storage

class Library:

    def __init__(self, songs, artists, albums, playlists):
        self.songs=Storage(songs).load()
        self.artists=Storage(artists).load()
        self.albums=Storage(albums).load()
        self.playlists=Storage(playlists).load()

    def add_element(self, file, info):
        lista=getattr(self, file)
        lista.append(info)
        return lista

    def remove_element(self, file, info):
        lista=getattr(self, file)
        lista.remove(info)
        return lista
        
    def search_element(self, file, name):
        lista=getattr(self, file)
        for item in lista:
            if ("name" in item and item['name']==name) or ('title' in item and item['title']==name):
                print('Found')
                print(item)
                return item
        print('Not found')
        return None
    
    def change_element(self, file, name, info):
        lista=getattr(self, file)
        for i, item in enumerate(lista):
            if ("name" in item and item['name']==name) or ('title' in item and item['title']==name):
                lista[i]=info
                return lista
        print('Not found')
        return lista

    def filter_elements(self, file:str, criteria:str, specific:str):
        lista=getattr(self, file)
        filtered=[]
        for item in lista:
            if (criteria in item and item[criteria]==specific):
                filtered.append(item)
        print('Results:')
        for i, j in enumerate(filtered,1):
            print(i, j)
        return filtered

    def save(self, file):
        lista=getattr(self, file)
        result_csv=Storage(file).export_csv(lista)
        result_json=Storage(file).save_json(lista)
        return result_csv, result_json