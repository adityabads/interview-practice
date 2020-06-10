# Making change
# Write a function that, given an amount of money and a list of coin denominations,
# computes the number of ways to make the amount of money with coins of the
# available denominations.
#
# EXAMPLE
# Input:  4, [1, 2, 3]
# Output: 4
# Since there are 4 combinations: {1, 1, 1, 1}, {1, 1, 2}, {1, 3}, {2, 2}

from typing import Dict, List
import unittest


def make_change_recursive(amount: int, denominations: List[int]) -> int:
    minval = min(denominations)
    if amount < minval:
        return 0
    elif amount == 0 or amount == minval:
        return 1
    return sum([make_change_recursive(amount-denomination, denominations)
                for denomination in denominations if amount >= denomination])


def make_change_memo(amount: int, denominations: List[int], memo: Dict[int, int] = None) -> int:
    minval = min(denominations)
    if amount < minval:
        return 0
    elif amount == 0 or amount == minval:
        return 1
    if memo is None:
        memo = {}

    total = 0
    for denomination in denominations:
        if amount-denomination not in memo:
            memo[amount-denomination] = make_change_memo(
                amount-denomination, denominations, memo)
        total += memo[amount-denomination]
    return total


def make_change_dp(amount: int, denominations: List[int]) -> int:
    ways = [0] * (amount+1)
    ways[0] = 1
    for denomination in denominations:
        for i in range(denomination, amount+1):
            ways[i] += ways[i-denomination]
    return ways[amount]


class TestMakingChange(unittest.TestCase):
    def test_make_change(self):
        tests = [
            [4, [1, 2, 3], 4]
        ]
        for amount, denominations, expected in tests:
            self.assertEqual(make_change_recursive(
                amount, denominations), expected)
            self.assertEqual(make_change_memo(
                amount, denominations), expected)
            self.assertEqual(make_change_dp(
                amount, denominations), expected)


if __name__ == "__main__":
    unittest.main()
