# Does this linked list have a cycle?
# Write a function contains_cycle() that takes the first node in a singly-linked
# list and returns a boolean indicating whether the list contains a cycle.
#
# 1. How would you detect the first node in the cycle? Define the first node
# of the cycle as the one closest to the head of the list.
#
# 2. Would the program always work if the fast runner moves three steps every
# time the slow runner moves one step?
#
# 3. What if instead of a simple linked list, you had a structure where each
# node could have several "next" nodes? This data structure is called a
# "directed graph." How would you test if your directed graph had a cycle?

from mylinkedlist import LinkedList, LinkedListNode
import unittest


def contains_cycle(head: LinkedListNode) -> bool:
    """Returns true iff linked list contains a cycle"""
    if not head or not head.next:
        return False
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


class TestContainsCycle(unittest.TestCase):
    def test_contains_cycle(self):
        ll = LinkedList([1, 2, 3, 4, 5, 1, 2])
        self.assertFalse(contains_cycle(ll.head))
        self.assertFalse(contains_cycle(ll.head.next))
        self.assertFalse(contains_cycle(ll.head.next.next.next))
        ll.append_node(ll.head.next.next)
        self.assertTrue(contains_cycle(ll.head))
        self.assertTrue(contains_cycle(ll.head.next))
        self.assertTrue(contains_cycle(ll.head.next.next))
        self.assertTrue(contains_cycle(ll.head.next.next.next))


if __name__ == "__main__":
    unittest.main()
