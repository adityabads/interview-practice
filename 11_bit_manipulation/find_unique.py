# Find unique
# Given the list of IDs, which contains many duplicate integers and one unique
# integer, find the unique integer.

from typing import List
import unittest


def find_unique(arr: List[int]) -> int:
    running = 0
    for val in arr:
        running ^= val
    return running


class TestFindUnique(unittest.TestCase):
    def test_find_unique(self):
        tests = [
            [[1, 9, 7, 9, 3, 1, 3], 7],
            [[-1, 4, 2, 9, 9, -1, 4], 2]
        ]
        for arr, expected in tests:
            self.assertEqual(find_unique(arr), expected)


if __name__ == "__main__":
    unittest.main()
