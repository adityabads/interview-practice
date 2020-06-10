from typing import List


class BinaryTreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert_left(self, val) -> None:
        self.left = BinaryTreeNode(val)
        return self.left

    def insert_right(self, val) -> None:
        self.right = BinaryTreeNode(val)
        return self.right


def make_binary_tree(vals: List[int]) -> BinaryTreeNode:
    return _make_binary_tree_util(vals, None, 0, len(vals))


def _make_binary_tree_util(vals: List[int], node: BinaryTreeNode, i: int, n: int) -> BinaryTreeNode:
    root = None
    if i < n and vals[i] is not None:
        root = BinaryTreeNode(vals[i])
        root.left = _make_binary_tree_util(vals, root.left, 2*i + 1, n)
        root.right = _make_binary_tree_util(vals, root.right, 2*i + 2, n)
    return root
