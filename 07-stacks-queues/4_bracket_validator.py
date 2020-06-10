# Bracket validator
# Write a braces/brackets/parentheses validator. Let's say:
# '(', '{', '[' are called "openers."
# ')', '}', ']' are called "closers."
# Write an efficient function that tells us whether or not an input string's
# openers and closers are properly nested.
#
# EXAMPLES:
# "{[]()}"  -> True
# "{[(])}"  -> False
# "{[}"     -> False
#
# Bonus
# In Ruby, sometimes expressions are surrounded by vertical bars, "|like this|".
# Extend your validator to validate vertical bars. Careful: there's no difference
# between the "opener" and "closer" in this case—they're the same character!

import unittest


def is_nested(s: str) -> bool:
    openers = ["(", "{", "["]
    closers = [")", "}", "]"]
    closers_to_openers = dict(zip(closers, openers))
    brackets = []
    for c in s:
        if c in openers:
            brackets.append(c)
        elif c in closers_to_openers and (
                not brackets or closers_to_openers[c] != brackets.pop()):
            return False
    return len(brackets) == 0


class TestBracketValidator(unittest.TestCase):
    def test_is_nested(self):
        trues = [
            "{[]()}",
            "hello(there)I am {hehe{}} []"
        ]
        falses = [
            "{[(])}",
            "{[}",
            "(",
            "[])"
        ]
        for string in trues:
            with self.subTest(string=string):
                self.assertTrue(is_nested(string))
        for string in falses:
            with self.subTest(string=string):
                self.assertFalse(is_nested(string))


if __name__ == "__main__":
    unittest.main()
