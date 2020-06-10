# Stock prices
# I have a list called stock_prices, where the indices are the time (in minutes)
# past trade opening time, which was 9:30am local time. The values are the price
# (in US dollars) of one share of stock at that time.
#
# Write an efficient function that takes stock_prices and returns the best
# profit I could have made from one purchase and one sale of one share of Apple
# stock yesterday.
#
# No "shorting" - you need to buy before you can sell. Also, you can't buy and
# sell in the same time step—at least 1 minute has to pass.
#
# EXAMPLE
# Input:  [10, 7, 5, 8, 11, 9]
# Output: 6 (buying for $5 and selling for $11)

from typing import List
import unittest


def max_increase(arr: List[int]) -> int:
    if len(arr) < 2:
        return 0
    minval = arr[0]
    maxprofit = -float("inf")
    for i in range(1, len(arr)):
        if arr[i] - minval > maxprofit:
            maxprofit = arr[i] - minval
        if arr[i] < minval:
            minval = arr[i]
    return maxprofit


class TestStockPrices(unittest.TestCase):
    def test_max_increase(self):
        tests = [
            [[10, 7, 5, 8, 11, 9], 6],
            [[10, 7, 5], -2]
        ]
        for prices, expected in tests:
            self.assertEqual(max_increase(prices), expected)


if __name__ == "__main__":
    unittest.main()
