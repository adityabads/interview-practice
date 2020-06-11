# kth to last node
# Write a function kth_to_last_node() that takes an integer k and the head_node
# of a singly-linked list, and returns the kth to last node in the list.
#
# BONUS
# Can we do better? What if we expect nn to be huge and k to be pretty small?
# In this case, our target node will be close to the end of the list...so it
# seems a waste that we have to walk all the way from the beginning twice.
# Can we trim down the number of steps in the "second trip"? One pointer will
# certainly have to travel all the way from head to tail in the list to get
# the total length...but can we store some "checkpoints" as we go so that the
# second pointer doesn't have to start all the way at the beginning? Can we
# store these "checkpoints" in constant space? Note: this approach only saves
# time if we know that our target node is towards the end of the list (in
# other words, n is much larger than k).

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
