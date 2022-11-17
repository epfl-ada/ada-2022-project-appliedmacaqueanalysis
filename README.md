"# ada-2022-project-appliedmacaqueanalysis" 

# Hoppy Christmas! A guide to christmas beers

## Abstract:
Being a small brewery, we would like to optimize the production of our beer with respect to the time dimension. We analyse seasonnal trends in beer consumtion to know when to release a new beer. On top of this we analyse the evolution over time of the consumtion of beer in order to have the a minimum amount of remaining storage after sales. Our goals would be to understand what makes a beer trendy and be able to predict how the beer’s success evolves throughout the years. With this, we could know how much beer to produce throughout the year. In particular this year, we would like to produce a holiday season beer. To do so we will focus our analyses on the winter season. We would like to know what the typical characteristics of a christmas beer are, how much people will consume it relative to other beers.

## Reasearch questions:
- Can we find successful beers during a certain season?
- What makes a trendy christmas beer? 
  - characteristics, key description words, confounding factors
- Summer also????
- Brewery size????
 
## Methods
The data was collected and cleaned by the maker of this dataset, a large portion of data wrangling was already done for us. 
Firstly, we filter for beers that have more than 2 years of reviews and that have more than a given amount of reviews (t.b.d.). Then, by analysing review density of different beers types (e.g. IPA, American Pale Wheat Ale) as a proxy for beer popularity, we select a subset of beers that show a strong seasonnal trend, in particular for the winter months.
### insert graph Hogo here
This can be verified by adding up the reviews done on each day of the year over the whole time the data was collected to verify if there is indeed a peak of popularity at a certain season:
### insert graph Michou here

From these seasonnal beer types, we can find the most used words to positively describe these beers. By doing the same for other beers,  we can isolate words that are specifically positive for winter/christmas beers. This dictionnairy would allow to identify other winter beers.  




## External libraries
- numpy, datetime
- regex, googletrans
- matplotlib, seaborn?
- worldcloud ?


## Proposed Timeline and
Tasks: data story, data visu, preprocessing, readme, seasonnal trend analysis, PCA on rating categories(appearance, aroma, palate, taste, abv) and clustering, characteristic word extraction NLP à l'aide Baudou ?


| Names                | Tasks |
|-----------------|-------|
| Louis Gounot    | T.B.D |
| Hugo Delesalle  | T.B.D |
| Baudouin Bosc   | T.B.D |
| Michael Richter | T.B.D |

