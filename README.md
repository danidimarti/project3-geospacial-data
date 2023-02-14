
<img width=500 src='https://media4.giphy.com/media/myBz2xDdUTMmuACPD6/giphy.gif?cid=ecf05e47atqvb8pzdsik0t2owr5h1r6l1tsyctepywytcf3q&rid=giphy.gif&ct=g'>

# Finding the best location for gaming company 
> _Geospacial data project with MongoDB_
----

## Goal
This is a python project that was sent to us at the Ironhack data analytics bootcamp. 

The objective of the project is to select the location of a `gaming company` offices with the following structure:
* 20 Designers
* 5 UI/UX Engineers
* 10 Frontend Developers
* 15 Data Engineers
* 5 Backend Developers
* 20 Account Managers
* 1 Maintenance guy that loves basketball
* 10 Executives
* 1 CEO/President

The location has to cover more or less this requirements:

* Designers like to go to design talks and share knowledge. There must be some nearby companies that also do design.
* 30% of the company staff have at least 1 child.
* Developers like to be near successful tech startups that have raised at least 1 Million dollars.
* Executives like Starbucks A LOT. Ensure there's a starbucks not too far.
* Account managers need to travel a lot.
* Everyone in the company is between 25 and 40, give them some place to go party.
* The CEO is vegan.
* If you want to make the maintenance guy happy, a basketball stadium must be around 10 Km.
* The office dog—"Dobby" needs a hairdresser every month. Ensure there's one not too far away.

## Libraries:
<ol>
    <li> 1. Libraries: </li>
    <ul> 
        <li>pymongo</li>
        <li>pandas </li>
        <li>numpy </li>
        <li>folium </li>
        <li>folium.plugins </li>
        <li>geopandas </li>
        <li>time</li>
        <li>requests </li>
        <li>cartoframes</li>
    </ul>
</ol> 

## Data Sources: 
<ol>
    <li>Company.json: non-relational database provided for analysis </li>
     
</ol>       
    

## My project 
The final location will be a city. 

- Designers (23%) and Developers (17%) compose 40% of the workforce. The company has a higher chance to recruit and retain good talent in those areas if they are located in a place that is either:
    1. near design companies <br> 
    OR
    2. near successful tech startups that have raised more tham 1M 

#### *To find the ideal city, the first decision to make is to narrowing down the research.*

- From a list of 18.8K companies, design and tech startups with a high net worth are selected. 

- Once this pre-selection is done, the cities chosen will be the top 3 cities with the highest number of companies. 

<img width=500 src='images\heatmap_world.png'>


#### The selected cities are `San Francisco`, `New York` and `London` 🏆

- Using foursquare API) some establishments that meet employee requirements in the 3 cities are located. 



#### `San Francisco` was the choosen city as it contained the most number of requirements near a chosen radius

<img width=500 src='images\sf_map_plotted.png'>
