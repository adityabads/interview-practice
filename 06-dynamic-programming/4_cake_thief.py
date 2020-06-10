# Cake thief
# Each type of cake has a weight and a value and is represented as a tuple
# (weight, value). You brought a duffel bag that can hold limited weight, and
# you want to make off with the most valuable haul possible.
#
# Write a function max_duffel_bag_value() that takes a list of cake type tuples
# and a weight capacity, and returns the maximum monetary value the duffel bag
# can hold.
#
# EXAMPLE
# Input:  [(7, 160), (3, 90), (2, 15)], 20
# Output: 555
# (6 of the middle type of cake and 1 of the last type of cake)
#
# Weights and values may be any non-negative integer.
#
# BONUS
# 1. We know the max value we can carry, but which cakes should we take, and
# how many? Try adjusting your answer to return this information as well.
#
# 2. What if we check to see if all the cake weights have a common denominator?
# Can we improve our algorithm?
#
# 3. A cake that's both heavier and worth less than another cake would never be
# in the optimal solution. This idea is called dominance relations. Can you
# apply this idea to save some time? Hint: dominance relations can apply to
# sets of cakes, not just individual cakes.
#
# 4. What if we had a tuple for every individual cake instead of types of
# cakes? So now there's not an unlimited supply of a type of cake—there's
# exactly one of each. This is a similar but harder problem, known as the
# 0/1 Knapsack problem.

from typing import Dict, List, Tuple
import unittest


def max_value_recursive(types: List[Tuple[int, int]], capacity: int) -> int:
    if capacity < 0:
        return 0
    if any([weight == 0 and value > 0 for weight, value in types]):
        return float("inf")
    maxval = 0
    for weight, value in types:
        if weight <= capacity and value > 0:
            maxval = max(maxval, max_value_recursive(
                types, capacity-weight) + value)
    return maxval


def max_value_memo(types: List[Tuple[int, int]], capacity: int, memo: Dict[int, int] = None) -> int:
    if capacity < 0:
        return 0
    if any([weight == 0 and value > 0 for weight, value in types]):
        return float("inf")
    if not memo:
        memo = {}
    maxval = 0
    for weight, value in types:
        if weight <= capacity and value > 0:
            if capacity-weight not in memo:
                memo[capacity - weight] = max_value_recursive(
                    types, capacity-weight)
            maxval = max(maxval, memo[capacity-weight] + value)
    return maxval


def max_value_dp(types: List[Tuple[int, int]], capacity: int) -> int:
    if capacity < 0:
        return 0
    if any([weight == 0 and value > 0 for weight, value in types]):
        return float("inf")
    values = [0] * (capacity + 1)
    for weight, value in types:
        for i in range(weight, capacity+1):
            values[i] = max(values[i], values[i-weight] + value)
    return values[capacity]


class TestCakeThief(unittest.TestCase):
    def test_max_value(self):
        tests = [
            [[(7, 160), (3, 90), (2, 15)], 20, 555],
            [[(7, 160), (3, 90), (2, 15)], 0, 0],
            [[(7, 160), (3, 90), (2, 15), (5, 0)], 20, 555],
            [[(7, 160), (3, 90), (2, 15), (0, 0)], 20, 555],
            [[(7, 160), (3, 90), (2, 15), (0, 0.1)], 20, float("inf")],
        ]
        for types, capacity, value in tests:
            with self.subTest(types=types, capacity=capacity):
                self.assertEqual(max_value_recursive(types, capacity), value)
                self.assertEqual(max_value_memo(types, capacity), value)
                self.assertEqual(max_value_dp(types, capacity), value)


if __name__ == "__main__":
    unittest.main()
