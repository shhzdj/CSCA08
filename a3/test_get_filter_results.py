import unittest
import twitterverse_functions as tf



class TestGetFilterResults(unittest.TestCase):
    '''Your unittests here'''
    
    def test_no_filter(self):
        """ Test the function with empty filter_dict """
        twitterverse_dict = {
            'tomCruise':{'name': 'Tom Cruise', 'bio': '', 'location': '',\
                         'web': '','following': []},
            'NicoleKidman': {'name': 'Nicole Kidman', 'bio': '', 'location':\
                             '', 'web': '', 'following': []}, 
            'tomHolland':{'name': 'Tom Holland', 'bio': '', 'location': '',\
                          'web': '', 'following': []}}

        username_list = ['tomCruise', 'NicoleKidman', 'tomHolland']
        filter_dict = {}
        expected = ['tomCruise', 'NicoleKidman', 'tomHolland']
        actual = tf.get_filter_results(twitterverse_dict, username_list,\
                                       filter_dict)
        
        msg = message("tf.get_filter_results(twitterverse_dict, username_list,\
                                filter_dict)", str(expected), str(actual))
        self.assertEqual(actual, expected, msg)        

    
        
    def test_filter_no_username_list(self):
        """ Test the function where username_list is empty """
        twitterverse_dict = {
            'tomCruise':{'name': 'Tom Cruise', 'bio': '', 'location':\
                         'New York', 'web': '', 'following': ['justineBieber']},
            'NicoleKidman': {'name': 'Nicole Kidman', 'bio': '', 'location':\
                        'Los Angles', 'web': '', 'following': ['TomHanks']}, 
            'tomHolland':{'name': 'Tom Holland', 'bio': '', 'location':\
                          'Toronto', 'web': '', 'following': []}}
        username_list = []
        filter_dict = {'location-includes': 'Paris'}
        expected = []
        actual = tf.get_filter_results(twitterverse_dict, username_list,\
                                       filter_dict)
    
        msg = message("tf.get_filter_results(twitterverse_dict, username_list,\
                                filter_dict)", str(expected), str(actual))
        self.assertEqual(actual, expected, msg)    
       

    def test_filter_name_includes(self):
        """ Test the function with name-include filter """
        twitterverse_dict = {
            'tomCruise':{'name': 'Tom Cruise', 'bio': '', 'location': 'Paris',\
                         'web': '', 'following': ['justineBieber', 'TomHanks']},
            'NicoleKidman': {'name': 'Nicole Kidman', 'bio': '', 'location': ''\
                             , 'web': '', 'following': ['TomHanks']}, 
            'tomHolland':{'name': 'Tom Holland', 'bio': '', 'location':\
                          'Toronto', 'web': '', 'following': []}}
        username_list = ['tomCruise', 'NicoleKidman', 'tomHolland']
        filter_dict = {'name-includes': 'tom'}
        expected = ['tomCruise', 'tomHolland']
        actual = tf.get_filter_results(twitterverse_dict, username_list,\
                                       filter_dict)
    
        msg = message("tf.get_filter_results(twitterverse_dict, username_list,\
                                filter_dict)", str(expected), str(actual))
        self.assertEqual(actual, expected, msg)
    
    def test_filter_name_not_found(self):
        """ Test the function where name-includes filter does not apply 
        to any username """
        twitterverse_dict = {
            'tomCruise':{'name': 'Tom Cruise', 'bio': '', 'location': 'Paris',\
                         'web': '', 'following': ['justineBieber', 'TomHanks']},
            'NicoleKidman': {'name': 'Nicole Kidman', 'bio': '', 'location':\
                             '', 'web': '', 'following': ['TomHanks']}, 
            'tomHolland':{'name': 'Tom Holland', 'bio': '', 'location':\
                          'Toronto', 'web': '', 'following': []}}

        username_list = ['tomCruise', 'NicoleKidman', 'tomHolland']
        filter_dict = {'name-includes': 'ladygaga'}
        expected = []
        actual = tf.get_filter_results(twitterverse_dict, username_list,\
                                       filter_dict)
    
        msg = message("tf.get_filter_results(twitterverse_dict, username_list,\
                                filter_dict)", str(expected), str(actual))
        self.assertEqual(actual, expected, msg)    
     
          

    def test_filter_location_includes(self):
        """ Test the function with location-includes filter """
        twitterverse_dict = {
            'tomCruise':{'name': 'Tom Cruise', 'bio': '', 'location': \
                        'New York', 'web': '', 'following':\
                        ['justineBieber', 'TomHanks']},
            'NicoleKidman': {'name': 'Nicole Kidman', 'bio': '', 'location':\
                             'Los Angles', 'web': '', 'following': []}, 
                             'tomHolland':{'name': 'Tom Holland', 'bio': '',\
            'location': 'Toronto', 'web': '', 'following': ''}}

        username_list = ['tomCruise', 'NicoleKidman', 'tomHolland']
        filter_dict = {'location-includes': 'Toronto'}
        expected = ['tomHolland']
        actual = tf.get_filter_results(twitterverse_dict, username_list,\
                                       filter_dict)
    
        msg = message("tf.get_filter_results(twitterverse_dict, username_list,\
                                filter_dict)", str(expected), str(actual))
        self.assertEqual(actual, expected, msg)  
        
    def test_filter_no_location_found(self):
        """ Test the function where location-includes filter does not apply 
        to any username """
        twitterverse_dict = {
            'tomCruise':{'name': 'Tom Cruise', 'bio': '', 'location':\
                         'New York', 'web': '', 'following': ['justineBieber']},
            'NicoleKidman': {'name': 'Nicole Kidman', 'bio': '', 'location':\
                        'Los Angles', 'web': '', 'following': ['TomHanks']}, 
            'tomHolland':{'name': 'Tom Holland', 'bio': '', 'location':\
                          'Toronto', 'web': '', 'following': []}}

        username_list = ['tomCruise', 'NicoleKidman', 'tomHolland']
        filter_dict = {'location-includes': 'Paris'}
        expected = []
        actual = tf.get_filter_results(twitterverse_dict, username_list,\
                                       filter_dict)

        msg = message("tf.get_filter_results(twitterverse_dict, username_list,\
                                filter_dict)", str(expected), str(actual))
        self.assertEqual(actual, expected, msg)    
        
    def test_filter_follower(self):
        """ Test the function with follower filter """
        twitterverse_dict = {
            'tomCruise':{'name': 'Tom Cruise', 'bio': '', 'location':\
                         'New York', 'web': '', 'following':\
                         ['NicoleKidman', 'RyanGosling', 'Sia']},
            'NicoleKidman': {'name': 'Nicole Kidman', 'bio': '', 'location':\
                             'Los Angles', 'web': '', 'following':\
                             ['tomCruise', 'Beyonce']}, 
            'tomHolland':{'name': 'Tom Holland', 'bio': '', 'location':\
                          'Toronto', 'web': '', 'following':\
                          ['NicoleKidman', 'RobertDowneyJr']}}

        username_list = ['tomCruise', 'NicoleKidman', 'tomHolland']
        filter_dict = {'follower': 'NicoleKidman'}
        expected = ['tomCruise']
        actual = tf.get_filter_results(twitterverse_dict, username_list,\
                                       filter_dict)
        msg = message("tf.get_filter_results(twitterverse_dict, username_list,\
                                filter_dict)", str(expected), str(actual))
        self.assertEqual(actual, expected, msg) 
        
    def test_filter_follower_not_found(self):
        """ Test the function where follower filter does not apply 
        to any username """
        twitterverse_dict = {
            'tomCruise':{'name': 'Tom Cruise', 'bio': '', 'location':\
                         'New York', 'web': '', 'following':\
                         ['NicoleKidman', 'RyanGosling', 'Sia']},
            'NicoleKidman': {'name': 'Nicole Kidman', 'bio': '', 'location':\
                             'Los Angles', 'web': '', 'following':\
                             ['tomCruise', 'Beyonce']}, 
            'tomHolland':{'name': 'Tom Holland', 'bio': '', 'location':\
                          'Toronto', 'web': '', 'following': ['NicoleKidman',\
                                                        'RobertDowneyJr']}}

        username_list = ['tomCruise', 'NicoleKidman', 'tomHolland']
        filter_dict = {'follower': 'James'}
        expected = []
        actual = tf.get_filter_results(twitterverse_dict, username_list,\
                                       filter_dict)

        msg = message("tf.get_filter_results(twitterverse_dict, username_list,\
                                filter_dict)", str(expected), str(actual))
        self.assertEqual(actual, expected, msg)

    def test_filter_following(self):
        """ Test the function with following filter """
        twitterverse_dict = {
            'tomCruise':{'name': 'Tom Cruise', 'bio': '', 'location':\
                         'New York', 'web': '', 'following': ['NicoleKidman',\
                                                        'RyanGosling', 'Sia']},
            'NicoleKidman': {'name': 'Nicole Kidman', 'bio': '', 'location':\
                             'Los Angles', 'web': '', 'following':\
                            ['tomCruise', 'Beyonce']}, 
            'tomHolland':{'name': 'Tom Holland', 'bio': '', 'location':\
                          'Toronto', 'web': '', 'following':\
                          ['NicoleKidman', 'RobertDowneyJr', 'Beyonce']},
            'Beyonce':{'name': 'Beyonce', 'bio': '', 'location': 'New York',\
                       'web': '', 'following': []}}
                             
        username_list = ['tomCruise', 'NicoleKidman', 'tomHolland']
        filter_dict = {'following': 'Beyonce'}
        expected = ['NicoleKidman', 'tomHolland']
        actual = tf.get_filter_results(twitterverse_dict, username_list,
                                       filter_dict)
        msg = message("tf.get_filter_results(twitterverse_dict, username_list,\
                                filter_dict)", str(expected), str(actual))
        self.assertEqual(actual, expected, msg)
    
    def test_filter_following_not_found(self):
        """ Test the function where follower filter does not apply 
        to any username """
        twitterverse_dict = {
            'tomCruise':{ 'name': 'Tom Cruise', 'bio': '', 'location':\
                          'New York', 'web': '','following': ['NicoleKidman',\
                                                        'RyanGosling', 'Sia']},
            'NicoleKidman': {'name': 'Nicole Kidman', 'bio': '', 'location':\
                             'Los Angles', 'web': '', 'following':\
                             ['tomCruise', 'Beyonce']}, 
            'tomHolland':{'name': 'Tom Holland', 'bio': '', 'location':\
                          'Toronto', 'web': '', 'following': ['NicoleKidman',\
                                                'RobertDowneyJr', 'Beyonce']},
            'Beyonce':{'name': 'Beyonce', 'bio': '', 'location': 'New York',\
                       'web': '', 'following': []}}
    
        username_list = ['tomCruise', 'NicoleKidman', 'tomHolland']
        filter_dict = {'following': 'Beyonce'}
        
        expected = ['NicoleKidman', 'tomHolland']
        actual = tf.get_filter_results(twitterverse_dict, username_list,
                                       filter_dict)
        msg = message("tf.get_filter_results(twitterverse_dict, username_list,\
                                filter_dict)", str(expected), str(actual))
        
        self.assertEqual(actual, expected, msg)


    def test_filter_with_two_filters(self):
        """ Test the function with two filters """
        twitterverse_dict = {
            'tomCruise':{'name': 'Tom Cruise', 'bio': '', 'location':\
                         'New York', 'web': '', 'following': ['NicoleKidman',\
                                                        'RyanGosling', 'Sia']},
            'NicoleKidman': {'name': 'Nicole Kidman', 'bio': '', 'location':\
                             'Los Angles', 'web': '', 'following':\
                             ['tomCruise', 'Beyonce']}, 
            'tomHolland':{'name': 'Tom Holland', 'bio': '', 'location':\
                          'Toronto', 'web': '', 'following':\
                          ['NicoleKidman', 'RobertDowneyJr']},
            'Beyonce':{'name': 'Beyonce', 'bio': '', 'location': 'New York',\
                       'web': '', 'following': []}}

        username_list = ['tomCruise', 'NicoleKidman', 'tomHolland', 'Beyonce']
        filter_dict = {'following': 'NicoleKidman', 'follower': 'NicoleKidman'}
        
        expected = ['tomCruise']
        actual = tf.get_filter_results(twitterverse_dict, username_list,\
                                       filter_dict)
        msg = message("tf.get_filter_results(twitterverse_dict, username_list,\
                                filter_dict)", str(expected), str(actual))
        
        self.assertEqual(actual, expected, msg)
        
    def test_filter_with_two_filters_more(self):
        """ Test the function with other 2 filters """
        twitterverse_dict = {
            'tomCruise':{'name': 'Tom Cruise', 'bio': '', 'location':\
                         'New York', 'web': '', 'following':\
                         ['NicoleKidman', 'RyanGosling', 'Sia']},
            'NicoleKidman': {'name': 'Nicole Kidman', 'bio': '', 'location':\
                             'Toronto', 'web': '', 'following':\
                             ['tomCruise', 'Beyonce']}, 
            'tomHolland':{'name': 'Tom Holland', 'bio': '', 'location':\
                          'New York', 'web': '', 'following':\
                          ['NicoleKidman', 'RobertDowneyJr']},
            'Beyonce':{'name': 'Beyonce', 'bio': '', 'location': 'Los Angles',\
                       'web': '', 'following': []},
            'justinBieber':{'name': 'Justin Bieber', 'bio': '', 'location':\
                            'Toronto', 'web': '', 'following':\
                            ['tomHolland', 'Beyonce', 'Sia']},
            'Sia':{'name': 'Sia', 'bio': '', 'location': 'New York', 'web': '',\
                   'following': ['Beyonce', 'RobertDowneyJr']}}
 
        username_list = ['tomCruise', 'NicoleKidman', 'tomHolland', 'Sia',\
                         'justinBieber']
        filter_dict = {'name-includes': 'Tom', 'location-includes': 'New York'}
        
        expected = ['tomCruise', 'tomHolland']
        actual = tf.get_filter_results(twitterverse_dict, username_list,
                                       filter_dict)
        msg = message("tf.get_filter_results(twitterverse_dict, username_list,\
                                filter_dict)", str(expected), str(actual))
        
        self.assertEqual(actual, expected, msg) 
        
    def test_filter_with_two_filters_empty(self):
        """ Test the function with 2 filters where no result is found """
        twitterverse_dict = {
            'tomCruise':{'name': 'Tom Cruise', 'bio': '', 'location':\
                         'New York', 'web': '', 'following': ['NicoleKidman',\
                                                    'RyanGosling', 'Sia']},
            'NicoleKidman': {'name': 'Nicole Kidman', 'bio': '', 'location':\
                             'Toronto', 'web': '', 'following': ['tomCruise',\
                                                                 'Beyonce']}, 
            'tomHolland':{'name': 'Tom Holland', 'bio': '', 'location':\
                          'Germany', 'web': '', 'following': ['NicoleKidman',\
                                                            'RobertDowneyJr']},
            'Beyonce':{'name': 'Beyonce', 'bio': '', 'location': 'New York',\
                       'web': '', 'following': []},
            'justinBieber':{'name': 'Justin Bieber', 'bio': '', 'location':\
                            'Toronto', 'web': '', 'following': ['tomHolland',\
                                                        'Beyonce', 'Sia']},
            'Sia':{'name': 'Sia', 'bio': '', 'location': 'New York', 'web': '',\
                   'following': ['Beyonce', 'RobertDowneyJr']}}
        expected = []
        username_list = ['tomCruise', 'NicoleKidman', 'tomHolland', 'Sia',\
                         'justinBieber']
        filter_dict = {'following': 'Beyonce', 'location-includes': 'Germany'}
        actual = tf.get_filter_results(twitterverse_dict, username_list,\
                                       filter_dict)
        
        msg = message("tf.get_filter_results(twitterverse_dict, username_list,\
                                filter_dict)", str(expected), str(actual))
        self.assertEqual(actual, expected, msg)    
        
    def test_filter_with_three_filters(self):
        """ Test the function with three filters """
        twitterverse_dict = {
            'tomCruise':{'name': 'Tom Cruise', 'bio': '', 'location':\
                         'New York', 'web': '', 'following': ['NicoleKidman',\
                                                        'RyanGosling', 'Sia']},
            'NicoleKidman': {'name': 'Nicole Kidman', 'bio': '', 'location':\
                             'Los Angles', 'web': '', 'following':\
                             ['tomCruise', 'Beyonce']}, 
            'tomHolland':{'name': 'Tom Holland', 'bio': '', 'location':\
                          'Germany', 'web': '', 'following': ['NicoleKidman',\
                                                            'RobertDowneyJr']},
            'Beyonce':{'name': 'Beyonce', 'bio': '', 'location': 'New York',\
                       'web': '', 'following': []},
            'justinBieber':{'name': 'Justin Bieber', 'bio': '', 'location':\
                            'Toronto', 'web': '', 'following': ['tomHolland',\
                                                            'Beyonce', 'Sia']},
            'Sia':{'name': 'Sia', 'bio': '', 'location': 'New York', 'web': '',\
                   'following': ['Beyonce', 'RobertDowneyJr']}}
                             
        username_list = ['tomCruise', 'NicoleKidman', 'tomHolland', 'Sia',\
                         'justinBieber']
        filter_dict = {'following': 'Beyonce', 'location-includes': 'New York',\
                       'follower': 'justinBieber' }
        expected = ['Sia']
        actual = tf.get_filter_results(twitterverse_dict, username_list,\
                                       filter_dict)
        
        msg = message("tf.get_filter_results(twitterverse_dict, username_list,\
                                filter_dict)", str(expected), str(actual))
        self.assertEqual(actual, expected, msg) 
        
    def test_filter_with_three_filters_more(self):
        """ Test the function with other three filter """
        twitterverse_dict = {
            'tomCruise':{'name': 'Tom Cruise', 'bio': '', 'location':\
                         'New York', 'web': '', 'following': ['NicoleKidman',\
                                                    'RyanGosling', 'Sia']},
            'NicoleKidman': {'name': 'Nicole Kidman', 'bio': '', 'location':\
                             'Los Angles', 'web': '', 'following':\
                             ['tomCruise', 'Beyonce']}, 
            'tomHolland':{'name': 'Tom Holland', 'bio': '', 'location':\
                          'Boston', 'web': '', 'following': ['NicoleKidman',\
                                                        'RobertDowneyJr']},
            'Beyonce':{'name': 'Beyonce', 'bio': '', 'location': 'Los Angles',\
                       'web': '', 'following': []},
            'justinBieber':{'name': 'Justin Bieber', 'bio': '', 'location':\
                            'Toronto', 'web': '', 'following': ['tomHolland',\
                                                            'Beyonce', ]},
            'Sia':{'name': 'Sia', 'bio': '', 'location': 'New York', 'web': '',\
                   'following': ['Beyonce', 'RobertDowneyJr']},
            'RobertDowneyJr':{'name': 'Robert Downey Jr', 'bio': '', 'location'\
                              : 'Paris', 'web': '', 'following':\
                              ['tomHolland','TomHanks']},
            'TomHanks':{'name': 'Tom Hanks', 'bio': '', 'location': 'Boston',\
                        'web': '', 'following': ['RobertDowneyJr',\
                                                 'NicoleKidman']}}

        username_list = ['tomCruise', 'NicoleKidman', 'tomHolland', 'Sia',\
                         'justinBieber', 'TomHanks', 'RobertDowneyJr']
        filter_dict = {'name-includes': 'tom', 'location-includes': 'Boston',\
                       'following': 'RobertDowneyJr' }
        expected = ['tomHolland', 'TomHanks']
        actual = tf.get_filter_results(twitterverse_dict, username_list,\
                                       filter_dict)
        
        msg = message("tf.get_filter_results(twitterverse_dict, username_list,\
                                filter_dict)", str(expected), str(actual))
        self.assertEqual(actual, expected, msg)
    
    def test_filter_with_three_filters_empty(self):
        """ Test the function with 3 filters where no result is found """
        twitterverse_dict = {
            'tomCruise':{'name': 'Tom Cruise', 'bio': '', 'location':\
                         'New York', 'web': '', 'following': ['NicoleKidman',\
                                                    'RyanGosling', 'Sia']},
            'NicoleKidman': {'name': 'Nicole Kidman', 'bio': '', 'location':\
                             'Los Angles', 'web': '', 'following':\
                             ['tomCruise', 'Beyonce']}, 
            'tomHolland':{'name': 'Tom Holland', 'bio': '', 'location':\
                          'Boston', 'web': '', 'following': ['NicoleKidman',\
                                                        'RobertDowneyJr']},
            'Beyonce':{'name': 'Beyonce', 'bio': '', 'location': 'Los Angles',\
                       'web': '', 'following': []},
            'justinBieber':{'name': 'Justin Bieber', 'bio': '', 'location':\
                            'Toronto', 'web': '', 'following': ['tomHolland',\
                                                            'Beyonce', ]},
            'Sia':{'name': 'Sia', 'bio': '', 'location': 'New York', 'web': '',\
                   'following': ['Beyonce', 'RobertDowneyJr']},
            'RobertDowneyJr':{'name': 'Robert Downey Jr', 'bio': '', 'location'\
                              : 'Paris', 'web': '', 'following':\
                              ['tomHolland','TomHanks']},
            'TomHanks':{'name': 'Tom Hanks', 'bio': '', 'location': 'Boston',\
                        'web': '', 'following': ['RobertDowneyJr',\
                                                 'NicoleKidman']}}
        username_list = ['tomCruise', 'NicoleKidman', 'tomHolland', 'Sia',\
                         'justinBieber', 'TomHanks', 'RobertDowneyJr']
        filter_dict = {'name-includes': 'tom', 'location-includes': 'Boston',\
                       'following': 'Beyonce' }
        expected = []
        actual = tf.get_filter_results(twitterverse_dict, username_list,\
                                       filter_dict)
        msg = message("tf.get_filter_results(twitterverse_dict, username_list,\
                                filter_dict)", str(expected), str(actual))
        self.assertEqual(actual, expected, msg)
        
    def test_filter_with_four_filters(self):
        """ Test the function with 4 filters """
        twitterverse_dict = {
            'tomCruise':{'name': 'Tom Cruise', 'bio': '', 'location':\
                         'New York', 'web': '', 'following': ['NicoleKidman',\
                                                    'RyanGosling', 'Sia']},
            'NicoleKidman': {'name': 'Nicole Kidman', 'bio': '', 'location':\
                             'Los Angles', 'web': '', 'following':\
                             ['tomCruise', 'Beyonce']}, 
            'tomHolland':{'name': 'Tom Holland', 'bio': '', 'location':\
                          'Boston', 'web': '', 'following': ['NicoleKidman',\
                                                            'RobertDowneyJr']},
            'Beyonce':{'name': 'Beyonce', 'bio': '', 'location': 'Los Angles',\
                       'web': '', 'following': []},
            'justinBieber':{'name': 'Justin Bieber', 'bio': '', 'location':\
                            'Toronto', 'web': '', 'following': ['tomHolland',\
                                                            'Beyonce', ]},
            'Sia':{'name': 'Sia', 'bio': '', 'location': 'New York', 'web': '',\
                   'following': ['Beyonce', 'RobertDowneyJr']},
            'RobertDowneyJr':{'name': 'Robert Downey Jr', 'bio': '',\
                              'location': 'Boston', 'web': '', 'following':\
                              ['tomHolland','TomHanks']},
            'TomHanks':{'name': 'Tom Hanks', 'bio': '', 'location': 'paris',\
                    'web': '', 'following': ['RobertDowneyJr', 'NicoleKidman']}}
                             
        username_list = ['tomCruise', 'NicoleKidman', 'tomHolland', 'Sia',\
                         'justinBieber', 'TomHanks', 'RobertDowneyJr']
        filter_dict = {'name-includes': 'robert', 'location-includes':\
                'Boston', 'following': 'TomHanks', 'follower': 'tomHolland'}
        expected = ['RobertDowneyJr']
        actual = tf.get_filter_results(twitterverse_dict, username_list,\
                                       filter_dict)
        msg = message("tf.get_filter_results(twitterverse_dict, username_list,\
                                filter_dict)", str(expected), str(actual))
        self.assertEqual(actual, expected, msg)

    def test_filter_with_four_filters_empty(self):
        """ Test the function with 4 filters where no result is found """
        twitterverse_dict = {
            'tomCruise':{'name': 'Tom Cruise', 'bio': '', 'location':\
                         'New York', 'web': '', 'following': ['NicoleKidman',\
                                                    'RyanGosling', 'Sia']},
            'NicoleKidman': {'name': 'Nicole Kidman', 'bio': '', 'location':\
                             'Los Angles', 'web': '', 'following':\
                             ['tomCruise', 'Beyonce']}, 
            'tomHolland':{'name': 'Tom Holland', 'bio': '', 'location':\
                          'Boston', 'web': '', 'following': ['NicoleKidman',\
                                                            'RobertDowneyJr']},
            'Beyonce':{'name': 'Beyonce', 'bio': '', 'location': 'Los Angles',\
                       'web': '', 'following': []},
            'justinBieber':{'name': 'Justin Bieber', 'bio': '', 'location':\
                            'Toronto', 'web': '', 'following': ['tomHolland',\
                                                            'Beyonce', ]},
            'Sia':{'name': 'Sia', 'bio': '', 'location': 'New York', 'web': '',\
                   'following': ['Beyonce', 'RobertDowneyJr']},
            'RobertDowneyJr':{'name': 'Robert Downey Jr', 'bio': '',\
                              'location': 'Boston', 'web': '', 'following':\
                              ['tomHolland','TomHanks']},
            'TomHanks':{'name': 'Tom Hanks', 'bio': '', 'location': 'paris',\
                    'web': '', 'following': ['RobertDowneyJr', 'NicoleKidman']}}
        
        username_list = ['tomCruise', 'NicoleKidman', 'tomHolland', 'Sia',\
                         'justinBieber', 'TomHanks', 'RobertDowneyJr']
        filter_dict = {'name-includes': 'justin', 'location-includes':\
                    'Boston', 'following': 'TomHanks', 'follower': 'tomHolland'}
        
        expected = []
        actual = tf.get_filter_results(twitterverse_dict, username_list,\
                                       filter_dict)
        msg = message("tf.get_filter_results(twitterverse_dict, username_list,\
                                filter_dict)", str(expected), str(actual))
        
        self.assertEqual(actual, expected, msg)

def message(test_case: str, expected: str, actual: str) -> str:
    """Return an error message for the function call test_case that
    resulted in a value actual, when the correct value is expected.
        
    """
        
    return ("When we called " + test_case + " we expected " + expected
                    + ", but got " + actual)
    
if __name__ == '__main__':
    unittest.main(exit=False)
