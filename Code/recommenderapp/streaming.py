# This file is to show the links to all the 
# streaming platforms for the recommended movies
import requests

def search_movie_on_justwatch(movie_name, country_code='US'):
    url = f"https://apis.justwatch.com/content/titles/en_US/popular"
    payload = {"query": movie_name}
    response = requests.post(url, json=payload)
    # Check for a valid response
    if response.status_code != 200:
        print("Failed to fetch data")
        return None
    
    # Parse JSON response
    data = response.json()
    
    # Extract the movie details (assumes first result is relevant)
    if data['items']:
        movie = data['items'][0]
        offers = movie.get('offers', [])
        
        # Iterate through offers and extract platform name and URL
        streaming_info = []
        for offer in offers:
            platform_name = offer['provider_id']
            streaming_url = offer['urls']['standard_web']
            streaming_info.append((platform_name, streaming_url))
        
        return streaming_info
    else:
        print("No movie found")
        return None

# Example usage
movie_name = "Inception"
streaming_data = search_movie_on_justwatch(movie_name)