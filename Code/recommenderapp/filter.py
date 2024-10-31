import pandas as pd

# from app import app
from flask import jsonify, request, render_template
import sys
import os

app_dir = os.path.dirname(os.path.abspath(__file__))
code_dir = os.path.dirname(app_dir)
project_dir = os.path.dirname(code_dir)


class Filter:

    df = pd.read_csv(project_dir + "/data/movies.csv")
    ratings = pd.read_csv(project_dir + "/data/ratings.csv")

    def __init__(self):
        pass

    def resultsratings(self, rate):
        res = []
        movies = []
        for index, row in self.ratings.iterrows():
            if rate >= row["rating"]:
                res.append(row["movieId"])
        for each in res:
           movies.append(self.df["title"][self.df["movieId"] == each])
        # movies = self.df["title"][self.df["movieId"] in res]
        return movies

    # With this function it is possible to have multiple pages to show 
    # more than just the first 10
    def resultsgenre(self, genres):
        res = []
        for index, row in self.df.iterrows():
            movie_genres = row["genres"].split('|')  # Assuming genres are separated by '|'
            if any(genre in movie_genres for genre in genres):
                res.append(row["title"])
        return res

    def resultsTop10rate(self, rate):
        return self.resultsratings(rate)[:10]
    
    def resultsTop10(self, genre):
        return self.resultsgenre(genre)[:10]


filter = Filter()
print(filter.resultsTop10rate(2))