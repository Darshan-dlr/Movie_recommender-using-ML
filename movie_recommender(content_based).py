import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def get_title_from_index(index):
    return df[df.index ==index]["title"].values[0]
def get_index_from_title(title):
    return df[df.title==title]["index"].values[0]
     
    #step1:read csv ^M
        
df=pd.read_csv("movie_dataset.csv")
df.columns

#select features
features=['keywords','genres','director','cast']

#create a column in df which combines all selected features
for feature in features:
    df[feature]=df[feature].fillna(" ")
    
def combined_features(row):
    try:
        return row['keywords']+" "+row['genres']+" "+row['director']+" "+row['cast']
    except:
        print('error'), row
        
df['combined_features']=df.apply(combined_features,axis=1)
print('combined features'),df.combined_features.head()

#create count matrix from this new combined matrix
cv=CountVectorizer()
count_matrix=cv.fit_transform(df['combined_features'])

#compute the cosine similarity basedon the counr_matrix
cosine_sim=cosine_similarity(count_matrix)
movie_user_likes='Avatar'

#get the index of the moviefrom this title
movie_index=get_index_from_title(movie_user_likes)

similar_movies=list(enumerate(cosine_sim[movie_index]))
sorted_similar_movies=sorted(similar_movies,key=lambda x:x[1],reverse=True)

#print titles of first 50 movies
i=0
for movie in sorted_similar_movies:
    print(get_title_from_index(movie[0]))
    i=i+1
    if i>10:
        break

