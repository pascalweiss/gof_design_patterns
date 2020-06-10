"""
- Pattern Name -
State

- Intent -
"Allow an object to alter its behavior when its internal state changes.
The object will appear to change its class." (GoF - Design Patterns)

- Also Known As -
Objects for States

- Example Description -
In this example, the State pattern is applied on a gate. The gate may be used at the entry of a
concert hall or a cinema. To control if a guest is authorised to enter, the guest has to show
the barcode on his ticket to a scanner.
Here the gate is represented as the following finite state machine:

(Q, Σ, T, q0, F)
States:         Q = (open, closed)
Actions:        Σ = (entered, valid)
initial state: q0 = closed
Transitions     F = {
                        (open, entered) -> closed,
                        (open, valid)   -> valid,
                        (closed, entered) -> closed,
                        (closed, valid)   -> open
                    }
"""


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
