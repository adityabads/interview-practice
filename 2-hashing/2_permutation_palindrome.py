# Permutation palindrome
# Write an efficient function that checks whether any permutation of an input
# string is a palindrome.
#
# Assume the input string only contains lowercase letters.

import unittest


def is_palindrome_permutation(s: str) -> bool:
    seen = set()
    for c in s:
        if c in seen:
            seen.remove(c)
        else:
            seen.add(c)
    return len(seen) <= 1


class TestPermutationPalindrome(unittest.TestCase):
    def test_is_palindrome_permutation(self):
        trues = ["civic", "ivicc"]
        falses = ["civil", "livci"]
        for test in trues:
            with self.subTest(test=test):
                self.assertTrue(is_palindrome_permutation(test))
        for test in falses:
            with self.subTest(test=test):
                self.assertFalse(is_palindrome_permutation(test))


if __name__ == "__main__":
    unittest.main()
