# Reverse string
# Write a function that takes a list of characters and reverses the letters in place.

from typing import List
import unittest


def reverse_string(s: List[str]) -> None:
    """Reverses list of characters in place"""
    i = 0
    j = len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1


class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        tests = [
            [val for val in "abcdefghij"[:j]] for j in range(10)
        ]
        for test in tests:
            reversedstr = test.copy()
            reverse_string(reversedstr)
            self.assertEqual(reversedstr, list(reversed(test)))


if __name__ == "__main__":
    unittest.main()
