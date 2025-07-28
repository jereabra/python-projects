import logging
from .ApiClient import ApiClient
from .Favorites import Favorites
from . import utils as u
from . import search as s
import os
from dotenv import load_dotenv


#configuración

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

os.makedirs(DATA_DIR, exist_ok=True)

log_path = os.path.join(DATA_DIR, 'logs.log')
logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def main():
    #Configuro api
    load_dotenv()
    api_key=os.getenv("OMDB_API_KEY")
    if not api_key:
        logging.error('There is not api key in .env')
        exit()
    client=ApiClient(api_key)

    #Configuro usuario
    while True:
        name=input('What is your username: \n')
        try:
            user=Favorites(name)
            logging.info(f'{name} correct')
            #user_fav=user.load()  para que cargarlo si lo hace el mismo codigo de favorite
            break
        except OSError:
            logging.error(f'username {name} not possible')

    #Configuro historial 
    history_titles=Favorites('history_titles')
    history_searches=Favorites('history_searches')
    #history.load()
    print(f'Hi {name}, welcome to the movie data base')

    while True:
        print('What do you want to do today?')
        print('1. Search for a specific title or IMDB id')
        print('2. Search for different titles')
        print('3. My favorites')
        print('4. My history')
        choice=u.select_choice(4)

        if choice==1:
            print('1. I have the title')
            print('2. I have the IMDB id')
            print('3. I am looking for a specific TV show')
            print('4. I want a random title')
            subchoice= u.select_choice(4)
            if subchoice==1:
                #active=True
                while True:
                    title=input('What is the title?\n')
                    result=client.search_title(title)
                    if s.validate(result) and result is not None:
                        lines=s.format_title(result)
                        print('This is the result:\n\n')
                        for line in lines: print(line)
                        history_titles.add_favorite(result)
                        print('How do you want to continue?')
                        print('1. Add to favorite')
                        print('2. Look for actors')
                        print('3. Search for another title')
                        subchoice2=u.select_choice(3)
                        if subchoice2==1:
                            if all(item.get('Title') != result.get('Title') for item in user.memory):
                                user.add_favorite(result)
                                print('Done!')
                            break
                        if subchoice2==2:
                            actors=s.extract_actors(result)
                            print(actors)
                            print('Done!')
                            break
                        if subchoice2==3:
                            continue
                        if subchoice2==None:
                            break
                    else: 
                        print('Not found')
                        print('Thank you')
                        break                    
                print('Thank you')
            if subchoice==2:
                while True:
                    id=input('What is the id?\n')
                    result=client.search_id(id)
                    if s.validate(result) and result is not None:
                        lines=s.format_title(result)
                        for line in lines: print(line)
                        history_titles.add_favorite(result)
                        print('How do you want to continue?')
                        print('1. Add to favorite')
                        print('2. Look for actors')
                        print('3. Search for another title')
                        subchoice2=u.select_choice(3)
                        if subchoice2==1:
                            if all(item.get('Title') != result.get('Title') for item in user.memory):
                                user.add_favorite(result)
                            print('Done!')
                            break
                        if subchoice2==2:
                            actors=s.extract_actors(result)
                            print(actors)
                            print('Done!')
                            break
                        if subchoice2==3:
                            continue
                        if subchoice2==None:
                            break
                    else: 
                        print('Not found')
                        print('Thank you')
                        break
                print('Thank you')
            if subchoice==3:
                while True:
                    title=input('What is the title?\n')
                    season=input('What season are you looking for? If you are not looking press any letter\n')
                    try:
                        season_int=int(season)
                        episode=input('What episode are you looking for? If you are not looking press any letter\n')
                        try:
                            episode_int=int(episode)
                            result=client.search_series(title=title, season=season_int, episode=episode_int)
                        except ValueError:
                            episode_int=None
                            result=client.search_series(title=title, season=season_int)
                    except ValueError:
                        if season.lower=='random':
                            result=client.search_series(title=title)
                            season_int=u.random_season
                            episode_int=None
                            result=client.search_series(title=title, season=season_int)
                        else:
                            season_int=None
                            episode_int=None
                            result=client.search_series(title=title)

                    if s.validate(result) and result is not None:
                        if (episode_int is not None) or season_int is None:
                            lines=s.format_title(result)
                            for line in lines: print(line)
                            history_titles.add_favorite(result)
                            print('How do you want to continue?')
                            print('1. Add to favorite')
                            print('2. Look for actors')
                            print('3. Search for another title')
                            subchoice2=u.select_choice(3)
                            if subchoice2==1:
                                if all(item.get('Title') != result.get('Title') for item in user.memory):
                                    user.add_favorite(result)
                                print('Done!')
                                break
                            if subchoice2==2:
                                actors=s.extract_actors(result)
                                print(actors)
                                print('Done!')
                                break
                            if subchoice2==3:
                                continue
                            if subchoice2==None:
                                break
                            print('Thank you')     
                        else:
                            lines=s.format_results(u.get_results_list(result))      
                            history_searches.add_favorite(result) 
                            for line in lines: print(line)
                            print('How do you want to continue?')
                            print('1. Search for another title')
                            print('2. Expand a particular episode')
                            print('3. Select random')
                            subchoice2=u.select_choice(2)

                            if subchoice2==1:
                                continue
                            if subchoice2==2:
                                episode=input('What episode are you looking for? If you are not looking press any letter')
                                try:
                                    episode_int=int(episode)
                                    result=client.search_series(title=title, season=season_int, episode=episode_int)
                                    if s.validate(result)==True and result is not None:
                                        history_titles.add_favorite(result)
                                        lines=s.format_title(result)
                                        for line in lines: print(line)
                                        print('How do you want to continue?')
                                        print('1. Add to favorite')
                                        print('2. Look for actors')
                                        print('3. Search for another title')
                                        subchoice2=u.select_choice(3)
                                        if subchoice2==1:
                                            if all(item.get('Title') != result.get('Title') for item in user.memory):
                                                user.add_favorite(result)
                                            print('Done!')
                                            break
                                        if subchoice2==2:
                                            actors=s.extract_actors(result)
                                            print(actors)
                                            print('Done!')
                                            break
                                        if subchoice2==3:
                                            continue
                                        if subchoice2==None:
                                            break
                                        print('Thank you')
                                    else: 
                                        print('Not found')
                                        print('Thank you')
                                        break
                                except ValueError:
                                    episode_int=None
                                    print('Thank you')
                                    break                
                    else: 
                        print('Not found')
                        print('Thank you')
                        break
                            
            if subchoice==4:
                print('Looking for a random title')
                genre=input('What genre do you want?')
                while True:
                    kword=u.random_search()
                    results=client.search_specifics(kword, 1)
                    new_result=u.random_select(results)
                    new_results=s.filter_genre(new_result,genre if genre is not None else 'Action')
                    final_result=client.search_title(new_result)
                    if s.validate(final_result) and final_result is not None:
                        lines=s.format_title(final_result)
                        for line in lines: print(line)
                        history_titles.add_favorite(final_result)
                        print('How do you want to continue?')
                        print('1. Add to favorite')
                        print('2. Look for actors')
                        print('3. Search for another random title')
                        subchoice2=u.select_choice(3)
                        if subchoice2==1:
                            if all(item.get('Title') != final_result.get('Title') for item in user.memory):
                                user.add_favorite(result)
                            print('Done!')
                            break
                        if subchoice2==2:
                            actors=s.extract_actors(result)
                            print(actors)
                            print('Done!')
                            break
                        if subchoice2==3:
                            continue
                        if subchoice2==None:
                            break
                    else: 
                        continue
                        
                print('Thank you')

        if choice==2:
            while True:
                kword=input('What titles are you looking for?\n')
                print('What type are you looking for?\n1. Movies\n2. Series\n3. Games\n4. Nothing particular')
                type_choice=u.select_choice(4)
                if type_choice==1:type='movie'
                elif type_choice==2:type='series'
                elif type_choice==3:type='game'
                elif type_choice==4:type=None
                else: break
                while True:
                    print('What year are you looking for? press any letter if you do not want to add a year')
                    year=input()
                    try:
                        year_int=int(year)
                        if year_int>1900 and year_int<2026:
                            break
                        else:
                            print('Try again')
                    except ValueError:
                        year_int=None
                        break
                page=1
                results=[]
                items=client.search_specifics(kword, page=page, type=type, year=year_int)
                if items is not None and 'Search' in items:
                    if s.validate(items):
                        results.extend(items.get('Search', []))
                        total_results=int(items.get('totalResults',0))
                        total_pages=int(total_results/10)
                        for page in range(2, total_pages): 
                            items=client.search_specifics(kword, page=page, type=type, year=year_int)
                            if items is not None and 'Search' in items:
                                if s.validate(items):
                                    results.extend(items.get('Search', []))
                                else:break
                            else:
                                print('Not found')
                                print('Thank you')
                    else:
                        print('Not found')
                        print('Thank you')
                        #page=+1
                else:
                    print('Not found')
                    print('Thank you')
                
                #if s.validate(results):
                    #titles_found=s.extract_title(results)
                    #for title in titles_found:
                    #    history_searches.add_favorite(client.search_title(title))
                get_results=u.get_results_list(results)
                titles=s.extract_title(get_results)
                expanded_results=[]
                for title in titles:
                    result=client.search_title(title)
                    if result is not None:
                        expanded_results.append(result)
                        history_searches.add_favorite(result)
                    else:
                        logging.warning(f"No data found for title: {title}")
                expanded_results = [r for r in expanded_results if isinstance(r, dict)]
                ordered_results=s.order_rating(expanded_results)#rating
                lines=s.format_results(ordered_results[:20])
                print(f'These are the results for {kword} ordered by rating\n')
                for line in lines: print(line)
                print('\n')
                while True:
                    print('What do you want to do next?')
                    print('1. Order by year')
                    print('2. See more results')
                    print('3. Filter results')
                    print('4. Expand a title')
                    print('5. Search title')
                    print('6. Continue searching')
                    subchoice=u.select_choice(6)
                    if subchoice==1:
                        ordered_results=s.order_year(expanded_results)#year
                        new_lines=s.format_results(ordered_results[:20])
                        print(f'These are the results for {kword} ordered by year\n')
                        for line in new_lines: print(line)    
                    elif subchoice==2:
                        print('Here you have more results')
                        more_lines=s.format_results(ordered_results[20:40])
                        print(f'Here you have more results for {kword}')
                        for line in more_lines: print(line)
                        print('Do you want to see more results?')
                        print('1. Yes')
                        print('2. No')
                        subchoice=u.select_choice(2)
                        if subchoice==1:
                            print('Here you have more results')
                            more_lines=s.format_results(ordered_results[40:])
                            print(f'Here you have more results for {kword}')
                            for line in more_lines: print(line)
                            else: continue    
                    elif subchoice==3:
                        print('What is the criteria?')
                        print('1. Genre')
                        print('2. Year')
                        print('3. Type')
                        print('4. Actor')
                        subchoice2=u.select_choice(4)
                        if subchoice2==2 or subchoice2==3:
                            if subchoice2==2:
                                while True:
                                    year=input('What year are you looking for?\n')
                                    try:
                                        year_int=int(year)
                                        if year_int<1900 or year_int>2026:
                                            print('Try again')
                                        else:
                                            filter_results=s.filter_year(expanded_results, year_int)
                                            break
                                    except ValueError:
                                        filter_results=expanded_results
                                        print('No criteria found, giving results back')
                                        break
                            if subchoice2==3:
                                print('What type are you looking for?\n1. Movies\n2. Series\n3. Games\n')
                                type_choice=u.select_choice(4)
                                if type_choice==None: 
                                    filter_results=expanded_results
                                    print('No criteria found, giving results back')
                                elif type_choice==1:filter_results=s.filter_type(expanded_results, 'movie')
                                elif type_choice==2:filter_results=s.filter_type(expanded_results, 'series')
                                elif type_choice==3:filter_results=s.filter_type(expanded_results, 'game')
                            
                        if subchoice2==1 or subchoice2==4:
                            while True:
                                if subchoice2==1:
                                    genre=input('What is the genre you want? press x to quit\n')
                                    real_genre=genre[0].capitalize()+genre[1:].lower()
                                    filter_results=s.filter_genre(expanded_results, real_genre)
                                    if filter_results is not None: break
                                    if genre.lower()=='x':
                                        break
                                    else:print('Genre not found')

                                if subchoice2==4:
                                    actor=input('What is the name of the actor? press x to quit\n')
                                    filter_results=s.filter_actor(expanded_results, actor)
                                    if filter_results is not None: break
                                    if genre.lower()=='x':
                                        break
                                    else:print('Actor not found')
                        filtered_lines=s.format_results(filter_results)
                        for line in filtered_lines:print(line)
                    elif subchoice==4:
                        title=input('What is the title? please copy and paste\n')
                        result=client.search_title(title)
                        if s.validate(result) and result is not None:
                            lines=s.format_title(result)
                            for line in lines: print(line)
                            history_titles.add_favorite(result)
                            print('Do you want to add favorite?\n1. Yes\n2. No')
                            subchoice2=u.select_choice(2)
                            if subchoice2==1:
                                if all(item.get('Title') != result.get('Title') for item in user.memory):
                                    user.add_favorite(result)

                                print('Done!')
                        else: 
                            print('Not found')                  
                    elif subchoice==5:
                        title=input('What is the title? \n')
                        result=s.search_title(results, title)
                        if result is not None:
                            new_lines=s.format_title(result)
                            for line in new_lines: print(line)
                            history_titles.add_favorite(result)
                            print('Do you want to add favorite?\n1. Yes\n2. No')
                            subchoice2=u.select_choice(2)
                            if subchoice2==1:
                                if all(item.get('Title') != result.get('Title') for item in user.memory):
                                    user.add_favorite(result)
                                print('Done!')   
                        else:
                            print('Not found')
                    if subchoice==6:
                        break
                    if subchoice==None:
                        break
                if subchoice==6: continue
                if subchoice==None:break
            
       
        if choice==3 or choice==4:
            while True:
                if choice==3:
                    f=user
                    r='favorites'
                elif choice==3:
                    r='history'
                    print('What history do you want to see?\n1. Search\n2. Titles')
                    subchoice=u.select_choice(2)
                    if subchoice==1:
                        f=history_searches
                    elif subchoice==2:
                        f=history_titles
                    else: break
                while True:
                    print('What do you want to do next?')
                    print(f'1. See all {r}')
                    print(f'2. Filtrate {r}')
                    print(f'3. Search in {r}')
                    print('4. Order by rating')
                    print('5. Order by year')
                    print('6. Search for a title')
                    print('7. Expand a title')
                    print('8. Remove all')
                    subchoice2=u.select_choice(8)
                    
                    if subchoice2==1:
                        print(f'Here you have all {name}`s {r}\n\n')
                        lines=s.format_results(f.memory)
                        for line in lines: print(line)
                    
                    if subchoice2==2:
                        print('What is the criteria?')
                        print('1. Genre')
                        print('2. Year')
                        print('3. Type')
                        print('4. Actor')
                        subchoice3=u.select_choice(4)
                        if subchoice3==2 or subchoice3==3:
                            if subchoice3==2:
                                while True:
                                    year=input('What year are you looking for?\n')
                                    try:
                                        year_int=int(year)
                                        if year_int<1900 or year_int>2026:
                                            print('Try again')
                                        else:
                                            filter_results=s.filter_year(f.memory, year_int)
                                            break
                                    except ValueError:
                                        filter_results=f.memory
                                        print('No criteria found, giving results back')
                                        break
                            if subchoice3==3:
                                print('What type are you looking for?\n1. Movies\n2. Series\n3. Games\n')
                                type_choice=u.select_choice(4)
                                if type_choice==None: 
                                    filter_results=f.memory
                                    print('No criteria found, giving results back')
                                elif type_choice==1:filter_results=s.filter_type(f.memory, 'movie')
                                elif type_choice==2:filter_results=s.filter_type(f.memory, 'series')
                                elif type_choice==3:filter_results=s.filter_type(f.memory, 'game')
                            
                        if subchoice3==1 or subchoice3==4:
                            if f==history_searches:
                                titles=s.extract_title(f.memory)
                                expanded_results=[]
                                for title in titles:
                                    expanded_results.append(client.search_title(title))
                                expanded_results = [r for r in expanded_results if isinstance(r, dict)]

                            else: 
                                expanded_results=f.memory
                            while True:
                                if subchoice3==1:
                                    genre=input('What is the genre you want? press x to quit')
                                    real_genre=genre[0].capitalize()+genre[1:].lower()
                                    filter_results=s.filter_genre(expanded_results, real_genre)
                                    if filter_results is not None: break
                                    if genre.lower()=='x':
                                        break
                                    else:print('Genre not found')

                                if subchoice3==4:
                                    actor=input('What is the name of the actor? press x to quit')
                                    filter_results=s.filter_actor(expanded_results, actor)
                                    if filter_results is not None: break
                                    if genre.lower()=='x':
                                        break
                                    else:print('Actor not found')
                        filtered_lines=s.format_results(filter_results)
                        for line in filtered_lines:print(line)

                    if subchoice2==3:
                        kword=input('What titles are you looking for?\n')
                        print('What type are you looking for?\n1. Movies\n2. Series\n3. Games\n4. Nothing particular')
                        type_choice=u.select_choice(4)
                        if type_choice==1:type='movie'
                        if type_choice==2:type='series'
                        if type_choice==3:type='game'
                        if type_choice==4:type=None
                        else: break
                        while True:
                            print('What year are you looking for? press any letter if you do not want to add a year\n')
                            year=input()
                            try:
                                year_int=int(year)
                                if year_int>1900 and year_int<2026:
                                    break
                                else:
                                    print('Try again')
                            except ValueError:
                                year_int=None
                                break
                        page=1
                        results=[]
                        while client.search_specifics(kword, page=page, type=type, year=year_int) is not None: 
                            results.append(client.search_specifics(kword, page=page, type=type, year=year_int))
                            page=+1
                        if s.validate(results):
                            new_results=s.extract_title(results)
                            results_in_f=[]
                            for title in new_results:
                                item=s.search_title(f.memory, title)
                                if item is not None: results_in_f.append(item)
                            
                            lines=s.format_results(results_in_f)
                            print(f'These are the results for {kword} in {r}:\n\n')
                            for line in lines: print(line)
                        else:
                            print('Not results found')
                            
                    if subchoice2==4:
                        ordered_results=s.order_rating(f.memory)#rating
                        new_lines=s.format_results(ordered_results)
                        print(f'These are the results for {r} ordered by rating\n')
                        for line in new_lines: print(line)    
                    
                    if subchoice2==5:
                        ordered_results=s.order_year(f.memory)#year
                        new_lines=s.format_results(ordered_results[:20])
                        print(f'These are the results for {r} ordered by year\n')
                        for line in new_lines: print(line)   

                    if subchoice2==6:
                        title=input('What is the title?\n')
                        result=s.search_title(f.memory,title)
                        if f==history_searches:
                            result=client.search_title(title)
                        new_lines=s.format_title(result)
                        for line in new_lines: print(line)
                        print(f'Do you want to remove from {r}?\n1. Yes\n2. No')
                        subchoice3=u.select_choice(2)
                        if subchoice2==1:
                            f.remove_favorite(result)
                            print('Done!')  

                    if subchoice2==7:
                        title=input('What is the title? please copy and paste')
                        if f==history_searches:
                            if s.search_title(f.memory, title) is not None:
                                result=client.search_title(title)
                                if s.validate(result):
                                    lines=s.format_title(result)
                                    for line in lines: print(line)
                                    print(f'Do you want to remove from {r}?\n1. Yes\n2. No')
                                    subchoice3=u.select_choice(2)
                                    if subchoice3==1:
                                        f.remove_favorite(result)
                                        print('Done!')
                                else: 
                                    print('Title not found')   
                            else:
                                print('Title is not in memory') 
                        else:
                            lines=s.format_title(s.search_title(f.memory, title))
                            for line in lines: print(line)
                            print(f'Do you want to remove from {r}?\n1. Yes\n2. No')
                            subchoice3=u.select_choice(2)
                            if subchoice3==1:
                                f.remove_favorite(s.search_title(f.memory, title))
                                print('Done!')
                        
                    if subchoice2==8:
                        print('Are you sure? there is no going back')
                        print('1. Yes\n2. No')
                        subchoice3=u.select_choice(2)
                        if subchoice3==1:
                            for item in f.memory:
                                f.remove_favorite(item)
                            print('Done!')
                        else:
                            print('going back')

                    if subchoice==None:
                        print('Going back')
                        break
    
        if choice==None:
            print('Thank you! We are saving the data')
            history_searches.save_all()
            history_titles.save_all()
            user.save_all()
            break


if __name__=='__main__':
    main()