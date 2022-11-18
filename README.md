"# ada-2022-project-appliedmacaqueanalysis" 

# Hoppy Christmas! A guide to christmas beers

## Abstract:
Being a small brewery, we would like to conduct a study on beer trendiness to optimize our production with respect to time. We analyse seasonal trends in beer consumption to know when to release a new one. On top of this we analyse the evolution over time of multiple beer's consumption in order to have the minimum amount of remaining storage after sales. Our goals would be to understand what makes a beer trendy and be able to predict how the beer’s success evolves throughout the years. With this, we could know how much beer to produce at a certain time. In particular, we would like to produce a holiday season beer. To do so we will focus our analyses on the winter season. We would like to know what the typical characteristics of a Christmas beer are and how much people will consume it relatively to other beers.

## Research questions:
* Can we find successful beers during a certain season?
* If yes, what makes a trendy christmas beer? 
  * What characterises them ? Is there a specific flavor which is more appreciated in winter, or does it even have influence in that regard ?
  * Can we find key words, describing what would make a beer successful on winter days e.g. the feeling of warmness it provides ?
  * Are there confounding factors ?
* Can we extend the analysis we made for the Christmas beers to the other ones ?
 
## Methods
The data was collected and cleaned by the maker of this dataset, a large portion of data wrangling was already done for us. 
Firstly, some beers do not provide us with enough data to be taken into account in our processing. Thus, we filter for beers that have more than 2 years of reviews and that have more than a given amount of reviews. The threshold for that is decided based on the distribution of the number of reviews per beer. Then, by analysing review density of different beers types (e.g. IPA, American Pale Wheat Ale) as a proxy for beer popularity, we select a subset of beers that show a strong seasonnal trend, in particular for the winter months.

To further study those particular beers, we will take a look at the metrics provided by the datasets (aroma, taste, etc.) along with the feeling experienced by the reviewers, and perform a comparison between the metrics of the seasonal beers and the non-seasonal ones.

If a word analysis is conducted, we may filter the reviews' text to only get english ones. The _NLTK_ library will provide us with sentiment analysis tools and other natural language processing means to investigate the reviews.
### insert graph Hogo here
This can be verified by adding up the reviews done on each day of the year over the whole time the data was collected to verify if there is indeed a peak of popularity at a certain season:
### insert graph Michou here
![alt text](https://github.com/epfl-ada/ada-2022-project-appliedmacaqueanalysis/blob/main/images/wordmap.jpeg)
From these seasonnal beer types, we can find the most used words to positively describe these beers. By doing the same for other beers,  we can isolate words that are specifically positive for winter/christmas beers. This dictionnairy would allow to identify other winter beers.  


## Tasks repartition

| Names                | Tasks |
|-----------------|-------|
| Louis Gounot    | Data story, Features extraction |
| Hugo Delesalle  | Preprocessing, Data visualization |
| Baudouin Bosc   | Sentiment analysis, Data visualization|
| Michael Richter | Seasonal trend analysis, Data story |

## Proposed timeline

19.11 --> 02.12 :
 * Preprocessing
 * Seasonal trend analysis


02.12 --> 16.12 : 
 * Sentiment analysis
 * Start of data story:
   * website creation
   * global structure
 * Features extraction


16.12 --> 21.12 :

  * Data visualization
  * Data story : 
     * write story and connect dots
     * embed graphics

21.12 --> 23.12 - 23h50 :

   * Draw conclusions
   * Clean up code

23.12 - 23h51 --> 23.12 - 23h59 :

  * git commit -m "final push"
  * git push
  * Taste beers
