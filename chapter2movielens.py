import json
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
from cairocffi import *
import numpy as np




pathUserData='/home/christoph/PycharmProjects/PythonForDataAnalysis/pydata-book-master/ch02/movielens/users.dat'
pathRatingsData='/home/christoph/PycharmProjects/PythonForDataAnalysis/pydata-book-master/ch02/movielens/ratings.dat'
pathMoviesData='/home/christoph/PycharmProjects/PythonForDataAnalysis/pydata-book-master/ch02/movielens/movies.dat'

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table(pathUserData, sep='::', header=None,
names=unames,engine='python')

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table(pathRatingsData, sep='::', header=None,
names=rnames,engine='python')
mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table(pathMoviesData, sep='::', header=None,
names=mnames,engine='python')


data = pd.merge(pd.merge(ratings, users), movies)

#print(data)

mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')



#print(mean_ratings)


ratings_by_title=data.groupby('title').size()

print(ratings_by_title)

active_titles = ratings_by_title.index[ratings_by_title >= 250]
top_female_ratings = mean_ratings.sort_index(by='F', ascending=False)
print(top_female_ratings)

mean_ratings['diff']=mean_ratings['F']-mean_ratings['M']

sorted_by_diff=mean_ratings.sort_values(by='diff')
print(sorted_by_diff[:10])

rating_std_by_title = data.groupby('title')['rating'].std()
rating_std_by_title = rating_std_by_title.ix[active_titles]

print(rating_std_by_title.order(ascending=False)[:10])



