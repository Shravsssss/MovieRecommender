import pandas as pd
import warnings
import os

app_dir = os.path.dirname(os.path.abspath(__file__))
code_dir = os.path.dirname(app_dir)
project_dir = os.path.dirname(code_dir)

warnings.filterwarnings("ignore")


def recommendForNewUser(user_rating):

    if not user_rating:
        return []

    # Check for invalid rating values
    invalid_ratings = [rating for rating in user_rating if rating["rating"] is None or rating["rating"] < 0.0 or rating["rating"] > 5.0]
    if invalid_ratings:
        return []  # Return an empty list if there are invalid ratings
        
    ratings = pd.read_csv(project_dir + "/data/ratings.csv")
    movies = pd.read_csv(project_dir + "/data/movies.csv")
    user = pd.DataFrame(user_rating)

    # Strip leading and trailing spaces from titles
    user["title"] = user["title"].str.strip()
    movies["title"] = movies["title"].str.strip()

    userMovieID = movies[movies["title"].isin(user["title"])]
    userRatings = pd.merge(userMovieID, user)

    # Check for too long movie titles
    max_title_length = 255  # Set your desired maximum title length
    if any(len(title) > max_title_length for title in user["title"]):
        return []  # Return an empty list if any title is too long

     # Ensure that the "title" key exists in each rating dictionary
    user = user[user["title"].isin(movies["title"])] if "title" in user.columns else pd.DataFrame()
    if user.empty:
        return []  # Return an empty list if no valid movie titles are found in the input

    moviesGenreFilled = movies.copy(deep=True)
    copyOfMovies = movies.copy(deep=True)
    for index, row in copyOfMovies.iterrows():
        copyOfMovies.at[index, "genres"] = row["genres"].split("|")
    for index, row in copyOfMovies.iterrows():
        for genre in row["genres"]:
            moviesGenreFilled.at[index, genre] = 1
    moviesGenreFilled = moviesGenreFilled.fillna(0)

    userGenre = moviesGenreFilled[moviesGenreFilled.movieId.isin(userRatings.movieId)]
    userGenre.drop(["movieId", "title", "genres"], axis=1, inplace=True)
    userProfile = userGenre.T.dot(userRatings.rating.to_numpy())
    moviesGenreFilled.set_index(moviesGenreFilled.movieId)
    moviesGenreFilled.drop(["movieId", "title", "genres"], axis=1, inplace=True)

    recommendations = (moviesGenreFilled.dot(userProfile)) / userProfile.sum()
    joinMoviesAndRecommendations = movies.copy(deep=True)
    joinMoviesAndRecommendations["recommended"] = recommendations
    joinMoviesAndRecommendations.sort_values(
        by="recommended", ascending=False, inplace=True
    )
    
    # Remove the movies that the user has already rated (training data)
    rated_movie_titles = userRatings["title"].tolist()  # Movies in training data
    joinMoviesAndRecommendations = joinMoviesAndRecommendations[~joinMoviesAndRecommendations["title"].isin(rated_movie_titles)]

    return [x for x in joinMoviesAndRecommendations["title"]][:201]
