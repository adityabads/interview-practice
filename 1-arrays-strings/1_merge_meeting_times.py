# Merge meeting times
# Write a function merge_ranges() that takes a list of multiple meeting time
# ranges and returns a list of condensed ranges.
#
# Do not assume the meetings are in order.
#
# EXAMPLE
# Input:  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
# Output: [(0, 1), (3, 8), (9, 12)]
#
# BONUS
# 1. What if we did have an upper bound on the input values? Could we improve
# our runtime? Would it cost us memory?
#
# 2. Could we do this "in place" on the input list and save some space? What
# are the pros and cons of doing this in place?

from typing import List, Tuple
import unittest


def merge_intervals(times: List[Tuple[int]]) -> List[Tuple[int]]:
    """Merge list of closed intervals (i, j)"""
    times = sorted(times)
    merged = []
    for time in times:
        start, end = time
        if not merged or start > merged[-1][1]:
            merged.append(time)
        elif end > merged[-1][1]:
            merged[-1] = (merged[-1][0], end)
    return merged


class TestMergeMeetingTimes(unittest.TestCase):
    def test_merge_intervals(self):
        tests = [
            [[(1, 2), (2, 3)], [(1, 3)]],
            [[(1, 3), (2, 5)], [(1, 5)]],
            [[(1, 5), (2, 3)], [(1, 5)]],
            [[(1, 2), (3, 4)], [(1, 2), (3, 4)]],
            [[(1, 4), (4, 8)], [(1, 8)]],
            [[(1, 10), (2, 6), (3, 5), (7, 9)], [(1, 10)]],
            [[(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)], [(0, 1), (3, 8), (9, 12)]]
        ]
        for times, merged in tests:
            self.assertEqual(merge_intervals(times), merged)


if __name__ == "__main__":
    unittest.main()
