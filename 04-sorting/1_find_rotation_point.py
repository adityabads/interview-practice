# Find rotation point
# I have an alphabetically ordered list that has been "rotated." For example:
# words = [
#     'ptolemaic',
#     'retrograde',
#     'supplant',
#     'undulate',
#     'xenoepist',
#     'asymptote',      <-- rotates here!
#     'babka',
#     'banoffee',
#     'engender',
#     'karpatka',
#     'othellolagkage',
# ]

# Write a function for finding the index of the "rotation point."

from typing import List
import unittest


def find_rotation_point(arr: List[int]) -> int:
    if len(arr) < 2:
        return None
    first = arr[0]
    i = 0
    j = len(arr) - 1
    while i < j:
        mid = (i+j)//2
        if arr[mid] >= first:
            i = mid
        else:
            j = mid
        if j == i+1:
            return j


class TestFindRotationPoint(unittest.TestCase):
    def test_find_rotation_point(self):
        tests = [
            [[3, 4, 7, 8, -5, -4, 1, 2], 4],
            [[3, 4, 7, 8, -5, -4, 2], 4],
            [[8, 1, 2, 4, 5, 6, 7], 1],
            [[8, 1, 2, 4, 5, 7], 1],
            [[2, 5, 6, 8, 9, 1], 5],
            [[2, 1], 1],
            [[2, 0, 1], 1],
        ]
        for arr, ind in tests:
            self.assertEqual(find_rotation_point(arr), ind)


if __name__ == "__main__":
    unittest.main()
