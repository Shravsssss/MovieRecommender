import unittest
from Code.prediction_scripts.item_based import recommendForNewUser


class RecommendationTests(unittest.TestCase):
    """Test suite for the recommendForNewUser function in RecommenderApp.
    
    This suite includes tests for:
    - Valid and empty movie lists.
    - Handling duplicates, missing data, and edge cases.
    - Filters for rating constraints.
    - Case insensitivity and unknown movie titles.
    """

    def test_recommendation_valid_movies(self):
        """Test recommendation with a valid list of movies.
        
        Verifies that recommendations are generated when a valid movie title
        with a valid rating is provided.
        """
        movies = [{"title": "Inception (2010)", "rating": 5.0}]
        self.assertTrue(recommendForNewUser(movies), "Expected recommendations")

    def test_recommendation_empty_movies(self):
        """Test recommendation with an empty movie list.
        
        Verifies that an empty list is returned when no movies are provided.
        """
        movies = []
        self.assertEqual(recommendForNewUser(movies), [], "Expected no recommendations")

    def test_recommendation_duplicate_movies(self):
        """Test recommendation with duplicate movie entries.
        
        Verifies that recommendations do not duplicate the user's rated movies.
        """
        movies = [{"title": "Inception (2010)", "rating": 5.0}, {"title": "Inception (2010)", "rating": 5.0}]
        self.assertTrue(recommendForNewUser(movies), "Expected recommendations without duplicates")

    def test_recommendation_missing_rating(self):
        """Test recommendation with a missing rating.
        
        Expects a KeyError if the 'rating' key is missing from any movie entry.
        """
        movies = [{"title": "Inception (2010)"}]
        self.assertRaises(KeyError, recommendForNewUser, movies)

    def test_recommendation_high_rating_filter(self):
        """Test recommendation with a rating above the valid range.
        
        Provides a movie rating of 9.0 (out of range) and expects no recommendations.
        """
        movies = [{"title": "Inception (2010)", "rating": 9.0}]
        self.assertEqual(recommendForNewUser(movies), [], "Expected no recommendations for out-of-range rating")

    def test_recommendation_low_rating_filter(self):
        """Test recommendation with a low valid rating.
        
        Provides a low rating (1.0) and expects valid recommendations based on that rating.
        """
        movies = [{"title": "Inception (2010)", "rating": 1.0}]
        self.assertTrue(recommendForNewUser(movies), "Expected recommendations for low rating filter")

    def test_recommendation_invalid_movie_format(self):
        """Test recommendation with an invalid movie entry format.
        
        Expects a TypeError if movie entries are not dictionaries.
        """
        movies = ["Inception (2010)"]
        self.assertRaises(TypeError, recommendForNewUser, movies)

    def test_recommendation_incomplete_movie_data(self):
        """Test recommendation with incomplete movie data.
        
        Expects a KeyError if a movie entry lacks the 'title' key.
        """
        movies = [{"rating": 5.0}]
        self.assertRaises(KeyError, recommendForNewUser, movies)

    def test_recommendation_case_insensitivity(self):
        """Test recommendation with case-insensitive movie titles.
        
        Verifies that recommendations are case-insensitive by using a lowercase title.
        """
        movies = [{"title": "inception (2010)", "rating": 5.0}]
        self.assertTrue(recommendForNewUser(movies), "Expected recommendations with case-insensitive title")

    def test_recommendation_no_valid_recommendations(self):
        """Test recommendation with an unknown movie title.
        
        Provides an unknown movie title and expects no recommendations.
        """
        movies = [{"title": "Unknown Movie (2022)", "rating": 5.0}]
        self.assertEqual(recommendForNewUser(movies), [], "Expected no recommendations for unknown movies")

    def test_recommendation_invalid_rating_value(self):
        """Test recommendation with invalid rating values.
        
        Provides a list with ratings out of the valid range (0.0-5.0) and expects an empty result.
        """
        movies = [{"title": "Inception (2010)", "rating": -1.0}, {"title": "Interstellar (2014)", "rating": 6.0}]
        self.assertEqual(recommendForNewUser(movies), [], "Expected no recommendations due to invalid rating values")

    def test_recommendation_long_movie_title(self):
        """Test recommendation with a very long movie title.
        
        Expects no recommendations if any movie title exceeds the max length (255 characters).
        """
        long_title = "A" * 256  # Generate a title longer than 255 characters
        movies = [{"title": long_title, "rating": 5.0}]
        self.assertEqual(recommendForNewUser(movies), [], "Expected no recommendations for overly long title")

    def test_recommendation_remove_user_rated_movies(self):
        """Test recommendation filtering out already rated movies.
        
        Provides a list of user-rated movies and checks if recommendations exclude them.
        """
        movies = [{"title": "Inception (2010)", "rating": 4.0}]
        recommendations = recommendForNewUser(movies)
        self.assertNotIn("Inception (2010)", recommendations, "Expected user-rated movies to be excluded from recommendations")

if __name__ == "__main__":
    unittest.main()
