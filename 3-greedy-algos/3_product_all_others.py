# Product of all other numbers
# You have a list of integers, and for each index you want to find the product
# of every integer except the integer at that index.
#
# Write a function get_products_of_all_ints_except_at_index() that takes a list
# of integers and returns a list of the products.
#
# EXAMPLE
# Input:  [1, 7, 3, 4]
# Output: [7*3*4, 1*3*4, 1*7*4, 1*7*3]
#
# Here's the catch: You can't use division in your solution!
#
# BONUS
# What if you could use division? Careful—watch out for zeroes!

from typing import List
import unittest


def get_all_products(arr: List[int]) -> List[int]:
    """Return answer"""
    n = len(arr)
    if n < 2:
        raise Exception("Input requires at least two ints")

    # rightprods[i] := product(arr[j]) s.t. j > i
    rightprods = [0] * n
    rightprods[-1] = 1
    for i in reversed(range(n-1)):
        rightprods[i] = rightprods[i+1] * arr[i+1]

    # at each iteration, leftprodval := product(arr[j]) s.t. j < i
    # answer is leftprodval * rightprods[i] = product(arr[j]) s.t. i != j
    leftprodval = 1
    for i in range(n):
        rightprods[i] *= leftprodval
        leftprodval *= arr[i]
    return rightprods


class TestProductAllOthers(unittest.TestCase):
    def test_get_all_products(self):
        tests = [
            [[1, 7, 3, 4], [7*3*4, 1*3*4, 1*7*4, 1*7*3]],
            [[2, 9, 5, 7, 8], [9*5*7*8, 2*5*7*8, 2*9*7*8, 2*9*5*8, 2*9*5*7]],
            [[2, 0, 7, 8], [0, 2*7*8, 0, 0]]
        ]
        for test, expected in tests:
            self.assertEqual(get_all_products(test), expected)


if __name__ == "__main__":
    unittest.main()
