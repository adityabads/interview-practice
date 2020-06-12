# Temp tracker
# Write a class TempTracker with these methods:
#
# insert() — records a new temperature
# get_max() — returns the highest temp we've seen so far
# get_min() — returns the lowest temp we've seen so far
# get_mean() — returns the mean of all temps we've seen so far
# get_mode() — returns a mode of all temps we've seen so far
#
# Optimize for space and time. Favor speeding up the getter methods get_max(),
# get_min(), get_mean(), and get_mode() over speeding up the insert() method.
#
# get_mean() should return a float, but the rest of the getter methods can
# return integers. Temperatures will all be inserted as integers. We'll record
# our temperatures in Fahrenheit, so we can assume they'll all be in the range
# 0..110.
#
# If there is more than one mode, return any of the modes.
#
# BONUS
# There's at least one way to use a just-in-time approach, have O(1) time for
# each operation, and keep our space cost at O(1)O(1) for nn inserts. How
# could we do that?

from collections import Counter
import random
import unittest


class TempTracker:

    def __init__(self, maxtemp=110):
        # for min/max
        self.min = None
        self.max = None

        # for mean
        self.mean = None
        self.total = 0
        self.totalcount = 0

        # for mode
        self.mode = None
        self.modecount = 0
        self.tempcounts = [0] * (maxtemp+1)

    def insert(self, temp: int) -> None:
        if temp < 0 or temp > 110:
            raise Exception("temp must be between 0 and 110 inclusive")

        # for min/max
        if not self.min or temp < self.min:
            self.min = temp
        if not self.max or temp > self.max:
            self.max = temp

        # for mean
        self.total += temp
        self.totalcount += 1
        self.mean = self.total / self.totalcount

        # for mode
        self.tempcounts[temp] += 1
        if self.tempcounts[temp] > self.modecount:
            self.modecount = self.tempcounts[temp]
            self.mode = temp

    def get_min(self) -> int:
        return self.min

    def get_max(self) -> int:
        return self.max

    def get_mean(self) -> float:
        return self.mean

    def get_mode(self) -> int:
        return self.mode


class TestTempTracker(unittest.TestCase):
    def test_get_max(self):
        temptracker = TempTracker()
        nums = [random.randint(0, 110) for _ in range(20)]
        for i in range(len(nums)):
            temptracker.insert(nums[i])
            self.assertEqual(temptracker.get_max(), max(nums[:i+1]))

    def test_get_min(self):
        temptracker = TempTracker()
        nums = [random.randint(0, 110) for _ in range(20)]
        for i in range(len(nums)):
            temptracker.insert(nums[i])
            self.assertEqual(temptracker.get_min(), min(nums[:i+1]))

    def test_get_mean(self) -> float:
        temptracker = TempTracker()
        nums = [random.randint(0, 110) for _ in range(20)]
        for i in range(len(nums)):
            temptracker.insert(nums[i])
            self.assertEqual(temptracker.get_mean(), sum(nums[:i+1])/(i+1))

    def test_get_mode(self) -> float:
        temptracker = TempTracker()
        nums = [random.randint(0, 110) for _ in range(20)]
        for i in range(len(nums)):
            temptracker.insert(nums[i])
            counts = Counter(nums[:i+1])
            maxcount = max(counts.values())
            modes = [val for val, count in counts.items() if count == maxcount]
            self.assertIn(temptracker.get_mode(), modes)


if __name__ == "__main__":
    unittest.main()
