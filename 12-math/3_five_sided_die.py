# Simulate 5-sided die
# You have a function rand7() that generates a random integer from 1 to 7. Use
# it to write a function rand5() that generates a random integer from 1 to 5.
# rand7() returns each integer with equal probability. rand5() must also return
# each integer with equal probability.
#
# BONUS
# This kind of math is generally outside the scope of a coding interview, but:
# if you know a bit of number theory you can prove that there exists no
# solution which is guaranteed to terminate. Hint: it follows from the
# fundamental theorem of arithmetic.

import random
import unittest


def rand7() -> int:
    """Returns random int between 1 and 7"""
    return random.randint(1, 7)


def rand5() -> int:
    """Returns random int between 1 and 5"""
    num = float("inf")
    while num > 5:
        num = rand7()
    return num


class TestFiveSidedDie(unittest.TestCase):
    def test_rand5(self):
        for i in range(20):
            print(rand5(), end=" ")
        print()


if __name__ == "__main__":
    unittest.main()
