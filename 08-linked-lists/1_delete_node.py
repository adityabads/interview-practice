from mylinkedlist import LinkedList, LinkedListNode
import unittest


def delete_node(node: LinkedListNode) -> None:
    """Delete node from linked list, not at head or tail of list"""
    if node.next:
        node.val = node.next.val
        node.next = node.next.next
    else:
        raise Exception("Cannot delete node with this function")


class TestDeleteNode(unittest.TestCase):
    def test_delete_node(self):
        ll = LinkedList([1, 2, 3, 4, 5])
        print(ll)
        delete_node(ll.head.next.next)
        print(ll)


if __name__ == "__main__":
    unittest.main()
