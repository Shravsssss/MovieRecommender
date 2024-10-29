# Extracting reviews from TMDB
import requests

# Return top 10 reviews
def get_movie_reviews(movie_id, api_key):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/reviews"
    params = {"api_key": api_key}
    
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        print("Failed to fetch data")
        return None
    
    reviews = response.json().get('results', [])
    results = reviews[:max(len(reviews), 5)]
    length = 0
    const = 1000
    show = []
    # Results max 1000 characters 
    for each in results:
        if length + len(each) <= const:
            show.append(each)
        else:
            show.append(each[:const - length])
    return show

def search_movie_tmdb(movie_name, api_key):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {"api_key": api_key, "query": movie_name}
    response = requests.get(url, params=params)
    data = response.json()
    
    if data['results']:
        return data['results'][0]['id']  # Return the first matching movie's ID
    return None


# Example usage
api_key = "9f385440fe752884a4f5b8ea5b6839dd"
movie_name = "Inception"  
# Find TMDb movie ID for "Inception"
movie_id = search_movie_tmdb(movie_name, api_key)
reviews = get_movie_reviews(movie_id, api_key)

if reviews:
    print(f"Top reviews for movie {movie_id}:")
    for review in reviews:
        print(f"Author: {review['author']}")
        print(f"Content: {review['content'][:200]}...")  # Print the first 200 characters of each review
