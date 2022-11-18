# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 15:23:05 2022

@author: baudo
"""

import pandas as pd
import pickle
import matplotlib.pyplot as plt
import gzip

def make_pickles(dataset,data):
    try:
        with open(dataset+'/'+data+'.pkl', "wb") as file:
            pickle.dump(data,file)
    except:
        raise SystemError(f"Unable to create pickle for {data}")

def load_pickles(dataset,*argv):
    datas = {}
    assert (type(dataset)==str), "The dataset should be a str"
    for arg in argv:
        with open(dataset+'/'+arg+'.pkl', "rb") as file:
            datas[arg] = pickle.load(file)
    return datas

#%%

datasets = load_pickles("RateBeer","beers")

#%%
# case study on RateBeer : https://drive.google.com/file/d/1VGz4OSe89bHpSG1SYx6yQ1hW25A5cYGA/view


cumsum = datasets["beers"].groupby("style")['nbr_ratings'].sum()

def barchart(df, cmap):
  fig = plt.figure()
  ax = fig.add_axes([0,0,1,1])
  ax.barh(df.index, df, color=cmap.colors[::5])
  ax.set_title("Top 20 most rated beer style")
  ax.set_ylabel("Beer style")
  ax.set_xlabel("Number of ratings")
  return fig

barchart(cumsum.sort_values()[-20:], plt.get_cmap("plasma"))

#%%

review_format = ["beer_name","beer_id","brewery_name","brewery_id","style","abv",\
                 "date","user_name","user_id","appearance","aroma","palate","taste",\
                     "overall","rating","text"]

def keep_only(*argv): return [(arg,review_format.index(arg)) for arg in argv] # filtering the columns not needed

def peek_to_dict(peek):
    categories = keep_only("beer_name","brewery_id","style","date","user_id",\
                           "appearance","aroma","palate","taste","overall","rating")
    review = {category[0] : [] for category in categories}
    
    for pe in peek:
        lines = pe.split("\n")
        for category in categories:
            review[category[0]].append(lines[category[1]][len(category[0]+" "):])
    return pd.DataFrame.from_dict(review)


chunk_size = 100000000
with gzip.open("RateBeer/reviews.txt.gz", "rb") as f:
    review = peek_to_dict(f.read(chunk_size).decode("utf-8").split("\n\n")[:-1])
    


#%%

review["date"] = pd.to_datetime(review["date"],unit='s')
review["rating"] = review["rating"].apply(lambda x: x.strip()).astype(float)

monthly_review = review.groupby([review.date.dt.month,"style"])['rating'].mean()
styles = monthly_review.index.get_level_values(1).unique()
#%%

monthly_review = monthly_review.unstack(level=0).iloc[::10,[1,8,9,10,11]].dropna()


rating_evolution = monthly_review.plot.bar()
plt.legend(["jan","sep","oct","nov","dec"],bbox_to_anchor=(1.0,1.0))
plt.ylabel("rating")
plt.tick_params(axis='x',labelrotation=30)
rating_evolution.set_ylim(2.5,4)





























