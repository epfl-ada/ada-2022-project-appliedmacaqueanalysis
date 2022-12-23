# Hoppy Christmas and Happy brew year ! A guide to christmas beers

## Data story available [here](https://mrichter-git.github.io/HoppyChristmas/) !

## Abstract:
Being a small brewery, we would like to conduct a study on beer trendiness to optimize our production with respect to time. We analyse seasonal trends in beer consumption to know when to release a new one. On top of this we analyse the evolution over time of multiple beer's consumption in order to have the minimum amount of remaining storage after sales. Our goals would be to understand what makes a beer trendy and be able to predict how the beer’s success evolves throughout the year. With this, we could know how much beer to produce at a certain time. In particular, we would like to produce a holiday season beer. To do so we will focus our analyses on the winter season. We would like to know what the typical characteristics of a Christmas beer are and how much people will consume it relatively to other beers. We assumed that the number of reviews was representative of the consumption rate, since a beer has to be consumed to be reviewed.

## Research questions:
* Is there seasonality in beer' success ?
* If yes, what makes a beer trendy, in particular during Christmas time? 
  * What characterises them ? Is there a specific flavor which is more appreciated in winter, or does it even have influence in that regard ?
  * Can we find key words, describing what would make a beer successful on winter days e.g. the feeling of warmness it provides ?
  * Are there confounding factors ?
* Can we extend the analysis we made for the Christmas beers to the other ones, for example summer beers ?
 
## Methods

### Preprocessing

The data are already quite clean for this dataset: a large portion of data wrangling was already done for us. Also, we do not consider the _./ratings.txt.gz_ files in the BeerAdvocate and RateBeer folders, as they are an unclean version of the _./reviews.txt.gz_ files. 
Firstly, some beers do not provide enough data to be taken into account in our processing. Thus, we filter for beers that have been reviewed for more than two years, and which already have enough feedbacks. The threshold for that is decided based on the distribution of the number of reviews per beer.

To ease the access and the opening speed, we store those data as a pickle file (_.pkl_).

### Feature extraction

Then, by analysing review density of different beers types (e.g. IPA, American Pale Wheat Ale) as a proxy for beer popularity, we select a subset of beers that show a strong seasonnal trend as shown [here](https://towardsdatascience.com/finding-seasonal-trends-in-time-series-data-with-python-ce10c37aa861), in particular for the winter months.

We can typically see how certain events influence a beeer's popularity (St. Patrick's day or Christmas / New Year's Eve for example) :
<p align="middle">
 <img src="https://github.com/epfl-ada/ada-2022-project-appliedmacaqueanalysis/blob/main/images/irish_stout_popularity.jpeg" width="300"/>
 <img src="https://github.com/epfl-ada/ada-2022-project-appliedmacaqueanalysis/blob/main/images/winter_warmer_popularity.jpeg" width="300"/>
</p>

To select the seasonal beers, we give the seasonality a rating. Also, by decomposing the review count per day, modulo the years, we can isolate the trend of a particular beer. Because some beers do not have enough reviews, or have not been reviewed for long enough, some have to be filtered. We considered that we needed at least two years worth of reviews to apply our algorithms. Finally, we keep only the beers, or types of beer, having a strong enough seasonality coefficient in the month of interest.

### Lexical differences between all beers and winter related beers

 <p align="middle">
  <img src="https://github.com/epfl-ada/ada-2022-project-appliedmacaqueanalysis/blob/main/images/wordmap.jpeg" width="300" />
  <img src="https://github.com/epfl-ada/ada-2022-project-appliedmacaqueanalysis/blob/main/images/winter_wordmap.jpeg" width="300" /> 
</p>

The wordcloud on the right corresponds to the lexical fields of the beers whose review contains "winter". However a review containing the w-word does not guarantee that the beer in question is a winter beer, nor does it says wether it is appreciated or not. Therefore, to go deeper, we conducted a sentiment and an aspect-based analysis on the reviews of the beers trendy during December, and the ones trendy during July to check if we could identify lexical fields for the most talked about aspects of those beers.

Based on those Christmas and Summer beers, we used the _Spacy_ library to select all the reviews which had a positive bias toward the analyzed beer, and retained the group of words characterizing it the best. Often, it corresponds to pairs like (_name_,_adjectives_) such as (head, white) (the head of a beer refering to the foam above). This analysis yields a list of aspects such as the carbonation, the lacing, the color, etc.

To classify the aspects' meaningfulness, we computed their popularity, i.e the frequency at wich they appear in the reviews. We assumed that the more a word was present, the likelier it was to be significant for the beer. Thus, we kept the most used aspects and adjectives to characterize the beers we were studying.

We obtained wordclouds like this :

 <p align="middle">
  <img src="https://github.com/epfl-ada/ada-2022-project-appliedmacaqueanalysis/blob/main/images/all_beers.png" width="200" height="400" title="Random beers">
  <img src="https://github.com/epfl-ada/ada-2022-project-appliedmacaqueanalysis/blob/main/images/xmas_beers.png" width="200" height="400" title="Christmas beers">
  <img src="https://github.com/epfl-ada/ada-2022-project-appliedmacaqueanalysis/blob/main/images/summer_beers.png" width="200" height="400" title="Summer beers">
</p>

## Contribution of the group members


| Names                | Tasks |
|-----------------|-------|
| Louis Gounot    | Thrilling data story, Incredible plots, tasting |
| Hugo Delesalle  | Preprocessing, Best seasonality study ever, tasting |
| Baudouin Bosc   | Sentiment analysis, Data visualization, tasting |
| Michael Richter | Thrilling data story, Amazing website, tasting |

## Proposed timeline

19.11 &#8594; 02.12 :
 * Preprocessing:
 * Seasonal trend analysis


02.12 &#8594; 16.12 : 
 * Sentiment analysis
 * Start of data story:
   * website creation
   * global structure
 * Features extraction


16.12 &#8594; 21.12 :

  * Data visualization
  * Data story : 
     * write story and connect dots
     * embed graphics

21.12 &#8594; 23.12 - 23h50 :

   * Draw conclusions
   * Clean up code

23.12 - 23h51 &#8594; 23.12 - 23h59 :

  * git commit
  * git push
  * Taste beers

The timeline proposed in Milestone 2 was overall respected during Milestone 3.
