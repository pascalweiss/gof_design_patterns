"""
- Pattern Name -
Command

- Intent -
"Encapsulate a request as an object, thereby letting you parameterize clients with
different requests, queue or log requests, and support undoable operations." (GoF - Design Patterns)

- Also Known As -
Action, Transaction
"""

import unittest
from behavioral.command.Invoker import Invoker
from behavioral.command.command import *


class TestClient(unittest.TestCase):

    def setUp(self):
        self.remote_controller = Invoker()

    def test_receiver_1(self):
        # The command is coupled with the receiver
        receiver = Receiver1()
        left = CommandReceiver1Left(receiver)
        right = CommandReceiver1Right(receiver)

        # remote_controller is decoupled from the receiver
        self.remote_controller.a_button_pressed(left)
        self.remote_controller.b_button_pressed(right)
        self.remote_controller.back_pressed()

    def test_receiver_2(self):
        receiver = Receiver2()
        forward = CommandReceiver2Forward(receiver)
        backward = CommandReceiver2Backward(receiver)

        # by decoupling the remote_controller can be used for various receivers
        self.remote_controller.a_button_pressed(forward)
        self.remote_controller.b_button_pressed(backward)
        self.remote_controller.back_pressed()