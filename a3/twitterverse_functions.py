"""CSC108/A08: Fall 2020 -- Assignment 3: Twitterverse

This code is provided solely for the personal and private use of
students taking the CSC108 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2020 Mario Badr, Jennifer Campbell, Tom Fairgrieve,
Diane Horton, Michael Liut, Jacqueline Smith, and Anya Tafliovich.

"""

from typing import Callable, List, TextIO
from constants import (TwitterverseDict, SearchDict, FilterDict,
                       PresentDict, QueryDict)
from constants import (NAME, LOCATION, WEB, BIO, FOLLOWING, USERNAME,
                       OPERATIONS, FOLLOWER, FOLLOWERS, NAME_INCLUDES,
                       LOCATION_INCLUDES, SORT_BY, FORMAT, SEARCH,
                       FILTER, PRESENT, POPULARITY, END, ENDBIO, LONG)


HANDOUT_DATA = {
    'tomCruise': {
        'name': 'Tom Cruise',
        'bio': ('Official TomCruise.com crew tweets. We love you guys!\n' +
                'Visit us at Facebook!'),
        'location': 'Los Angeles, CA',
        'web': 'http://www.tomcruise.com',
        'following': ['katieH', 'NicoleKidman']},
    'PerezHilton': {
        'name': 'Perez Hilton',
        'bio': ('Perez Hilton is the creator and writer of one of the most ' +
                'famous websites\nin the world. And he also loves music -' +
                'a lot!'),
        'location': 'Hollywood, California',
        'web': 'http://www.PerezH...',
        'following': ['tomCruise', 'katieH', 'NicoleKidman']}}
MY_DATA = {
    'tomCruise': {
        'name': 'Tom Cruise', 'bio':'', 'location': 'New York', 'web': '',\
        'following':['NicoleKidman', 'RyanGosling', 'Sia']},
    'NicoleKidman': {
        'name': 'Nicole Kidman', 'bio': '', 'location': 'Los Angles', 'web':\
        '', 'following': ['tomCruise', 'Beyonce']},
    'tomHolland': {
        'name': 'Tom Holland', 'bio': '', 'location': 'Toronto', 'web': '',
        'following': ['NicoleKidman', 'RobertDowneyJr']},
    'Beyonce': {
        'name': 'Beyonce', 'bio': '', 'location': 'New York', 'web': '',\
    'following': []}}

HANDOUT_QUERY = {
    'SEARCH': {'username': 'tomCruise',
               'operations': ['following', 'followers']},
    'FILTER': {'following': 'katieH'},
    'PRESENT': {'sort-by': 'username',
                'format': 'short'}
}

############################################################################


def all_following(twitter_data: TwitterverseDict, username: str) -> List[str]:
    """Return a list of strings representing the usernames of all users
    that username is following in twitter_data.

    >>> following = all_following(HANDOUT_DATA, 'tomCruise')
    >>> set(following) == {'katieH', 'NicoleKidman'}
    True
    >>> all_following(HANDOUT_DATA, 'KatieH')
    []

    """

    all_following_list = []
    if username in twitter_data:
        all_following_list = twitter_data[username][FOLLOWING]
    return all_following_list


def process_data(file: TextIO) -> TwitterverseDict:
    """Return the data in the file in TwitterverseDict format.

    precondition: file must be open for reading.
    """

    data_dictionary = {}
    next_user = file.readline().strip()
    while next_user != "":
        user = next_user
        data_dictionary[user] = {}
        data_dictionary[user][NAME] = file.readline().strip()
        data_dictionary[user][LOCATION] = file.readline().strip()
        data_dictionary[user][WEB] = file.readline().strip()
        line = file.readline()
        bio = ''
        while line != ENDBIO + '\n':
            bio += line
            line = file.readline()
        data_dictionary[user][BIO] = bio.strip()
        following_list = []
        following_line = file.readline().strip()
        while following_line != END:
            following_list.append(following_line.strip())
            following_line = file.readline().strip()
            data_dictionary[user][FOLLOWING] = following_list
        next_user = file.readline().strip()

    return data_dictionary


def process_query(file: TextIO) -> QueryDict:
    """Return the query from file in QueryDict format.

    precondition: file must be open for reading.
    """

    query_dictionary = {}
    query_dictionary[SEARCH] = {}
    query_dictionary[SEARCH][USERNAME] = file.readline().strip()
    query_dictionary[SEARCH][OPERATIONS] = []

    line = file.readline().strip()

    while line != FILTER:
        query_dictionary[SEARCH][OPERATIONS].append(line)
        line = file.readline().strip()
    query_dictionary[FILTER] = {}
    line = file.readline().strip()
    while line != PRESENT:
        filter_list = line.split()
        query_dictionary[FILTER][filter_list[0]] = filter_list[1]
        line = file.readline().strip()

    query_dictionary[PRESENT] = {}
    line = file.readline().strip()
    while line != '':
        present_list = line.split()
        query_dictionary[PRESENT][present_list[0]] = present_list[1]
        line = file.readline().strip()

    return query_dictionary

