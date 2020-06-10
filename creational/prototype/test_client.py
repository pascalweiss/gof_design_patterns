"""
- Pattern Name -
Prototype

- Intent -
Specify the kinds of objects to create using a prototypical instance, and create new objects
by copying the prototype.

- Motivation -
Suppose we are building a graph editor and we want to implement the new feature "duplicate shape".
When the user applies "duplicate shape", the editor will take the currently selected shape
and duplicate it by creating a new shape of the same type with the same properties.
"""


import unittest
from hamcrest import assert_that, has_length, equal_to
from creational.prototype.client import Editor
from creational.prototype.prototype import Circle, Rectangle
from creational.prototype.utils.utils import get_circles


class TestClient(unittest.TestCase):

    def test(self):
        circle = Circle(3.5, "green")
        rectangle = Rectangle(4.5, 3.0, "red")
        editor = Editor([circle, rectangle])

        editor.select(circle)
        editor.duplicate()

        circles = get_circles(editor.shapes)
        assert_that(circles, has_length(2))
        for c in circles:
            assert_that(c.radius, equal_to(circle.radius))
            assert_that(c.color, equal_to(circle.color))
