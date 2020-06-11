# Reverse linked list
# Write a function for reversing a linked list. Do it in place. Your function
# will have one input: the head of the list. Your function should return the
# new head of the list.
#
# This in-place reversal destroys the input linked list. What if we wanted to
# keep a copy of the original linked list? Write a function for reversing a
# linked list out-of-place.

from mylinkedlist import LinkedList, LinkedListNode
import unittest


def reverse_linked_list(head: LinkedListNode) -> LinkedListNode:
    """Reverses a linked list in-place, returns new head"""
    if not head:
        return None
    prev = None
    n = head
    next_ = None
    while n:
        next_ = n.next
        n.next = prev
        prev = n
        n = next_
    return prev


class TestReverseLinkedList(unittest.TestCase):
    def test_reverse_linked_list(self):
        arrs = [
            [],
            [1],
            [1, 2],
            [1, 2, 3],
            [1, 2, 3, 4],
            [1, 2, 3, 4, 5]
        ]
        for arr in arrs:
            ll = LinkedList(arr)
            head = reverse_linked_list(ll.head)
            while head:
                print(head.val, end=" ")
                head = head.next
            print()


if __name__ == "__main__":
    unittest.main()
