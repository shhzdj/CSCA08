"""CSC108/CSCA08: Fall 2020 -- Assignment 1: Phrase Puzzler

This code is provided solely for the personal and private use of
students taking the CSC108/CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2020 Mario Badr, Jennifer Campbell, Tom Fairgrieve,
Diane Horton, Michael Liut, Jacqueline Smith, and Anya Tafliovich.

"""

from constants import (CONSONANT_POINTS, VOWEL_PRICE, CONSONANT_BONUS,
                       PLAYER_ONE, PLAYER_TWO, CONSONANT, VOWEL,
                       SOLVE, QUIT, HUMAN, HUMAN_HUMAN,
                       HUMAN_COMPUTER, EASY, HARD, ALL_CONSONANTS,
                       ALL_VOWELS, PRIORITY_CONSONANTS, HIDDEN)


# We provide this function as an example.
def is_win(puzzle: str, view: str) -> bool:
    """Return True if and only if puzzle and view are a winning
    combination. That is, if and only if puzzle and view are the same.

    >>> is_win('banana', 'banana')
    True
    >>> is_win('apple', 'a^^le')
    False
    >>> is_win('apple', 'app')
    False
    """

    return puzzle == view


# We provide this function as an example of using a function as a helper.
def is_game_over(puzzle: str, view: str, move: str) -> bool:
    """Return True if and only if puzzle and view are a winning
    combination or move is QUIT.

    >>> is_game_over('apple', 'a^^le', 'V')
    False
    >>> is_game_over('apple', 'a^^le', 'Q')
    True
    >>> is_game_over('apple', 'apple', 'S')
    True
    """

    return move == QUIT or is_win(puzzle, view)


# We provide the header and docstring of this function as an example
# of where and how to use constants in the docstring.
def is_human(current_player: str, game_type: str) -> bool:
    """Return True if and only if current_player represents a human in a
    game of type game_type.

    current_player is PLAYER_ONE or PLAYER_TWO.
    game_type is HUMAN, HUMAN_HUMAN, or HUMAN_COMPUTER.

    In a HUMAN game or a HUMAN_HUMAN game, a player is always
    human. In a HUMAN_COMPUTER game, PLAYER_ONE is human and
    PLAYER_TWO is computer.

    >>> is_human('Player One', 'H-')
    True
    >>> is_human('Player One', 'HH')
    True
    >>> is_human('Player Two', 'HH')
    True
    >>> is_human('Player One', 'HC')
    True
    >>> is_human('Player Two', 'HC')
    False
    """

    pass


# Helper.
def half_revealed(view: str) -> bool:
    """Return True if and only if at least half of the alphabetic
    characters in view are revealed.

    >>> half_revealed('')
    True
    >>> half_revealed('x')
    True
    >>> half_revealed('^')
    False
    >>> half_revealed('a^,^c!')
    True
    >>> half_revealed('a^b^^e ^c^d^^d')
    False
    """

    num_hidden = view.count(HIDDEN)
    num_alphabetic = 0
    for char in view:
        if char.isalpha():
            num_alphabetic += 1
    return num_alphabetic >= num_hidden


if __name__ == '__main__':
    import doctest
    doctest.testmod()
