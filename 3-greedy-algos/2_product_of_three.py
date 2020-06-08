# Product of three
# Given a list of integers, find the highest product you can get from three
# of the integers.
#
# The input list_of_ints will always have at least three integers.

from typing import List
import unittest


def product_of_three(arr: List[int]) -> int:
    if len(arr) == 3:
        return arr[0] * arr[1] * arr[2]
    bigs = []
    bignegs = []
    smallnegs = []
    for val in arr:
        if val > 0:
            bigs.append(val)
            bigs.sort(reverse=True)
            if len(bigs) > 3:
                bigs.pop()
        if val < 0:
            bignegs.append(val)
            bignegs.sort()
            if len(bignegs) > 2:
                bignegs.pop()
            smallnegs.append(val)
            smallnegs.sort(reverse=True)
            if len(smallnegs) > 3:
                smallnegs.pop()
    # must be at least 4 numbers
    if len(bigs) == 0:
        # 0 positive numbers
        return smallnegs[0] * smallnegs[1] * smallnegs[2]
    elif len(bignegs) <= 1:
        # 0 or 1 negative numbers
        return bigs[0] * bigs[1] * bigs[2]
    elif len(bigs) <= 2:
        # 1 or 2 positive numbers, >2 negative numbers
        return bigs[0] * bignegs[0] * bignegs[1]
    else:
        # >3 positive numbers, >2 negative numbers
        return max(bigs[0] * bigs[1] * bigs[2],
                   bigs[0] * bignegs[0] * bignegs[1])


class TestProductOfThree(unittest.TestCase):
    def test_product_of_three(self):
        tests = [
            [[1, 5, 2, 4, 3], 60],
            [[7, -1, 8, 9, 4, 10, 6], 720],
            [[-1, -90, -7, -20, -4, -5], -20],
            [[-2, -27, -3, -10, -9, 2], 540],
            [[-9, -4, 1, -11, 10, 2, -10], 1100],
            [[-10, -10, 1, 3, 2], 300],
            [[4, -2, 3, 1], 12],
        ]
        for arr, expected in tests:
            self.assertEqual(product_of_three(arr), expected)


if __name__ == "__main__":
    unittest.main()
