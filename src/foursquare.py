

import requests
import json
from dotenv import load_dotenv
import os
import pandas as pd
import geopandas
from getpass import getpass
load_dotenv()

def find_places_fsq(city_coords, category=None, query=None):
    """
    Makes calls to the foursquare API
    Args:
        city (point): coordinates of the city in type point where the request is to be made 
        query (string): the site to be searched 
        category (string): the category of the site to be searched 
    Returns:
        The request as a list
    """
    url = "https://api.foursquare.com/v3/places/search?"
    headers = {
        "accept": "application/json",
        "Authorization": token
    }
    
    params = {
        "ll": f"{city_coords[0]},{city_coords[1]}",
        "limit": 50
    }
    
    if query and category:
        url += f'query={query}&categories={category}'
        params["query"] = query
        params["category"] = category
    elif query:
        url += f'query={query}'
        params["query"] = query
    elif category:
        url += f'categories={category}'
        params["category"] = category
        
    return requests.get(url=url, headers=headers, params=params).json()

# Function that takes the dict_ (results form four square queries) and returns a clearner dict_ with only relevant information
# name_coordinates(VARIABLE_NAME["results"]) -> variable_name is the name of the var where you saved the result of the fsq query above

def name_coordinates (dict_):
    '''
    Function that takes the dict_ (results form four square queries) and returns a clearner dict_ with only relevant information
    THIS FUNCTION WILL BE CALLED IN THE DICT_T0_DF FUNCTION.
    '''    
    processed_dict = {"name": dict_["name"],
                      #"location": {"type": "Point", "coordinates": [dict_["geocodes"]["main"]["latitude"], dict_["geocodes"]["main"]["longitude"]]}
                      'latitude': dict_["geocodes"]["main"]["latitude"],
                      'longitude': dict_["geocodes"]["main"]["longitude"]
                        }
    return processed_dict

def dict_to_df(query_list, category=None):
    new_list = []
    for i in query_list:
        new_list.append(name_coordinates(i))
        df = pd.DataFrame(new_list)
        if category:
            df['category'] = category
        else:
            np.nan
        #df.to_json(f"json/{query_list}.json", orient="records")
    return df