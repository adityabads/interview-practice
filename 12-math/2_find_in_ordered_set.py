# Suppose we had a list of n integers sorted in ascending order. How quickly
# could we check if a given integer is in the list?

from typing import List
import unittest


def binary_search(arr: List[int], k: int) -> bool:
    """Returns true iff k is in sorted list arr"""
    l = 0
    r = len(arr)-1
    while l <= r:
        mid = (l+r)//2
        if arr[mid] == k:
            return True
        elif k < arr[mid]:
            r = mid-1
        else:
            l = mid+1
    return False


class TestFindInOrderedSet(unittest.TestCase):
    def test_binary_search(self):
        arrs = [
            [],
            [1],
            [1, 2],
            [1, 4, 5],
            [1, 2, 4, 5, 7, 9],
            [1, 2, 4, 5, 7, 9, 11]
        ]
        for arr in arrs:
            for i in range(12):
                with self.subTest(arr=arr, i=i):
                    if i in arr:
                        self.assertTrue(binary_search(arr, i))
                    else:
                        self.assertFalse(binary_search(arr, i))


if __name__ == "__main__":
    unittest.main()
