# Balanced binary tree
# Write a function to see if a binary tree is "superbalanced" (a new tree
# property we just made up).
#
# A tree is "superbalanced" if the difference between the depths of any two
# leaf nodes is no greater than one.

from typing import Tuple
from mybinarytree import BinaryTreeNode, make_binary_tree
import unittest


def is_balanced(tree: BinaryTreeNode) -> bool:
    """Returns true iff all leaf nodes have depths within 1 of each other"""
    if tree is None:
        return True
    heights = []
    stack = [(tree, 0)]
    while stack:
        n, height = stack.pop()
        if (not n.left) and (not n.right) and height not in heights:
            heights.append(height)
            if len(heights) > 2 or (len(heights) == 2 and abs(heights[0] - heights[1]) > 1):
                return False
        else:
            if n.left:
                stack.append((n.left, height+1))
            if n.right:
                stack.append((n.right, height+1))
    return True


class TestBalancedBinaryTree(unittest.TestCase):
    def test_is_balanced(self):
        trues = [
            [],
            [1],
            [1, 2],
            [1, 2, 3],
            [1, 2, 3, 4],
            [1, 2, None, 4],
            [1, 2, 3, 4, None, 5, None],
            [1, 2, 3, 4, None, 5, None, 6],
        ]
        falses = [
            [1, 2, 3, None, 4, None, None, None, None, 5],
        ]
        for arr in trues:
            tree = make_binary_tree(arr)
            self.assertTrue(is_balanced(tree))
        for arr in falses:
            tree = make_binary_tree(arr)
            self.assertFalse(is_balanced(tree))


if __name__ == "__main__":
    unittest.main()
