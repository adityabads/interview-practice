# Cafe order checker
# Write a function to check that my service is first-come, first-served. All
# food should come out in the same order customers requested it. We'll represent
# each customer order as a unique integer.

# EXAMPLE
# Take-out orders: [1, 3, 5]
# Dine-in orders:  [2, 4, 6]
# Served orders:   [1, 2, 4, 6, 5, 3]
# Output:          False (3 was requested before 5, but 5 was served first)

# EXAMPLE
# Take-out orders: [17, 8, 24]
# Dine-in orders:  [12, 19, 2]
# Served orders:   [17, 8, 12, 19, 24, 2]
# Output:          True

from typing import List
import unittest


def is_valid_merge(a: List[int], b: List[int], merged: List[int]) -> bool:
    """Returns true iff `merged` is a valid merge of `a` and `b`"""
    i = j = 0
    alen = len(a)
    blen = len(b)
    for mergedval in merged:
        if i < alen and mergedval == a[i]:
            i += 1
        elif j < blen and mergedval == b[j]:
            j += 1
        else:
            return False
    return True


class TestCafeOrderChecker(unittest.TestCase):
    def test_is_valid_merge(self):
        trues = [
            [[], [], []],
            [[1], [], [1]],
            [[1], [3], [1, 3]],
            [[1], [3], [3, 1]],
            [[1, 2], [5], [1, 5, 2]],
            [[17, 8, 24], [12, 19, 2], [17, 8, 12, 19, 24, 2]]
        ]
        falses = [
            [[1, 3, 5], [2, 4, 6], [1, 2, 4, 6, 5, 3]]
        ]
        for a, b, merged in trues:
            self.assertTrue(is_valid_merge(a, b, merged))
        for a, b, merged in falses:
            self.assertFalse(is_valid_merge(a, b, merged))


if __name__ == "__main__":
    unittest.main()
