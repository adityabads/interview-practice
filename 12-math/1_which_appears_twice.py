# Which appears twice
# I have an array of n+1 numbers. Every number in the range 1..n appears once
# except for one number that appears twice. Write a function for finding the
# number that appears twice.
#
# NOTE: Also see `find_repeat_space` (problem 4.2) for a space-optimized solution,
# and `find_repeat_challenge` (problem 5.6) for an optimal solution where multiple
# duplicates are allowed

from typing import List
import unittest


def find_repeat(arr: List[int]) -> int:
    """Returns the repeat number in array described above"""
    n = len(arr)-1
    expected = n*(n+1)/2
    total = sum(arr)
    return total - expected


class TestWhichAppearsTwice(unittest.TestCase):
    def test_which_appears_twice(self):
        tests = [
            [[1, 4, 2, 3, 5, 2], 2],
            [[2, 1, 1], 1],
            [[3, 4, 2, 1, 4], 4]
        ]
        for arr, expected in tests:
            self.assertEqual(find_repeat(arr), expected)


if __name__ == "__main__":
    unittest.main()
