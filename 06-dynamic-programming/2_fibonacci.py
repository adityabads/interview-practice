# Nth Fibonacci
# Write a function fib() that takes an integer nn and returns the nth Fibonacci
# number. Let's say our Fibonacci series is 0-indexed and starts with 0. So:
#
# fib(0)  # => 0
# fib(1)  # => 1
# fib(2)  # => 1
# fib(3)  # => 2
# fib(4)  # => 3
#
# BONUS
# If you're good with matrix multiplication you can bring the time cost down
# even further, to O(lg n). Can you figure out how?

from typing import Dict
import unittest


def fibonacci_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("n must be positive")
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_memo(n: int, memo: Dict[int, int] = None) -> int:
    if n < 0:
        raise ValueError("n must be positive")
    if n == 0 or n == 1:
        return n
    if not memo:
        memo = {}
    if n not in memo:
        memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]


def fibonacci_dp(n: int) -> int:
    if n < 0:
        raise ValueError("n must be positive")
    if n == 0 or n == 1:
        return n
    nums = [None, 0, 1]
    for _ in range(n-1):
        nums[0] = nums[1]
        nums[1] = nums[2]
        nums[2] = nums[0] + nums[1]
    return nums[2]


class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        tests = [
            [0, 0], [1, 1], [2, 1], [3, 2], [4, 3], [5, 5], [6, 8], [7, 13]
        ]
        for n, expected in tests:
            self.assertEqual(fibonacci_recursive(n), expected)
            self.assertEqual(fibonacci_memo(n), expected)
            self.assertEqual(fibonacci_dp(n), expected)


if __name__ == "__main__":
    unittest.main()
