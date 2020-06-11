# kth to last node
# Write a function kth_to_last_node() that takes an integer k and the head_node
# of a singly-linked list, and returns the kth to last node in the list.

from mylinkedlist import LinkedList, LinkedListNode
import unittest


def kth_to_last_node(head: LinkedListNode, k: int) -> LinkedListNode:
    """Returns kth to last node in linked list if it exists, else None"""
    if k <= 0:
        return None
    slow = head
    fast = head
    for _ in range(k):
        if not fast:
            return None
        fast = fast.next
    while fast is not None:
        slow = slow.next
        fast = fast.next
    return slow


class TestKthToLastNode(unittest.TestCase):
    def test_kth_to_last_node(self):
        tests = [
            [[1, 2, 3, 4, 5], 1, 5],
            [[1, 2, 3, 4, 5], 2, 4],
            [[1, 2, 3, 4, 5], 3, 3],
            [[1, 2, 3, 4, 5], 5, 1],
            [[1, 2, 3, 4, 5], 6, None],
            [[1], 1, 1],
            [[1], 2, None],
            [[], 1, None]
        ]
        for arr, k, expected in tests:
            with self.subTest(arr=arr, k=k):
                ll = LinkedList(arr)
                val = kth_to_last_node(ll.head, k)
                if val:
                    val = val.val
                self.assertEqual(val, expected)


if __name__ == "__main__":
    unittest.main()
