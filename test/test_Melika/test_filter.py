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
        expected_resp = ['Toy Story (1995)', 'Jumanji (1995)', 
                         'Tom and Huck (1995)', 'GoldenEye (1995)', 
                         'Balto (1995)', 'Cutthroat Island (1995)', 
                         'City of Lost Children, The (Cité des enfants perdus, La) (1995)', 
                         'Mortal Kombat (1995)', 'Lamerica (1994)', 
                         'Indian in the Cupboard, The (1995)']
        self.assertTrue(filtered_dict == expected_resp)

    # Test 2
    def testFilterAnimation(self):
        search_word = "Animation"
        search = Filter()
        filtered_dict = search.resultsTop10(search_word)
        expected_resp = ['Toy Story (1995)', 'Balto (1995)', 'Pocahontas (1995)', 
                        'Goofy Movie, A (1995)', 'Swan Princess, The (1994)', 
                        'Lion King, The (1994)', 'Nightmare Before Christmas, The (1993)',
                        'Pagemaster, The (1994)', 'Aladdin (1992)', 
                        'Snow White and the Seven Dwarfs (1937)']
        self.assertTrue(filtered_dict == expected_resp)
    
    # Test 3
    def testFilterChildren(self):
        search_word = "Children"
        search = Filter()
        filtered_dict = search.resultsTop10(search_word)
        expected_resp = ['Toy Story (1995)', 'Jumanji (1995)', 
                         'Tom and Huck (1995)', 'Balto (1995)', 
                         'Now and Then (1995)', 'Babe (1995)', 
                         'It Takes Two (1995)', 'Pocahontas (1995)', 
                         'Big Green, The (1995)', 'Indian in the Cupboard, The (1995)']
        self.assertTrue(filtered_dict == expected_resp)

    # Test 4
    def testFilterComedy(self):
        search_word = "Comedy"
        search = Filter()
        filtered_dict = search.resultsTop10(search_word)
        expected_resp = ['Toy Story (1995)', 'Grumpier Old Men (1995)', 
                         'Waiting to Exhale (1995)', 'Father of the Bride Part II (1995)',
                           'Sabrina (1995)', 'American President, The (1995)', 
                           'Dracula: Dead and Loving It (1995)', 'Four Rooms (1995)', 
                           'Ace Ventura: When Nature Calls (1995)', 'Money Train (1995)']
        self.assertTrue(filtered_dict == expected_resp)
    
    # Test 5
    def testFilterFantasy(self):
        search_word = "Fantasy"
        search = Filter()
        filtered_dict = search.resultsTop10(search_word)
        expected_resp = ['Toy Story (1995)', 'Jumanji (1995)', 
                         'City of Lost Children, The (Cité des enfants perdus, La) (1995)', 
                         'Mortal Kombat (1995)', 'Indian in the Cupboard, The (1995)', 
                         'NeverEnding Story III, The (1994)', 'Prophecy, The (1995)',
                           'Reckless (1995)', 'Three Wishes (1995)', 'Gordy (1995)']
        self.assertTrue(filtered_dict == expected_resp)

    # Test 6
    def testFilterRomanceCom(self):
        search_word = ["Romance", "Comedy"]
        search = Filter()
        filtered_dict = search.resultsTop10(search_word)
        expected_resp = ['Grumpier Old Men (1995)', 'Waiting to Exhale (1995)', 
                         'Sabrina (1995)', 'American President, The (1995)', 
                         'Clueless (1995)', 'Mighty Aphrodite (1995)', 
                         'Postman, The (Postino, Il) (1994)', 
                         'Two if by Sea (1996)', 'French Twist (Gazon maudit) (1995)', 
                         'Vampire in Brooklyn (1995)']
        self.assertTrue(filtered_dict == expected_resp)
    
    # Test 7
    def testFilterAF(self):
        search_word = ["Action", "Fantasy"]
        search = Filter()
        filtered_dict = search.resultsTop10(search_word)
        expected_resp = ['Mortal Kombat (1995)', 'Crow, The (1994)',
                        'Mask, The (1994)', 'Street Fighter (1994)',
                        'Highlander III: The Sorcerer (a.k.a. Highlander: The Final Dimension) (1994)', 
                        'Last Action Hero (1993)', 'Shadow, The (1994)', 'Super Mario Bros. (1993)', 
                        'Pagemaster, The (1994)', 'Dragonheart (1996)']
        self.assertTrue(filtered_dict == expected_resp)

    # Test 8
    # Less than 10 values are returned
    def testFilterRomanceFT(self):
        search_word = ["Romance", "Fantasy", "Thriller"]
        search = Filter()
        filtered_dict = search.resultsTop10(search_word)
        expected_resp = ['Ghost (1990)', "Dracula (Bram Stoker's Dracula) (1992)", 
                         'King Kong (1976)', 'Dragonfly (2002)', 
                         'Survive Style 5+ (2004)', 'Twilight (2008)', 
                         'Aelita: The Queen of Mars (Aelita) (1924)', 
                         'Twilight Saga: New Moon, The (2009)', 
                         'Twilight Saga: Eclipse, The (2010)']
        self.assertTrue(filtered_dict == expected_resp)

    # Ratings
    # Test 1
    def testRate5(self):
        rate = 5
        search = Filter()
        filtered_dict = search.resultsTop10rate(rate)
        expected_resp = 
        [
            "Toy Story (1995)"
            "Grumpier Old Men (1995)",
            "Heat (1995)",
            "Seven (a.k.a. Se7en) (1995)",
            "Usual Suspects, The (1995)",
            "From Dusk Till Dawn (1996)",
            "Bottle Rocket (1996)",
            "Braveheart (1995)",
            "Rob Roy (1995)",
            "Canadian Bacon (1995)"
        ]
        self.assertTrue(filtered_dict == expected_resp)

    # Test 2
    def testRate4(self):
        rate = 4
        search = Filter()
        filtered_dict = search.resultsTop10rate(rate)
        expected_resp = [
            "Toy Story (1995)"
            "Grumpier Old Men (1995)",
            "Heat (1995)",
            "From Dusk Till Dawn (1996)",
            "Braveheart (1995)",
            "Clerks (1994)",
            "Ed Wood (1994)",
            "Pulp Fiction (1994)",
            "Stargate (1994)",
            "Clear and Present Danger (1994)"
        ]
        self.assertTrue(filtered_dict == expected_resp)

    # Test 3
    def testRate3(self):
        rate = 3
        search = Filter()
        filtered_dict = search.resultsTop10rate(rate)
        expected_resp = [
            "From Dusk Till Dawn (1996)",
            "Clerks (1994)",
            "Pulp Fiction (1994)",
            "Stargate (1994)",
            "Blown Away (1994)",
            "Mrs. Doubtfire (1993)",
            "Mission: Impossible (1996)",
            "Space Jam (1996)",
            "Twister (1996)",
            "Independence Day (a.k.a. ID4) (1996)"
        ]
        self.assertTrue(filtered_dict == expected_resp)

    # Test 4
    def testRate2(self):
        rate = 2
        search = Filter()
        filtered_dict = search.resultsTop10rate(rate)
        expected_resp = [
            "Psycho (1960)",
            "Toys (1992)",
            "I Still Know What You Did Last Summer (1998)",
            "Psycho (1998)",
            "Mummy, The (1999)",
            "Talented Mr. Ripley, The (1999)",
            "The Drop (2014)",
            "Dangerous Minds (1995)",
            "Schindler's List (1993)",
            "Courage Under Fire (1996)"
        ]
        self.assertTrue(filtered_dict == expected_resp)

if __name__ == "__main__":
    unittest.main()