class Node:
    val = left = right = None

    def __init__(self, val, parent=None):
        self.val = val
        self.parent: Node = parent

    def add(self, item):
        if item <= self.val:
            if self.left is None:
                self.left = Node(item, self)
            else:
                self.left.add(item)
        else:
            if self.right is None:
                self.right = Node(item, self)
            else:
                self.right.add(item)