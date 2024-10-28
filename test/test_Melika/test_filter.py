import unittest
import warnings
import sys
import os

sys.path.append("../")
from Code.recommenderapp.filter import Filter

warnings.filterwarnings("ignore")

class Tests(unittest.TestCase):
    # Test 1
    def testFilterAdventure(self):
        search_word = "Adventure"
        search = Filter()
        filtered_dict = search.resultsTop10(search_word)
        expected_resp = [
            "Toy Story (1995)",
            "Jumanji (1995)",
            "Tom and Huck (1995)",
            "GoldenEye (1995)",
            "Balto (1995)",
            "Cutthroat Island (1995)",
            "City of Lost Children, The (Cité des enfants perdus, La) (1995)",
            "Mortal Kombat (1995)",
            "Lamerica (1994)",
            "Indian in the Cupboard, The (1995)"
        ]
        self.assertTrue(filtered_dict == expected_resp)

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

    # Test 6
    def testFilterRomance(self):
        search_word = "Romance"
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
    
    # Ratings
    # Test 1
    def testRate5(self):
        rate = 5
        search = Filter()
        filtered_dict = search.resultsTop10rate(rate)
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

    # Test 2
    def testRate5(self):
        rate = 4
        search = Filter()
        filtered_dict = search.resultsTop10rate(rate)
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
    def testRate5(self):
        rate = 3
        search = Filter()
        filtered_dict = search.resultsTop10rate(rate)
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
    def testRate5(self):
        rate = 2
        search = Filter()
        filtered_dict = search.resultsTop10rate(rate)
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