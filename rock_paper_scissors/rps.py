#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    # the keywords
    keyWords = ['rock', 'paper', 'scissors']
    # will hold the combinations
    result = []
    turns = n

    def generateCombinations(turnsLeft, game):
        # base case
        if turnsLeft == 0:
            result.append(game)
            return

        for i in keyWords:
            # recursive case
            generateCombinations(turnsLeft - 1, game + [i])

    generateCombinations(turns, [])
    return result


print(rock_paper_scissors(2))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
