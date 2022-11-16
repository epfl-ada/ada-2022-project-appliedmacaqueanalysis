"# ada-2022-project-appliedmacaqueanalysis" 
# Hoppy Christmas! A guide on christmas beers
## Abstract:
Being a new brewery, we would like to optimize the production of our beer in respect to the time dimension. We analyse seasonnal trends in beer consumtion to know when to release a new beer. On top of this we analyse the evolution over time of the consumtion of beer in order to have the a minimum amount of remaining storage after sales. Our goals would be to understand what makes a beer trendy and be able to predict how the beer’s success evolves throughout the years. With this, we could know how much beer to produce throughout the year.

We focus on the reviews of the beer to see its success and how the reviews and the number of reviews evolve during a certain amount of time. Like this we can determine the success of the beer depending on the season.

## Reasearch questions:
- What makes a beer trendy? Can we find characteristics that make certain beer trendy at a certain time?
  - What makes a good christmas beer?
- Is it possible to optimize the production of a beer during the year, by knowing when it will be trendy?
  - Could we find a production agenda?
 
## Methods
By analysing review density of different styles of beer (e.g. IPA, American Pale Wheat Ale) as a proxy for beer popularity, we isolate some types that have strong seasonal trends. With this subset of the data we can run an analysis of reviews to make a 'heatmap' of most used words to describe a trendy seasonal beer. With this we could establish a description of a Christmas beer.
Further, with the review density analysis, we could estimate beer consumption over time. Normalizing by the number of reviews for that moment on the different websites, an estimation of how much beer will be consumed for a certain beer at a certain time can be made. Applying linear regression, the amount of production of our trendy christmas beer could be estimated for the following season knowing the success we had the previous season.
