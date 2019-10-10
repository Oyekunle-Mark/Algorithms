#!/usr/bin/python

import argparse


def find_max_profit(prices):
    """Find the max profit from a list of prices

    Arguments:
        prices {list} -- list of prices as integer

    Returns:
        int -- maximum profit obtainable
    """
    # set a default profit of second price minus first price
    max_profit = prices[1] - prices[0]
    prices_len = len(prices)

    # find the difference between each price and the price that comes before
    for i in range(0, prices_len):
        for j in range(0, i):
            profit = prices[i] - prices[j]

            if profit > max_profit:
                max_profit = profit

    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
