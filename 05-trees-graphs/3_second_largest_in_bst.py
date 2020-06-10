# Second largest item in a binary search tree
# Write a function to find the 2nd largest element in a binary search tree.

from mybinarytree import BinaryTreeNode, make_binary_tree
from typing import Tuple
import unittest


def find_second_largest(tree: BinaryTreeNode) -> int:
    if not tree or ((not tree.left) and (not tree.right)):
        return None
    largest, prev = find_largest_and_parent(tree)
    if largest.left:
        secondlargest, _ = find_largest_and_parent(largest.left)
        return secondlargest.val
    else:
        return prev.val


def find_largest_and_parent(tree: BinaryTreeNode) -> Tuple[BinaryTreeNode, BinaryTreeNode]:
    """Returns largest node in BST and its parent"""
    parent = None
    while tree.right:
        parent = tree
        tree = tree.right
    return tree, parent


class TestSecondLargestInBST(unittest.TestCase):
    def test_find_second_largest(self):
        tests = [
            [[], None],
            [[5], None],
            [[5, 2], 2],
            [[5, 1, 7], 5],
            [[5, 1, 7, -1, 2, 6], 6],
            [[5, 1, 7, 1, 2, 6], 6],
            [[5, 1, 7, -1, 2, None, 8], 7]
        ]
        for arr, expected in tests:
            tree = make_binary_tree(arr)
            self.assertEqual(find_second_largest(tree), expected)


if __name__ == "__main__":
    unittest.main()
