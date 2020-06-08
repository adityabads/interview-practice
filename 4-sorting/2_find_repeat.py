# Find repeat
# We have a list of integers, where the integers are in the range 1...n and the
# list has a length of n+1. It follows that our list has at least one integer
# which appears at least twice. But it may have several duplicates, and each
# duplicate may appear more than twice.
#
# Write a function which finds an integer that appears more than once in our list.
# (If there are multiple duplicates, you only need to find one of them.)
#
# Optimize for space.
#
# BONUS
# This function always returns one duplicate, but there may be several duplicates.
# Write a function that returns all duplicates.

from typing import List
import unittest


def find_repeat(arr: List[int], maxval: int) -> int:
    """Returns a repeated element in `arr`"""
    i = 1
    j = maxval
    while i < j:
        mid = (i+j)//2
        countfirsthalf = 0
        for val in arr:
            if i <= val and val <= mid:
                countfirsthalf += 1
        if countfirsthalf > mid - i + 1:
            j = mid
        else:
            i = mid+1
    return i


class TestFindRepeat(unittest.TestCase):
    def test_find_repeat(self):
        tests = [
            [[1, 4, 2, 5, 7, 8, 6, 3, 9, 7], 9, [7]],
            [[2, 1, 2], 2, [2]],
            [[6, 4, 3, 5, 5, 3, 1], 6, [3, 5]]
        ]
        for arr, maxval, expectedvals in tests:
            self.assertIn(find_repeat(arr, maxval), expectedvals)


if __name__ == "__main__":
    unittest.main()
