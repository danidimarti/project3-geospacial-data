
from pymongo import MongoClient
client = MongoClient("localhost:27017")
import pandas as pd
import numpy as np
import folium
from folium import Choropleth, Circle, Marker, Icon, Map
from folium.plugins import HeatMap, MarkerCluster
import geopandas as gpd
import time
import requests





def top_cities(df, column, n=4, columns_to_keep=['city', 'company', 'latitude', 'longitude']):
    """
    Filters a dataframe to contain only the top n most frequent values in a specified column
    Args:
        df (pandas.DataFrame): the dataframe to be filtered
        column (str): the name of the column to count and filter
        n (int): the number of top values to keep (default is 3)
        columns_to_keep (list): the list of columns to keep in the filtered dataframe (default is ['city', 'country', 'name', 'latitude', 'longitude'])
    Returns:
        The filtered dataframe
    """
    value_counts = df[column].value_counts()
    top_values = value_counts[:n].index.tolist()
    return df[df[column].isin(top_values)][columns_to_keep]


def count_cities(column):
    """
    Args:
        column: the column for which you want the value counts 
    Returns:
        The value counts of the column 
    """
    value_counts = column.value_counts()
    index = value_counts.index.astype(str)
    return value_counts

def get_city_map(city, zoom=15):
    '''
    Args: 
    City: the city you want to use to create your map. The city needs to be in the below dict cities
    Zoom: how close you want the map to be, defatul being 10
    Returns: the map, centralized in the city with the zoom of choice
    '''
    cities = {
        'New York': (40.7128, -74.0060),
        'San Francisco': (37.7749, -122.4194),
        'London': (51.5074, -0.1278),
    }

    city_coordinates = {'type': 'Point', 'coordinates': cities[city]}
    return folium.Map(location=city_coordinates['coordinates'], zoom_start=zoom)

def map_markers(df,city,map_):
    """
    Args:
        df (dataframe): the dataframe from where we get the coordinates of each company  
        city (string): the city where we will map the companies from the df
        map (folium.Map): the map where the data wil be placed.
    Returns:
        the map with all markers
    """
    for i, row in df[df.city == city].iterrows():
        company = {
            "location":[row["latitude"], row["longitude"]],
            "tooltip" : row["company"]
        }
        
        icon = Icon(color = "blue",
                    prefix = "fa",
                    icon = "building",
                    icon_color = "white"
        )
            
        Marker(**company,icon = icon ).add_to(map_)
    return(map_)

def count_cities(column):
    """
    Args:
        column: the column for which you want the value counts 
    Returns:
        The value counts of the column 
    """
    value_counts = column.value_counts()
    index = value_counts.index.astype(str)
    return value_counts


def get_city_map(city, zoom=15):
    '''
    Args: 
    City: the city you want to use to create your map. The city needs to be in the below dict cities
    Zoom: how close you want the map to be, defatul being 10
    Returns: the map, centralized in the city with the zoom of choice
    '''
    cities = {
        'New York': (40.7128, -74.0060),
        'San Francisco': (37.7749, -122.4194),
        'London': (51.5074, -0.1278),
    }

    city_coordinates = {'type': 'Point', 'coordinates': cities[city]}
    return folium.Map(location=city_coordinates['coordinates'], zoom_start=zoom)

def map_markers(df,city,map_):
    """
    Args:
        df (dataframe): the dataframe from where we get the coordinates of each company  
        city (string): the city where we will map the companies from the df
        map (folium.Map): the map where the data wil be placed.
    Returns:
        the map with all markers
    """
    for i, row in df[df.city == city].iterrows():
        company = {
            "location":[row["latitude"], row["longitude"]],
            "tooltip" : row["company"]
        }
        
        icon = Icon(color = "blue",
                    prefix = "fa",
                    icon = "building",
                    icon_color = "white"
        )
            
        Marker(**company,icon = icon ).add_to(map_)
    return(map_)