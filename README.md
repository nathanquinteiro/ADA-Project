# ADA-Project - Seasonal points of interest in Switzerland

## Abstract

The idea of our project is to find, based on social networks data, the seasonal points of interest in Switzerland. What we mean by *seasonal point of interest* is a place which experience a **regular and predictable** change of its interest through calendar year, likely to repeat each year.   

More concretely, we want to focus on places that generate interest according to natural conditions (temperature, weather, scenary, etc..) rather than events (Festival, exposition, etc..).

## Data choice

We will focus on Switzerland Tweeter data mainly because it is a very popular and active social network in Switzerland and it provides geolocation of the tweets, which is necessary to establish a map of the places of interest precisely.

## Data processing

### Filtering of the data

To focus on tweets that are located in "natural" areas, a mask is applied on the data to filter out all the tweets that are located in urban areas.

### Data clustering

To obtain meaningfull informations about the tweets distribution, the 1.8 remaining tweets are gathered in 1000 different clusters based on their location. To perform this task, the kmeans algorithm is run on the data using the processing power of EPFL clusters.

