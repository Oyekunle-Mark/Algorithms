#!/usr/bin/python

import sys


def making_change(amount, denominations):
    """Implementation of the making change algorithm

    Arguments:
        amount {int} -- amount in cent
        denominations {list} -- changes available

    Returns:
        int -- possible change that can be made
    """
    # [1, 5, 10, 25, 50] -> provided denominations

    # initialize a variable to an empty array to hold the possible number of ways to make change
    combinations = []

    # create the function to create the combinations
    def find_possible_change(amount_of_change, changes):
        # state a base case
        if amount_of_change == 0:
            # add changes to combinations
            # sort the changes for purpose of comparison later on
            combinations.append(sorted(changes))
            return

        # check if the change adds up to amount
        # if it does store the change and return
        if sum(changes) == amount:
            # sort the changes and check if it has been computed previously.
            # if it has not been computed, add it to the combinations
            if sorted(changes) not in combinations:
                combinations.append(sorted(changes))
            return

        # for change in denominations
        for change in denominations:
            # if sum of changes is up to or sum of changes plus change is greater than amount return
            if sum(changes) == amount or sum(changes) + change > amount:
                return

            # call recursive functions for amount - 1 and pass in array to hold changes
            find_possible_change(amount_of_change - 1, changes + [change])

    # call function
    find_possible_change(amount, [])

    # return length of result
    return len(combinations)


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
