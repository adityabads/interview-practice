# In-place shuffle
# Write a function for doing an in-place shuffle of a list. The shuffle must be
# "uniform," meaning each item in the original list must have the same
# probability of ending up in each spot in the final list.
#
# Assume that you have a function get_random(floor, ceiling) for getting a
# random integer that is >= floor and <= ceiling.

from typing import List
import random
import unittest


def shuffle(arr: List[int]) -> None:
    """Shuffles list in-place"""
    n = len(arr)
    for i in range(n):
        shuffle = random.randint(i, n-1)
        if i != shuffle:
            arr[i], arr[shuffle] = arr[shuffle], arr[i]


class TestShuffle(unittest.TestCase):
    def test_shuffle(self):
        arr = [i for i in range(10)]
        for i in range(10):
            shuffle(arr)
            print(arr)
        arr = []
        shuffle(arr)
        print(arr)
        arr = [1]
        shuffle(arr)
        print(arr)


if __name__ == "__main__":
    unittest.main()
