
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
            "tooltip" : row["name"]
        }
        
        if row['category'] == 'school':
            icon = Icon(color = "orange",
                    prefix = "fa",
                    icon = "graduation-cap",
                    icon_color = "white"
        )

        elif row['category'] == 'starbucks':
            icon = Icon(color = "cadetblue",
                    prefix = "fa",
                    icon = "coffee",
                    icon_color = "white"
        )

        elif row['category'] == 'vegan-restaurant':
            icon = Icon(color = "green",
                    prefix = "fa",
                    icon = "cutlery",
                    icon_color = "white"
        )

        elif row['category'] == 'basketball-court':
            icon = Icon(color = "red",
                    prefix = "fa",
                    icon = "paw",
                    icon_color = "white"
        )

        elif row['category'] == 'club':
            icon = Icon(color = "darkpurple",
                    prefix = "fa",
                    icon = "beer",
                    icon_color = "white"
        )
                
        Marker(**company,icon = icon ).add_to(map_)
    return(map_)