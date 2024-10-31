import unittest
import warnings
import sys
import os

sys.path.append("../")
from Code.recommenderapp.reviews import get_movie_reviews, search_movie_tmdb

warnings.filterwarnings("ignore")

class Tests(unittest.TestCase):
    # Test 1
    api_key = "9f385440fe752884a4f5b8ea5b6839dd"
    def testFilterAdventure(self):
        movie_name = "Inception"  
        # Find TMDb movie ID for "Inception"
        movie_id = search_movie_tmdb(movie_name, self.api_key)
        reviews = get_movie_reviews(movie_id, self.api_key)

        expected_resp = [
            
        ]
        self.assertTrue(reviews == expected_resp)

    # Test 2
    def testFilterAnimation(self):
        search_word = "Animation"
        search = Filter()
        filtered_dict = search.resultsTop10(search_word)
        expected_resp = [
            "Toy Story (1995)",
            "Toys (1992)",
            "Toy Story 2 (1999)",
            "Toy, The (1982)",
            "Toy Soldiers (1991)",
            "Toy Story 3 (2010)",
            "Babes in Toyland (1961)",
            "Babes in Toyland (1934)",
        ]
        self.assertTrue(filtered_dict == expected_resp)
    
    # Test 3
    def testFilterChildren(self):
        search_word = "Children"
        search = Filter()
        filtered_dict = search.resultsTop10(search_word)
        expected_resp = [
            "Toy Story (1995)",
            "Toys (1992)",
            "Toy Story 2 (1999)",
            "Toy, The (1982)",
            "Toy Soldiers (1991)",
            "Toy Story 3 (2010)",
            "Babes in Toyland (1961)",
            "Babes in Toyland (1934)",
        ]
        self.assertTrue(filtered_dict == expected_resp)

    # Test 4
    def testFilterComedy(self):
        search_word = "Comedy"
        search = Filter()
        filtered_dict = search.resultsTop10(search_word)
        expected_resp = [
            "Toy Story (1995)",
            "Toys (1992)",
            "Toy Story 2 (1999)",
            "Toy, The (1982)",
            "Toy Soldiers (1991)",
            "Toy Story 3 (2010)",
            "Babes in Toyland (1961)",
            "Babes in Toyland (1934)",
        ]
        self.assertTrue(filtered_dict == expected_resp)
    
    # Test 5
    def testFilterFantasy(self):
        search_word = "Fantasy"
        search = Filter()
        filtered_dict = search.resultsTop10(search_word)
        expected_resp = [
            "Toy Story (1995)",
            "Toys (1992)",
            "Toy Story 2 (1999)",
            "Toy, The (1982)",
            "Toy Soldiers (1991)",
            "Toy Story 3 (2010)",
            "Babes in Toyland (1961)",
            "Babes in Toyland (1934)",
        ]
        self.assertTrue(filtered_dict == expected_resp)

if __name__ == "__main__":
    unittest.main()