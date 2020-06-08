# Top scores
# Each round, players receive a score between 0 and 100, which you use to rank
# them from highest to lowest. So far you're using an algorithm that sorts in
# O(n lg n) time, but players are complaining that their rankings aren't
# updated fast enough. You need a faster sorting algorithm.
#
# Write a function that takes a list of unsorted_scores and the
# highest_possible_score in the game and returns a sorted list of scores in
# less than O(n lg n) time.
#
# EXAMPLE
# Input:  [37, 89, 41, 65, 91, 53], 100
# Output: [91, 89, 65, 53, 41, 37]
#
# We're defining n as the number of unsorted_scores because we're expecting
# the number of players to keep climbing. We'll treat highest_possible_score
# as a constant instead of factoring it into our big O time and space costs
# because the highest possible score isn't going to change. Even if we do
# redesign the game a little, the scores will stay around the same order of
# magnitude.
#
# BONUS
# 1. Note that by optimizing for time we ended up incurring some space cost!
# What if we were optimizing for space?
#
# 2. We chose to generate and return a separate, sorted list. Could we instead
# sort the list in place? Does this change the time complexity? The space
# complexity?

from typing import List
import unittest


def bucket_sort_desc(arr: List[int], max: int) -> None:
    buckets = [0] * (max + 1)
    for val in arr:
        buckets[val] += 1
    arri = 0
    for i in reversed(range(len(buckets))):
        count = buckets[i]
        for _ in range(count):
            arr[arri] = i
            arri += 1


class TestTopScores(unittest.TestCase):
    def test_bucket_sort(self):
        tests = [
            [[37, 89, 41, 65, 91, 53], 100, [91, 89, 65, 53, 41, 37]],
            [[8, 9, 5, 10, 7, 9], 10, [10, 9, 9, 8, 7, 5]]
        ]
        for unsorted_scores, highest_possible_score, expected in tests:
            bucket_sort_desc(unsorted_scores, highest_possible_score)
            self.assertEqual(unsorted_scores, expected)


if __name__ == "__main__":
    unittest.main()
