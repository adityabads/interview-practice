# Recursive string permutations
# Write a recursive function for generating all permutations of an input string.
# Return them as a set.
#
# Don't worry about time or space complexity—if we wanted efficiency we'd write
# an iterative version.
#
# To start, assume every character in the input string is unique.
#
# Your function can have loops—it just needs to also be recursive.
#
# How does the problem change if the string can have duplicate characters?
#
# What if we wanted to bring down the time and/or space costs?

from typing import Set
import unittest

# f(s) :=   s                                       , len(s) <= 1
#           for perm in f(s[:len(s)-1]):
#               for i in range(len(s))]:
#                   perm[:i] + s[-1] + perm[i:]     , otherwise


def get_permutations(s: str) -> Set[str]:
    if len(s) <= 1:
        return set([s])
    prevperms = get_permutations(s[:-1])
    perms = set()
    for prevperm in prevperms:
        for i in range(len(s)):
            perms.add(prevperm[:i] + s[-1] + prevperm[i:])
    return perms


class TestStringPermutations(unittest.TestCase):
    def test_get_permutations(self):
        tests = ["a", "ab", "abc", "abcd"]
        for test in tests:
            print(get_permutations(test))


if __name__ == "__main__":
    unittest.main()
