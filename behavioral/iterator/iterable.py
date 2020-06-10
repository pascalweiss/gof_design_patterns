from behavioral.iterator.iterator import *
from behavioral.iterator.utils.util_tree import Node


# --- Iterable ---

class Iterable:
    def get_iterator(self):
        raise NotImplementedError

    def add(self, item):
        raise NotImplementedError


# --- Concrete Iterables ---

class ListIterable(Iterable):
    """
    This is a rather trivial iterable, as it is just a wrapper for a normal list
    """
    _list = []

    def add(self, item):
        self._list.append(item)

    def get_iterator(self):
        return ListIterator(self._list)


class TreeIterable(Iterable):
    _root = None

    def add(self, item):
        if self._root is None:
            self._root = Node(item)
        else:
            self._root.add(item)

    def get_iterator(self):
        return TreeIterator(self._root)


class AbsurdIterable(Iterable):
    """
    This is shows, how the iterator pattern can be applied even on absurd iterables
    """
    one = two = three = four = five = six = None
    _i = 0

    def add(self, item):
        if self._i is 0:
            self.one = item
        elif self._i is 1:
            self.two = item
        elif self._i is 2:
            self.three = item
        elif self._i is 3:
            self.four = item
        elif self._i is 4:
            self.five = item
        elif self._i is 5:
            self.six = item
        self._i += 1

    def get_iterator(self):
        return AbsurdIterator(self)


class EndlessIterable(Iterable):

    list = []

    def add(self, item):
        self.list.append(item)

    def get_iterator(self):
        return EndlessIterator(self)