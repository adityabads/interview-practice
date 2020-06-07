# Merge sorted lists
# We have two lists of numbers sorted numerically already, in lists. Write a
# function to merge our lists of orders into one sorted list.
#
# EXAMPLE
# Input:  [3, 4, 6, 10, 11, 15], [1, 5, 8, 12, 14, 19]
# Output: [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]

from typing import List
import unittest


def merge(a: List[int], b: List[int]) -> List[int]:
    merged = []
    i = j = 0
    alen = len(a)
    blen = len(b)
    while i < alen or j < blen:
        aval = a[i] if i < alen else float("inf")
        bval = b[j] if j < blen else float("inf")
        if aval <= bval:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    return merged


class TestMerge(unittest.TestCase):
    def test_merge(self):
        tests = [
            [[], []],
            [[1], []],
            [[3], [2]],
            [[3, 4, 6, 10, 11, 15], [1, 5, 8, 12, 14, 19]],
            [[1, 4, 4, 7, 9, 10], [-5, 2, 4, 7, 11]]
        ]
        for a, b in tests:
            with self.subTest(a=a, b=b):
                merged = merge(a, b)
                a.extend(b)
                expected = sorted(a)
                self.assertEqual(merged, expected)


if __name__ == "__main__":
    unittest.main()
