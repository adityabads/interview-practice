# Largest stack
# Use your Stack class to implement a new class MaxStack with a method get_max()
# that returns the largest element in the stack. get_max() should not remove the
# item. Your stacks will contain only integers.
#
# BONUS
# Our solution requires O(m) additional space for the second stack. But do we
# really need it? Can you come up with a solution that requires O(1) additional
# space? (It's tricky!)

from mystack import Stack
import unittest


class MaxStack:

    def __init__(self):
        """Initialize an empty stack"""
        self.stack = Stack()
        self.maxvals = Stack()

    def push(self, item: int) -> None:
        """Push a new item onto the stack"""
        self.stack.push(item)
        if self.maxvals.isempty() or item >= self.maxvals.peek():
            self.maxvals.push(item)

    def pop(self) -> int:
        """Remove and return the last item"""
        if self.stack.isempty():
            return None
        val = self.stack.pop()
        if val == self.maxvals.peek():
            self.maxvals.pop()
        return val

    def peek(self) -> int:
        """Return the last item without removing it"""
        return self.stack.peek()

    def get_max(self) -> int:
        """Return the largest element in the stack"""
        return self.maxvals.peek()


class TestMaxStack(unittest.TestCase):
    def test_max_stack(self):
        pushes = [
            [0, 0],
            [1, 1],
            [0, 1],
            [4, 4],
            [3, 4],
            [4, 4],
            [-4, 4],
            [7, 7]
        ]
        pops = [
            [7, 4],
            [-4, 4],
            [4, 4],
            [3, 4],
            [4, 1],
            [0, 1],
            [1, 0]
        ]
        maxstack = MaxStack()
        for val, expected in pushes:
            maxstack.push(val)
            self.assertEqual(maxstack.peek(), val)
            self.assertEqual(maxstack.get_max(), expected)
        for val, expected in pops:
            self.assertEqual(maxstack.pop(), val)
            self.assertEqual(maxstack.get_max(), expected)


if __name__ == "__main__":
    unittest.main()
