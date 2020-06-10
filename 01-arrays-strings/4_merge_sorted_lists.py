# Merge sorted lists
# We have two lists of numbers sorted numerically already, in lists.
#
# Write a function to merge our lists of orders into one sorted list.
#
# EXAMPLE
# Input:  [3, 4, 6, 10, 11, 15], [1, 5, 8, 12, 14, 19]
# Output: [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
#
# BONUS
# 1. What if we wanted to merge several sorted lists? Write a function that
# takes as an input a list of sorted lists and outputs a single sorted list
# with all the items from each list.
#
# 2. Do we absolutely have to allocate a new list to use for the merged output?
# Where else could we store our merged list? How would our function need to change?

from typing import List
import unittest


def merge(a: List[int], b: List[int]) -> List[int]:
    """Returns sorted merge of two sorted lists"""
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


def merge_all(lists: List[List[int]]) -> List[int]:
    """Returns sorted merge of all sorted lists, in a list"""
    merged = []
    n = len(lists)
    indices = [0 for _ in range(n)]
    lengths = [len(list_) for list_ in lists]
    while any([indices[i] < lengths[i] for i in range(n)]):
        vals = [lists[i][indices[i]] if indices[i] < lengths[i]
                else float("inf") for i in range(n)]
        mini = vals.index(min(vals))
        merged.append(lists[mini][indices[mini]])
        indices[mini] += 1
    return merged


class TestMergeSortedLists(unittest.TestCase):
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

    def test_merge_all(self):
        tests = [
            [[], [], [], []],
            [[1], [], [], [3], []],
            [[-5, -1, 0, 3, 3, 9], [-2, 4, 7, 10]],
            [[-3, 1, 7], [2, 5, 7], [-2, 0, 8, 9], [-2, 2]]
        ]
        for test in tests:
            with self.subTest(test=test):
                print(merge_all(test))


if __name__ == "__main__":
    unittest.main()
