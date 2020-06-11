# Find repeat, challenge mode
# We have a list with n+1 integers in the range 1..n. Thus, the list must have
# at least 1 duplicate. The previous challenge was to find a duplicate number,
# while optimizing for space. We used a divide and conquer approach, iteratively
# cutting the list in half to find a duplicate integer in O(n lg n) time and
# O(1) space (sort of a modified binary search).
#
# But we can actually do better. We can find a duplicate integer in O(n) time
# while keeping our space cost at O(1).
#
# This is a tricky one to derive (unless you have a strong background in graph
# theory), so we'll get you started:
#
# Imagine each item in the list as a node in a linked list. In any linked list,
# each node has a value and a "next" pointer. In this case:
# The value is the integer from the list.
# The "next" pointer points to the value-th node in the list (numbered starting
# from 1). For example, if our value was 3, the "next" node would be the third node.
#
# EXAMPLE
# A list [2, 3, 1, 3], so 2 is in the first position and points to 3 in the
# second position. Notice we're using "positions" and not "indices." For this
# problem, position = index + 1.
#
# Using this, find a duplicate integer in O(n) time while keeping our space
# cost at O(1).
#
# BONUS
# There another approach using randomized algorithms that is O(n) time and
# O(1) space. Can you come up with that one? (Hint: You'll want to focus on the median.)

from typing import List
import unittest


def find_repeat(arr: List[int], maxval: int) -> int:
    """Find repeated integer"""
    # modification of Floyd's cycle detection
    def _next(x: int) -> int:
        nonlocal arr
        return arr[x-1]

    # last will never have any pointers
    slow = len(arr)
    fast = len(arr)
    while True:
        slow = _next(slow)
        fast = _next(_next(fast))
        if slow == fast:
            break

    # find beginning of cycle
    slow = len(arr)
    while slow != fast:
        slow = _next(slow)
        fast = _next(fast)
    return slow


class TestFindRepeatChallenge(unittest.TestCase):
    def test_find_repeat(self):
        tests = [
            [[3, 4, 2, 3, 1, 5], 5, [3]],
            [[3, 1, 2, 2], 3, [2]],
            [[2, 3, 1, 3], 3, [3]],
            [[4, 3, 1, 1, 4], 4, [1, 4]],
            [[1, 4, 2, 5, 7, 8, 6, 3, 9, 7], 9, [7]],
            [[2, 1, 2], 2, [2]],
            [[6, 4, 3, 5, 5, 3, 1], 6, [3, 5]]
        ]
        for arr, maxval, expectedvals in tests:
            with self.subTest(arr):
                self.assertIn(find_repeat(arr, maxval), expectedvals)


if __name__ == "__main__":
    unittest.main()
