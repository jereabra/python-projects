import random
import logging


def random_search():
    try:
        with open('../data/keywords.txt', 'r') as f:
            words=[line.strip() for line in f if line.strip() and not line.startswith('#')]
            kword=random.choice(words)
            logging.info('selected random word to search')
            return kword
    except OSError as e:
        logging.error(f'{e} not found any word')
        return 

def random_select(search_results):
    if not search_results:
        return None
    item=random.choice(search_results)
    title=item.get('Title')
    logging.info(f'{title} selected')
    return title

def random_season(item):
    number=item.get('totalSeasons')
    try:
        number=int(number)
    except (TypeError, ValueError):
        return 1
    return random.randint(1,number)

def quit():
    print('Thank you')
    logging.info('Closing program')
    return None

def select_choice(max_number):
    active=True
    while active:
        value=input('Select a choice, press x to exit\n')
        try:
            value=int(value)
            if value>max_number or value<=0:
                active=True
                logging.info('Client selected number out of the list')
            else:
                logging.info(f'Client selected number correctly: {value}')
                active=False
                return value
        except ValueError:
            logging.info('Client selected out of the list')
            if value=='x':
                logging.warning('Clients wants to exit')
                active=False
                return quit()
            active=True

def get_results_list(results):
    if isinstance(results, dict) and "Search" in results:
        return results["Search"]
    if isinstance(results, list):
        return results
    return []

