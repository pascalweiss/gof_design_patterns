"""
- Pattern Name -
Iterator

- Intent -
"Provide a way to access the elements of an aggregate object sequentially without
exposing its underlying representation." (GoF - Design Patterns)

- Also Known As -
Cursor
"""

import unittest
from hamcrest import equal_to, assert_that
from behavioral.iterator.iterable import ListIterable, TreeIterable, AbsurdIterable, EndlessIterable


def aggregation_test(iterator):
    aggregation = ""
    while iterator.has_next():
        item = iterator.get_next()
        aggregation = aggregation + str(item)
        print(aggregation)
    assert_that(aggregation, equal_to("123456"))


class TestClient(unittest.TestCase):

    def test_list(self):
        iterable = ListIterable()
        for i in range(1,7):
            iterable.add(i)
        aggregation_test(iterable.get_iterator())

    def test_tree(self):
        iterable = TreeIterable()
        for i in [5,2,1,4,3,6]:
            iterable.add(i)
        aggregation_test(iterable.get_iterator())

    def test_absurd(self):
        iterable = AbsurdIterable()
        for i in range(1, 7):
            iterable.add(i)
        aggregation_test(iterable.get_iterator())

    def test_endless(self):
        iterable = EndlessIterable()
        for i in range(1, 4):
            iterable.add(i)
        aggregation = ""
        iter = iterable.get_iterator()
        while iter.has_next() and len(aggregation) < 7:
            aggregation += str(iter.get_next())
        assert_that(aggregation, equal_to("1231231"))




