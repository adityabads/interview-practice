class LinkedListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self, arr):
        self.head = None
        self.tail = None
        for val in arr:
            self.append(val)

    def __iter__(self):
        n = self.head
        while n:
            yield n
            n = n.next

    def __str__(self):
        return " ".join(str(n.val) for n in self)

    def append(self, val) -> None:
        self.append_node(LinkedListNode(val))

    def append_node(self, node: LinkedListNode) -> None:
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
