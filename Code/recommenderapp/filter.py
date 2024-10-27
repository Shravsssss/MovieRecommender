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
        for x in self.df.rows:
            if rate >= x["rating"]:
                res.append(x["movieId"])
        movies = self.df["title"].iloc[self.df["movieId"] in res]
        return movies

    def resultsgenre(self, genre):
        res = []
        for x in self.df.rows:
            if genre in x["genres"]:
                res.append(x["title"])
        return res

    def resultsTop10rate(self, word):
        return self.resultsrate(word)[:10]
    
    def resultsTop10(self, word):
        return self.resultsgenre(word)[:10]


if __name__ == "__main__":
    app.run()
