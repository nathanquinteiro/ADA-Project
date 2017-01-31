# ADA-Project - Temporal analysis of networking activity in non-urban points of interest in Switzerland

## Abstract

The idea of this project is to find, based on social networks data and satellite imagery, the non-urban points of interest in Switzerland. What we mean by *non-urban point of interest* is a place located in a low to zero built environment density, which experience a relatively high social network activity  

More concretely, we want to focus on places in the nature that generate network activity, rather than places in the cities or villages.

## Data choice

We will focus on Switzerland Tweeter data mainly because it is a very popular and active social network in Switzerland and it provides geolocation of the tweets, which is necessary to establish a map of the places of interest precisely.

*The data in hadoop fs format can be found on EPFL cluster on **/datasets/twitter-swisscom/twex.tsv**.*

## Urban area detection

To determine the urban and non-urban area in Switzerland, we use Landsat-8 satellite images, and compute the NDBI (Normalized Difference Built-up Index), using the SWIR and NIR bands of the satellite images. We then apply filters and morphological operators on the NDBI image to produce a urban mask that will let us differentiate urban and non-urban location and therefore discard the urban tweets.

We used Google Earth Engine code editor to produce the NDBI for Switzerland and export the urban mask.

*The Google Earth engine code cand be found in the script [google_earth_NDBI.js](google_earth_NDBI.js "NDBI for Switzerland on Google Earth Engine"). The generated mask in TIFF format can be found in [data/urban_mask.tif](data/urban_mask.tif "TIFF urban mask")*.

## Data processing

*The data cleaning and processing is done in the notebook [DataCleaning_Urbanization.ipynb](DataCleaning_Urbanization.ipynb "Data Cleaning and processing")*

*The notebook produces two tsv files that are used by further Notebook (Clusters_analyze.ipynb):
* data/cleaned_non_urban_with_clusters.tsv: Which contains all information about the non-urban tweets, their id, date, position, and the cluster they belong to.
* data/clusters_centers.tsv: Which contains the position of the clusters
*


### Filtering of the data

To focus on tweets that are located in non-urban areas, we therefore apply the urban-mask on all tweets, and discard the non-urban tweets.

*Urban areas represents about 76% of the overall area, but only 9.5% of the tweets (~1.2 Millions of tweets).*

### Data clustering

To obtain meaningfull informations about the tweets distribution, the 1.8 remaining tweets are gathered in 1000 different clusters based on their location. To perform this task, the kmeans algorithm is run on the data using the processing power of EPFL clusters.

