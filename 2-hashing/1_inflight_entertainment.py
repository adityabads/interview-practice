# In-flight entertainment
# You're building a feature for choosing two movies whose total runtimes will
# equal the exact flight length.
#
# Write a function that takes an integer flight_length (in minutes) and a list
# of integers movie_lengths (in minutes) and returns a boolean indicating
# whether there are two numbers in movie_lengths whose sum equals flight_length.
#
# Assume your users will watch exactly two movies. Don't make your users watch
# the same movie twice. Optimize for runtime over memory

from typing import List
import unittest


def is_sum(arr: List[int], k: int) -> bool:
    times = set()
    for time in arr:
        if k - time in times:
            return True
        times.add(time)
    return False


class TestInFlightEntertainment(unittest.TestCase):
    def test_is_merge(self):
        trues = [
            [[9, 3, 7, 2, 1], 3],
            [[9, 3, 7, 2, 1], 10],
            [[9, 3, 7, 2, 1], 16]
        ]
        falses = [
            [[9, 3, 7, 2, 1], 6],
            [[9, 3, 7, 2, 1], 2],
            [[9, 3, 7, 2, 1], 15],
            [[9, 3, 7, 2, 1], 14],
        ]
        for movie_lengths, flight_length in trues:
            self.assertTrue(is_sum(movie_lengths, flight_length))
        for movie_lengths, flight_length in falses:
            self.assertFalse(is_sum(movie_lengths, flight_length))


if __name__ == "__main__":
    unittest.main()
