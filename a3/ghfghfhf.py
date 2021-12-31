"""Generating a random story.
"""

from typing import List, Dict, TextIO
import random


def generate_random_story(data_file: TextIO, context_size: int,
                          num_words: int) -> str:
    """Return a randomly generated story with num_words words based on a
    context of context_size words from the text in data_file.
    """

    pass


def read_words(data_file: TextIO) -> List[str]:
    """Return a list of words from data_file. Words are defined as all
    strings delimited by whitespace.
    """
    word_list = data_file.readlines()
    return word_list


def build_context_to_words(word_list: List[str],
                           context_size: int) -> Dict[tuple, List[str]]:
    """Return a dictionary where each key is a tuple of context_size
    adjacent words from word_list, and each corresponding value is a
    list of words that immediately follow these adjacent words in
    word_list.

    >>> context_to_words = build_context_to_words(
    ...    ['to', 'be', 'or', 'not', 'to', 'be', 'that'], 2)
    >>> context_to_words == {('to', 'be'): ['or', 'that'],
    ...                      ('be', 'or'):['not'],
    ...                      ('or', 'not'):['to'],
    ...                      ('not', 'to'): ['be']}
    True
    >>> context_to_words = build_context_to_words(
    ...    ['to', 'be', 'or', 'not', 'to', 'be', 'or'], 2)
    >>> context_to_words == {('to', 'be'): ['or', 'or'],  # another decision!
    ...                      ('be', 'or'):['not'],
    ...                      ('or', 'not'):['to'],
    ...                      ('not', 'to'): ['be']}
    True
    """
    context_to_words = {}
    num = context_size
    
    for i in range(len(word_list)):
        a = ()
        
        for j in range(num):
            a += word_list(j+i)
        
        context_to_words[a] = []
        




def generate_story(context_to_words: Dict[tuple, List[str]],
                   num_words: int) -> str:
    """Return a randomly generated story with num_words words based on
    context_to_words.
    """

    pass


if __name__ == '__main__':

    #import doctest
    # doctest.testmod()

    # with open('small.txt') as small:
    #    print(generate_random_story(small, 2, 10))

    # filename = input('Enter a filename: ')
    # with open(filename) as training_file:
    #     print(generate_random_story(training_file, 2, 50))
    pass