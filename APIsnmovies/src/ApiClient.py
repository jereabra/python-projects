import requests
import logging

class ApiClient:

    def __init__(self, api_key) -> None:
        self.api_key=api_key
        self.timeout=5
        self.base_url='http://www.omdbapi.com/' #?apikey=[yourkey]&

    def search_title(self, title):
        params={'apikey':self.api_key, 't':title}
        logging.info(f'Starting search for {title}')
        try:
            resp= requests.get(self.base_url, params=params, timeout=self.timeout)
            resp.raise_for_status()
            logging.info(f'Succesfull search by the title {title}')
            data=resp.json()
            if data.get('Response')=='True':
                logging.info(f'{title} exists')
                return data
            else:
                logging.warning(f'No results in the research for {title}')
                return None
        except requests.RequestException as e:
            logging.error(f"Request error: {e}")
            return None
    
    def search_id(self, id):
        params={'apikey':self.api_key, 'i':id}
        logging.info(f'Starting search for {id}')
        try:
            resp= requests.get(self.base_url, params=params, timeout=self.timeout)
            resp.raise_for_status()
            logging.info(f'Succesfull search by the id {id}')
            data=resp.json()
            if data.get('Response')=='True':
                logging.info(f'{id} exists')
                return data
            else:
                logging.warning(f'No results in the research for {id}')
                return None
        except requests.RequestException as e:
            logging.error(f"Request error: {e}")
            return None
    
        
    def search_specifics(self, kword, page, type=None, year=None):
        params={'apikey':self.api_key, 's':kword, 'page':page}
        logging.info(f'Starting search for word {kword} from page {page}')
        if year is not None:
            params['y']=year
            logging.info(f'Searching for the year {year}')
        if type is not None:
            params['type']=type
            logging.info(f'Searching for {type}')
        try:
            resp= requests.get(self.base_url, params=params, timeout=self.timeout)
            resp.raise_for_status()
            logging.info(f'Succesfull search by the word {kword} in page {page}')
            data=resp.json()
            if data.get('Response')=='True':
                logging.info(f'{kword} in page {page} exists')
                return data
            else:
                logging.warning(f'No results in the research for {kword} in page {page}')
                return None
        except requests.RequestException as e:
            logging.error(f"Request error: {e}")
            return None
        
    def search_series(self, title=None, id=None, season=None, episode=None):
        if title is None and id is None:
            logging.error('No title or id')
            return None
        else:
            params={'apikey':self.api_key}
            if title is not None: params['t']=title
            if id is not None: params['i']=id
            logging.info(f'Searching for {title} ({id}):')
            if season is not None: 
                params['Season']=season
                logging.info(f'Searching for season {season}')
                if episode is not None: 
                    params['Episode']=episode
                    logging.info(f'Searching for episode {episode}')
            try:
                resp= requests.get(self.base_url, params=params, timeout=self.timeout)
                resp.raise_for_status()
                logging.info(f'Succesfull search for {title} ({id})')
                data=resp.json()
                if data.get('Response')=='True':
                    logging.info(f'{title} ({id}) exists with the especifications {params.get("Season")}:{params.get("Episode")}')
                    return data
                else:
                    logging.warning(f'No results in the search for {title} ({id}) with the especifications {params["season"]}:{params["episode"]}')
                    return None
            except requests.RequestException as e:
                logging.error(f"Request error: {e}")
                return None

            



    '''
        def  search_key_word(self, kword, page):
        params={'apikey':self.api_key, 's':kword, 'page':page}
        logging.info(f'Starting search for word {kword} from page {page}')
        try:
            resp= requests.get(self.base_url, params=params)
            resp.raise_for_status()
            logging.info(f'Succesfull search by the word {kword} in page {page}')
            data=resp.json()
            if data.get('Response')=='True':
                logging.info(f'{kword} in page {page} exists')
                return data
            else:
                logging.warning(f'No results in the research for {kword} in page{page}')
                return None
        except requests.RequestException as e:
            logging.error(f"Request error: {e}")
            return None
        '''