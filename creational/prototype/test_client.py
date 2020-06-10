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
