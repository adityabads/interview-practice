# Binary search tree checker
# Write a function to check that a binary tree is a valid binary search tree.
#
# BONUS
# 1. What if the input tree has duplicate values?
#
# 2. What if -float('inf') or float('inf') appear in the input tree?

from mybinarytree import BinaryTreeNode, make_binary_tree
import unittest


def is_valid_bst(tree: BinaryTreeNode, minval: float = float("-inf"), maxval: float = float("inf")):
    """Returns true iff binary tree is a valid search tree"""
    if tree is None:
        return True
    leftvalid = is_valid_bst(tree.left, minval, tree.val)
    rightvalid = is_valid_bst(tree.right, tree.val, maxval)
    return minval < tree.val and tree.val <= maxval and leftvalid and rightvalid


class TestBinarySearchTreeChecker(unittest.TestCase):
    def test_is_valid_bst(self):
        trues = [
            [],
            [5],
            [5, 1, 7],
            [5, 1, 7, -1, 2, 6],
            [5, 1, 7, 1, 2, 6],
            [5, 1, 7, -1, 2, None, 8]
        ]
        falses = [
            [1, 2, 3],
            [5, 1, 7, -1, 1, 6],
            [5, 1, 7, 0, 6],
            [5, 3, 8, 2, 6, 7, 9]
        ]
        for arr in trues:
            tree = make_binary_tree(arr)
            self.assertTrue(is_valid_bst(tree))
        for arr in falses:
            tree = make_binary_tree(arr)
            self.assertFalse(is_valid_bst(tree))


if __name__ == "__main__":
    unittest.main()
