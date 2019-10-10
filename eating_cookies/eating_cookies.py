#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    # there is only one way of eating 0 cookie
    if n == 0:
        return 1

    # define the keywords or number to generate the combinations from
    ways_of_eating_cookies = [1, 2, 3]

    # initiate a list to hold the possible ways to eat cookies to []
    result = []

    # declare a function to find cookie eating combination
    def find_ways_of_eating_cookies(n_cookies, combo):
        # state a base case
        if n_cookies == 0:
            # add the combo to the result list and return
            result.append(combo)
            return

        # check if the sum of possible combination is n
        # if it is there is no need to continue add ways
        if sum(combo) == n:
            result.append(combo)
            return

        # for way in ways_of_eating_cookies:
        # loop through the keywords
        for way in ways_of_eating_cookies:
            # if sum of the combo adds up to n or the addition of the current way
            # will make it large than n
            # no need to go on with the recursion or loop, just return
            if sum(combo) == n or sum(combo) + way > n:
                return

            # call the recursive case for n - 1 here
            find_ways_of_eating_cookies(n_cookies - 1, combo + [way])

    # call the function to generate combination
    find_ways_of_eating_cookies(n, [])

    # return the length of the list
    return len(result)


# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_cookies = int(sys.argv[1])
#     print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
#   else:
#     print('Usage: eating_cookies.py [num_cookies]')