def all_followers(twitter_data: TwitterverseDict,
                  current_username: str) -> List[str]:
    """Return a list of strings representing the usernames of all users
    that current_username is followed by in twitter_data.

    >>> all_followers(HANDOUT_DATA, 'tomCruise')
    ['PerezHilton']
    >>> all_followers(HANDOUT_DATA, 'NicoleKidman')
    ['tomCruise', 'PerezHilton']
    >>> all_followers(MY_DATA, 'Beyonce')
    ['NicoleKidman']

    """
    all_followers_list = []

    for username in twitter_data:
        if current_username in twitter_data[username][FOLLOWING]:
            all_followers_list.append(username)
    return all_followers_list


def get_search_results(twitter_data: TwitterverseDict,
                       search_dict: SearchDict) -> List[str]:
    """Return a list of strings representing the username
    that match the search_dict criteria.

    >>> search_dictionary = {'username': 'PerezHilton',\
    'operations': ['following']}
    >>> get_search_results(HANDOUT_DATA, search_dictionary)
    ['tomCruise', 'katieH', 'NicoleKidman']
    >>> search_dictionary = {'username': 'PerezHilton', \
    'operations': ['follower']}
    >>> get_search_results(HANDOUT_DATA, search_dictionary)
    []
    >>> search_dictionary = HANDOUT_QUERY['SEARCH']
    >>> get_search_results(MY_DATA, search_dictionary)
    ['tomCruise', 'tomHolland']
    """

    current_username = search_dict[USERNAME]
    operations = search_dict[OPERATIONS]

    search_match_list = [current_username]
    for operation in operations:
        temp_list = []
        for item in search_match_list:
            if operation == FOLLOWING:
                temp_list.extend(all_following(twitter_data, item))
            else:
                temp_list.extend(all_followers(twitter_data, item))
        temp_list = remove_duplicates(temp_list)
        search_match_list = temp_list
    return search_match_list


def get_filter_results(twitter_data: TwitterverseDict, username_list:
                       List[str], filter_dict: FilterDict) -> List[str]:
    """Return a filtered version of username_list in twitter_data
    based on the specific criteria given in filter_dict.

    >>> username = ['PerezHilton', 'tomCruise']
    >>> filter_dictionary = HANDOUT_QUERY['FILTER']
    >>> get_filter_results(HANDOUT_DATA, username, filter_dictionary)
    ['PerezHilton', 'tomCruise']
    >>> filter_dictionary = {'following': 'tomHolland'}
    >>> get_filter_results(HANDOUT_DATA, username, filter_dictionary)
    []
    >>> username = ['tomCruise', 'NicoleKidman', 'tomHolland']
    >>> filter_dictionary = {'following': 'NicoleKidman', \
    'location-includes': 'New York'}
    >>> get_filter_results(MY_DATA, username, filter_dictionary)
    ['tomCruise']

    """

    filter_list = username_list.copy()

    if len(filter_dict) > 0:
        for key in filter_dict:
            filter_list = filter_by_specification(twitter_data, filter_list,\
                                                  filter_dict, key)
    return filter_list


def get_present_string(twitter_data: TwitterverseDict, username_list:
                       List[str], present_dict: PresentDict) -> str:
    """Return a formated string of username_list in twitter_data for
    presentation based on the given criteria on present_dict.

    Precondition: present_dict[SORT_BY] can be USERNAME, NAME AND POPULARITY
    >>> username = [ 'tomCruise', 'PerezHilton']
    >>> present_dict = HANDOUT_QUERY['PRESENT']
    >>> get_present_string(HANDOUT_DATA, username, present_dict)
    "['PerezHilton', 'tomCruise']"
    >>> present_dict = {'sort-by': 'popularity', 'format': 'short'}
    >>> get_present_string(HANDOUT_DATA, username, present_dict)
    "['tomCruise', 'PerezHilton']"

    """
    if present_dict[SORT_BY] == USERNAME:
        tweet_sort(twitter_data, username_list, USERNAME)
    elif present_dict[SORT_BY] == NAME:
        tweet_sort(twitter_data, username_list, NAME)
    elif present_dict[SORT_BY] == POPULARITY:
        tweet_sort(twitter_data, username_list, POPULARITY)

    result = format_report(twitter_data, username_list, present_dict[FORMAT])
    return result


