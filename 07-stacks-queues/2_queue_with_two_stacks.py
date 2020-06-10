# Queue with two stacks
# Implement a queue with 2 stacks. Your queue should have an enqueue and a
# dequeue method and it should be "first in first out" (FIFO).
#
# Optimize for the time cost of m calls on your queue. These can be any mix
# of enqueue and dequeue calls.
#
# Assume you already have a stack implementation and it gives O(1) time
# push and pop.

from mystack import Stack
import unittest


class Queue:
    def __init__(self):
        self.addstack = Stack()
        self.removestack = Stack()

    def enqueue(self, val) -> None:
        """Enqueues val onto queue"""
        self.addstack.push(val)

    def dequeue(self):
        """Dequeues val, returns None if queue empty"""
        if self.removestack.isempty():
            while not self.addstack.isempty():
                self.removestack.push(self.addstack.pop())
        return self.removestack.pop()


class TestQueueWithTwoStacks(unittest.TestCase):
    def test_queue_with_two_stacks(self):
        enqueues1 = [5, 3, 7, 4, 9]
        dequeues1 = [5, 3]
        enqueues2 = [2, 4, 3, 9]
        dequeues2 = [7, 4, 9, 2, 4, 3, 9]
        q = Queue()
        for val in enqueues1:
            q.enqueue(val)
        for val in dequeues1:
            self.assertEqual(q.dequeue(), val)
        for val in enqueues2:
            q.enqueue(val)
        for val in dequeues2:
            self.assertEqual(q.dequeue(), val)


if __name__ == "__main__":
    unittest.main()
