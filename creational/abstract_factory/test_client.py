import unittest
from creational.abstract_factory.factory import *
from creational.abstract_factory.product import *


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