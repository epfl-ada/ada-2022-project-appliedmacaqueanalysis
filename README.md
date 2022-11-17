"# ada-2022-project-appliedmacaqueanalysis" 
# Hoppy Christmas! A guide to christmas beers
## Abstract:
Being a new brewery, we would like to optimize the production of our beer in respect to the time dimension. We analyse seasonnal trends in beer consumtion to know when to release a new beer. On top of this we analyse the evolution over time of the consumtion of beer in order to have the a minimum amount of remaining storage after sales. Our goals would be to understand what makes a beer trendy and be able to predict how the beer’s success evolves throughout the years. With this, we could know how much beer to produce throughout the year. In particular this year, we would like to produce a holiday season beer. To do so we will focus our analyses on the winter season. We would like to know what the typical characteristics of a christmas beer are, how much people will consume it relative to other beers.

## Reasearch questions:
- Can we find successful beers during a certain season?
- What makes a trendy christmas beer? 
  - characteristics, key description words, confounding factors
- Summer also????
- Brewery size????
 
## Methods
### Pre-Processing
Firstly, we filter for beers that have more than 2 years of reviews and that have more than a given amount of reviews (t.b.d.). Then, by analysing review density of different beers (e.g. IPA, American Pale Wheat Ale) as a proxy for beer popularity, we select a subsetof beers that show a strong seasonnal trend, in particular for the winter months.

### Characteristics extraction
Then, we extract positive description words for winter beers. By comparing this to the positive words of other beers, we find particular winter beer characteristics. vive le veau

Further, with the review density analysis, we could estimate beer consumption over time. Normalizing by the number of reviews for that moment on the different websites, an estimation of how much beer will be consumed for a certain beer at a certain time can be made. Applying linear regression, the amount of production of our trendy christmas beer could be estimated for the following season knowing the success we had the previous season.

## External libraries
- regex

