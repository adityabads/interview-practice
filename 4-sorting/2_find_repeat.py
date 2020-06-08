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

from typing import List
import unittest


def find_repeat(arr: List[int], maxval: int) -> int:
    """Returns a repeated element in `arr`"""
    i = 0
    j = maxval
    while True:
        mid = (i+j)//2
        countfirsthalf = countsecondhalf = 0
        for val in arr:
            if val < mid:
                countfirsthalf += 1
            else:
                countsecondhalf += 1
        if countfirsthalf > mid - i:
            j = mid
        else:
            i = mid+1
        if i+1 == j:
            return i


class TestFindRepeat(unittest.TestCase):
    def test_find_repeat(self):
        tests = [
            [[1, 4, 7, 3, 9, 7], 9, [7]],
            [[2, -1, 0, -1, 2], 2, [-1, 2]]
        ]
        for arr, maxval, expectedvals in tests:
            self.assertIn(find_repeat(arr, maxval), expectedvals)


if __name__ == "__main__":
    unittest.main()
