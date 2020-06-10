# Balanced binary tree
# Write a function to see if a binary tree is "superbalanced" (a new tree
# property we just made up).
#
# A tree is "superbalanced" if the difference between the depths of any two
# leaf nodes is no greater than one.

from typing import Tuple
from mybinarytree import BinaryTreeNode
import unittest


def is_balanced(tree: BinaryTreeNode) -> bool:
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
        tree = BinaryTreeNode(1)
        tree.insert_left(1)
        tree.insert_right(1)
        self.assertTrue(is_balanced(tree))
        tree.left.insert_right(1)
        self.assertTrue(is_balanced(tree))
        tree.right.insert_left(1)
        self.assertTrue(is_balanced(tree))
        tree.right.left.insert_right(1)
        self.assertTrue(is_balanced(tree))
        tree.right.left.right.insert_right(1)
        self.assertFalse(is_balanced(tree))


if __name__ == "__main__":
    unittest.main()
