import unittest
from behavioral.state.context import Gate
from behavioral.state.state import Closed, Open


class TestClient(unittest.TestCase):
    def test(self):
        # check that initial state is "closed"
        gate = Gate()
        assert isinstance(gate.state, Closed)

        # Given that guest shows valid ticket: check that state changed to "open"
        gate.showed_valid()
        assert isinstance(gate.state, Open)

        # Given that guest showed valid ticket again: check that state stays "open"
        gate.showed_valid()
        assert isinstance(gate.state, Open)

        # Given that guest entered through the gate: Check that state changed to "closed"
        gate.guest_entered()
        assert isinstance(gate.state, Closed)

        # Given that guest tries to enter (without valid ticket): Check that state stays "closed"
        gate.guest_entered()
        assert isinstance(gate.state, Closed)