############################################################################
# Provided helper functions
############################################################################
def filter_by_specification(twitter_data: TwitterverseDict, username_list:
                            List[str], filter_dict: FilterDict,
                            key: str) -> List[str]:
    """ Return a new version of username_list from twitter_data according
    to the give key in filter_dict.

    >>> username_list = ['tomCruise', 'NicoleKidman', 'tomHolland']
    >>> filter_dict = {'following': 'Beyonce'}
    >>> key = FOLLOWING
    >>> filter_by_specification(MY_DATA, username_list,\
    filter_dict, key)
    ['NicoleKidman']

    """
    filtered_list = []
    for username in username_list:
        if key == NAME_INCLUDES and \
           filter_dict[key].lower() in username.lower():
            filtered_list.append(username)
        elif key == LOCATION_INCLUDES and filter_dict[key].lower()\
             in twitter_data[username][LOCATION].lower():
            filtered_list.append(username)
        elif key == FOLLOWER and \
             filter_dict[key] in all_followers(twitter_data, username):
            filtered_list.append(username)
        elif key == FOLLOWING and \
             filter_dict[key] in all_following(twitter_data, username):
            filtered_list.append(username)
    return filtered_list




def remove_duplicates(data_list: list) -> List[str]:
    """retun a list which does not include the duplicated items
    in the data_list

    >>> lst = ['bob', 'tom', 'tom', 'hailey']
    >>> remove_duplicates(lst)
    ['bob', 'tom', 'hailey']

    """
    filtered_list = []
    for item in data_list:
        if item not in filtered_list:
            filtered_list.append(item)
    return filtered_list

def tweet_sort(twitter_data: TwitterverseDict,
               usernames: List[str],
               sort_spec: str) -> None:
    """Sort usernames based on the sorting specification in sort_spec
    using the data in twitter_data.

    >>> usernames = ['tomCruise', 'PerezHilton']
    >>> tweet_sort(HANDOUT_DATA, usernames, 'username')
    >>> usernames == ['PerezHilton', 'tomCruise']
    True
    >>> tweet_sort(HANDOUT_DATA, usernames, 'popularity')
    >>> usernames == ['tomCruise', 'PerezHilton']
    True
    >>> tweet_sort(HANDOUT_DATA, usernames, 'name')
    >>> usernames == ['PerezHilton', 'tomCruise']
    True

    """

    usernames.sort()  # sort by username first
    if sort_spec in SORT_FUNCS:
        SORT_FUNCS[sort_spec](twitter_data, usernames)


def by_popularity(twitter_data: TwitterverseDict, usernames: List[str]) -> None:
    """Sort usernames in ascending order based on popularity in
    twitter_data.

    >>> usernames = ['PerezHilton', 'tomCruise']
    >>> by_popularity(HANDOUT_DATA, usernames)
    >>> usernames == ['tomCruise', 'PerezHilton']
    True

    """

    def get_popularity(username: str) -> int:
        return len(all_following(twitter_data, username))

    usernames.sort(key=get_popularity)


def by_name(twitter_data: TwitterverseDict, usernames: List[str]) -> None:
    """Sort usernames in ascending order based on name in twitter_data.

    >>> usernames = ['tomCruise', 'PerezHilton']
    >>> by_name(HANDOUT_DATA, usernames)
    >>> usernames == ['PerezHilton', 'tomCruise']
    True

    """

    def get_name(username: str) -> str:
        return twitter_data.get(username, {}).get(NAME, '')

    usernames.sort(key=get_name)


def format_report(twitter_data: TwitterverseDict,
                  usernames: List[str],
                  format_spec: str) -> str:
    """Return a string representing usernames presented as specified by
    the format specification format_spec.

    Precondition: each username in usernames is in twitter_data
    """

    if format_spec == LONG:
        result = '-' * 10 + '\n'
        for user in usernames:
            result += format_details(twitter_data, user)
            result += '-' * 10 + '\n'
        return result
    return str(usernames)


def format_details(twitter_data: TwitterverseDict, username: str) -> str:
    """Return a string representing the long format of username's info in
    twitter_data.

    Precondition: username is in twitter_data
    """

    user_data = twitter_data[username]
    return ("{}\nname: {}\nlocation: {}\nwebsite: {}\nbio:\n{}\n" +
            "following: {}\n").format(username, user_data[NAME],
                                      user_data[LOCATION],
                                      user_data[WEB], user_data[BIO],
                                      user_data[FOLLOWING])


############################################################################


SORT_FUNCS = {POPULARITY: by_popularity,
              NAME: by_name}


if __name__ == '__main__':
    import doctest
    doctest.testmod()
