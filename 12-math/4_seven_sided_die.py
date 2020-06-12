# Simulate 7-sided die
# You have a function rand5() that generates a random integer from 1 to 5. Use
# it to write a function rand7() that generates a random integer from 1 to 7.
# rand5() returns each integer with equal probability. rand7() must also return
# each integer with equal probability.

import random
import unittest


def rand5() -> int:
    return random.randint(1, 5)


def rand7() -> int:
    outcome = float("inf")
    # make outcome uniform between 1 and 21, inclusive
    while outcome > 21:
        i = rand5()
        j = rand5()
        outcome = (i-1)*5 + (j-1) + 1
    # return uniform between 1 and 7, inclusive
    return outcome % 7 + 1


class TestSevenSidedDie(unittest.TestCase):
    def test_seven_sided_die(self):
        for i in range(21):
            print(rand7(), end=" ")
        print()


if __name__ == "__main__":
    unittest.main()
