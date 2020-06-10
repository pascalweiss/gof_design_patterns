"""
- Pattern Name -
Observer

- Intent -
"Define a one-to-many dependency between objects so that when one object
changes state, all its dependents are notified and updated automatically." (GoF - Design Patterns)

- Also Known As -
Dependents, Publish-Subscribe
"""

import unittest
from hamcrest import greater_than, assert_that
from patterns.behavioral.observer.observable import TempObservable, HumidObservable
from patterns.behavioral.observer.observer import TempObserver, HumidObserver


class TestClient(unittest.TestCase):
    def test(self):
        temp_sensor  = TempObservable()
        humid_sensor = HumidObservable()

        kitchen_display = TempObserver(temp_sensor)
        living_room_display = TempObserver(temp_sensor)
        basement_display = HumidObserver(humid_sensor)

        temp_sensor.test_run()
        humid_sensor.test_run()

        assert_that(len(kitchen_display.get_temp_observations()), greater_than(0))
        assert_that(len(living_room_display.get_temp_observations()), greater_than(0))
        assert_that(len(basement_display.get_humid_observations()), greater_than(0))

