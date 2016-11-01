# ADA-Project - Seasonal points of interest in Switzerland

## Abstract

The idea of our project is to find, based on social networks data, the seasonal points of interest in Switzerland. What we mean by *seasonal point of interest* is a place which experience a **regular and predictable** change of its interest through calendar year, likely to repeat each year.   

More concretely, we want to focus on places that generate interest according to natural conditions (temperature, weather, scenary, etc..) rather than events (Festival, exposition, etc..).

## Data description 

We will mainly focus on Switzerland Instagram data, for various reason
* It is a very popular and active social network in Switzerland
* It is mainly based on photo/video sharing, which makes it interesting to represents nature interest of a place
* It encourages the users to geolocate the content they publish, hence the data contains a lot of geolocation helping for the development of this project

### Points location

We will use pictures/videos geolocation to establish the points of interests position. We may also use the hashtags in the pictures description that generally contains useful information about the location, for those who are not geolocated.

### Points interests

The interests of a place will be computed according to the number of "likes" and "share" its pictures got.

### Seasonality

For each point, we will have a time series representing the interest throughout the year. This way we will be able to sort to sort the events according to their interest at a given period of the year. The time series will also allow to discard points with non-natural interest distribution (Events, festivals, etc...).

## Feasibility and Risks 

The two challenging aspects of our project will be:
* Treating the data and extracting information, because of the large amount of data
* Offer a nice vizualization of our results

### Data treatment

Despite the fact that the data will be very big and require the use of the cluster, the information we want to extract are pretty simple. We will need to find the point of interests by clustering the location, then compute the number of likes/share for each point.

### Visualization

Once we have our results, we will provide a nice and intuitive vizualization allowing to display the point of interests according to a specific period or a location filter.

### Risks

The principal risk is to not obtain enough information to produce proper time series of point interests. Therefore we would not be able to determine their seasonality, discards the events/festivals or propose points according to period of the year.

This risk could come to the fact that not all post on Instagram are geolocated. We will need to determine the proportion of located/unlocated picture and maybe we will have to extract location from "hashtags".

## Deliverables 

We will produce a website with a Javascript interface display the map of Switzerland. The user will have the possiblity to add period/location filter and according to them, the point of interests will pop on the map. Clicking on the points will display infos/pictures.

## Timeplan

| Date     |   Progress |
|------------|------------------|
|Nov. 6th  | Project proposal|
|Nov 25th | Obtained data from january to end of october <br> Location clustering |
|Dec 9th | Extract points interest time series <br> Get location from hashtags (if necessary) |
|Mid december TBD | Checkpoint|
|End of december | Display results |
|Mid of january | Add data of november-december, rerun|
|Mini-Symposium |(End of January - TBD)|
