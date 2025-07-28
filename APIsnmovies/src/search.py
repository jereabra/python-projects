import logging

def search_title(results, title):
    logging.info(f'Searching {title} in results')
    for item in results:
        if item.get('Title').lower()==title.lower():
            logging.info(f'{title} found')
            return item
        else:
            pass
    logging.info(f'{title} not found')
    return None

def filter_genre(results, genre):
    logging.info(f'Looking for {genre} results')
    filtered=[]
    for item in results:
        if 'Genre' in item and genre.lower() in item.get('Genre').lower():
            filtered.append(item)
            logging.info(f'{item.get("Title")} added to filtered')
        else:
            pass
    logging.info('Filter finished')
    return filtered      
def filter_year(results, year):
    logging.info(f'Looking for results launched in {year}')
    filtered=[]
    for item in results:
        if 'Year' in item and item.get('Year')==year:
            filtered.append(item)
            logging.info(f'{item.get("Title")} added to filtered')
        else:
            pass
    logging.info('Filter finished')
    return filtered
def filter_type(results, type):
    logging.info(f'Looking for {type} results')
    filtered=[]
    for item in results:
        if 'Type' in item and type.lower() in item.get('Type').lower():
            filtered.append(item)
            logging.info(f'{item.get("Title")} added to filtered')
        else:
            pass
    logging.info('Filter finished')
    return filtered
def filter_actor(results, actor):
    logging.info(f'Looking for {actor} results')
    filtered=[]
    for item in results:
        if 'Actors' in item and actor.lower() in item.get('Actors').lower():
            filtered.append(item)
            logging.info(f'{item.get("Title")} added to filtered')
        else:
            pass
    logging.info('Filter finished')
    return filtered

def order_year(results, des=True):
    logging.info('Getting year')
    def extract_year(item):
        year_str=item.get('Year', '')
        if year_str.isdigit():
            return int(year_str)
        if year_str and year_str[:4].isdigit():
            return int(year_str[:4])
        return 0
    logging.info('Starting to order by year')
    return sorted(results, key=extract_year,reverse=des)
def order_rating(results):
    logging.info('Getting rating')
    def extract_rating(item):
        rating_str=item.get('imdbRating', '')
        if rating_str.isdigit():
            return float(rating_str)
        return 0
    
    logging.info('Starting to order by rating')
    return sorted(results, key=extract_rating)

def format_results(results):
    showing=[]
    logging.info('Starting to format results')
    for i,item in enumerate(results, 1):
        showing.append(f'{i}. {item.get("Title")} ({item.get("Year")})\nRating: {item.get("imdbRating")}\nGenre:{item.get("Genre")}\n\n')
    return showing
def format_title(item):
    showing=[]
    logging.info('Starting to format title')
    showing.append(f'{item.get("Title")} ({item.get("Year")})')
    showing.append(f'Written by {item.get("Writer")}')
    showing.append(f'Directed by {item.get("Director")}')
    showing.append(f'{item.get("Plot")}')
    showing.append(f'{item.get("Runtime")} of entretainment for those who like {item.get("Genre")} titles')
    #showing.append(f'Written by {item.get("Writer")}')
    showing.append(f'{item.get("imdbRating")}/10 according to imdb')
    return showing

def extract_title(results):
    new_results=[]
    logging.info('extracting titles')
    for item in results:
        new_results.append(item.get('Title'))
    logging.info(f'{len(new_results)} titles extracted')
    return new_results
def extract_actors(title):
    logging.info(f'extracting actors from {title}')
    actors=title.get('Actors')
    logging.info('extracted')
    return actors

def validate(results):
    logging.info('validating results')
    if isinstance(results, dict) and 'Search' in results and isinstance(results['Search'], list) and len(results['Search'])>0:
        logging.info('Results are search type')
        return True
    if isinstance(results, dict) and results.get('Response')=="True":
        logging.info('Validated')
        return True
    else:
        logging.warning('Results not validated')
        return False
    

