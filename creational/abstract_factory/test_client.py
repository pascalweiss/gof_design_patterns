"""
- Pattern Name -
Abstract Factory

- Intent -
"Provide an interface for creating families of related or dependent objects without
specifying their concrete classes." (GoF - Design Patterns)

- Also Known As -
Kit
"""

import unittest
from patterns.creational.abstract_factory.factory import *
from patterns.creational.abstract_factory.product import *


class TestClient(unittest.TestCase):
    def test_linux(self):
        factory = LinuxFactory()
        button = factory.create_button()
        alert_view = factory.create_alert_view(button)
        assert isinstance(button, LinuxButton)
        assert isinstance(alert_view, LinuxAlertView)

    def test_mac(self):
        factory = MacFactory()
        button = factory.create_button()
        alert_view = factory.create_alert_view(button)
        assert isinstance(button, MacButton)
        assert isinstance(alert_view, MacAlertView)