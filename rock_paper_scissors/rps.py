#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    """Rock paper scissors recursive algorithm

    Arguments:
            n {int} -- number of combination

    Returns:
            list -- the generated combination
    """
    # the keywords
    keyWords = ['rock', 'paper', 'scissors']
    # will hold the combinations
    result = []
    turns = n

    # will generate the combinations
    def generateCombinations(turnsLeft, game):
        # base case
        if turnsLeft == 0:
            # Add the combinations to the result array
            result.append(game)
            return

        # Use every word in the keyword
        for i in keyWords:
            # recursive case
            generateCombinations(turnsLeft - 1, game + [i])

    # call the function with an empty array
    generateCombinations(turns, [])

    return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
