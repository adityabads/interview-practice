class Stack:

    def __init__(self) -> None:
        """Initialize an empty stack"""
        self.items = []

    def push(self, item) -> None:
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        if not self.items:
            return None
        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]
