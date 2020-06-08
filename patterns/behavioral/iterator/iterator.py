from patterns.behavioral.iterator.utils.util_tree import Node


class Iterator:
    def has_next(self):
        raise NotImplementedError

    def get_next(self):
        raise NotImplementedError


# ------------------- Concrete Iterators ---------------------

class ListIterator(Iterator):
    def __init__(self, l):
        self._list = l
        self._i = 0

    def has_next(self):
        return self._i < len(self._list)

    def get_next(self):
        self._i += 1
        return self._list[self._i - 1]


class TreeIterator(Iterator):
    def __init__(self, root: Node):
        self._node = self._find_smallest(root)
        self._smallest = self._node

    def _find_smallest(self, node:Node):
        if node.left is not None:
            return self._find_smallest(node.left)
        return node

    def _find_next(self, node):
        if node.right is not None:
            return self._find_smallest(node.right)
        parent = node.parent
        while parent is not None:
            if node != parent.right:
                break
            node = parent
            parent = parent.parent
        return parent

    def has_next(self):
        return self._find_next(self._node) is not None

    def get_next(self):
        if self._smallest is not None:
            self._node = self._smallest
            self._smallest = None
        else:
            self._node = self._find_next(self._node)
        return self._node.val


class AbsurdIterator(Iterator):
    def __init__(self, iterable):
        self._iterable = iterable
        self._i = -1

    def has_next(self):
        return self._i < 5

    def get_next(self):
        self._i += 1
        if self._i is 0:
            return self._iterable.one
        elif self._i is 1:
            return self._iterable.two
        elif self._i is 2:
            return self._iterable.three
        elif self._i is 3:
            return self._iterable.four
        elif self._i is 4:
            return self._iterable.five
        elif self._i is 5:
            return self._iterable.six
        return None


class EndlessIterator(Iterator):
    def __init__(self, iterable):
        self._iterable = iterable
        self._i = -1

    def has_next(self):
        return True

    def get_next(self):
        self._i += 1
        if self._i >= len(self._iterable.list):
            self._i = 0
        return self._iterable.list[self._i]



