# Parenthesis matching
# Write a function that, given a sentence and the position of an opening
# parenthesis, finds the position of the corresponding closing parenthesis.

import unittest


def match_paren(s: str, ind: int) -> int:
    if s[ind] != "(":
        raise Exception("ind must correspond to opening parenthesis")
    parens = 1
    for i in range(ind+1, len(s)):
        if s[i] == "(":
            parens += 1
        elif s[i] == ")":
            parens -= 1
        if parens == 0:
            return i
    return None


class TestParenthesisMatching(unittest.TestCase):
    def test_match_paren(self):
        tests = [
            ["01(345((8)))", 2, 11],
            ["01(345((8)))", 6, 10],
            ["01(345((8)))", 7, 9],
            ["01(345((8))", 2, None],
            ["(12(4(6))9)1", 0, 10],
            ["(12(4(6))9)1", 3, 8],
            ["(12(4(6))9)1", 5, 7]
        ]
        for test, left, right in tests:
            self.assertEqual(match_paren(test, left), right)


if __name__ == "__main__":
    unittest.main()
