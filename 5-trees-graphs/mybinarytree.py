class BinaryTreeNode(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert_left(self, val):
        self.left = BinaryTreeNode(val)
        return self.left

    def insert_right(self, val):
        self.right = BinaryTreeNode(val)
        return self.right
