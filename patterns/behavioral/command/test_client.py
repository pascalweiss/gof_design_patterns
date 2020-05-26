import unittest
from patterns.behavioral.command.Invoker import Invoker
from patterns.behavioral.command.commands import *


class TestClient(unittest.TestCase):

    def setUp(self):
        self.remote_controller = Invoker()

    def test_receiver_1(self):
        receiver = Receiver1()
        left = CommandReceiver1Left(receiver)
        right = CommandReceiver1Right(receiver)

        # remote_controller is decoupled from receiver
        self.remote_controller.a_button_pressed(left)
        self.remote_controller.b_button_pressed(right)
        self.remote_controller.undo_pressed()

    def test_receiver_2(self):
        receiver = Receiver2()
        forward = CommandReceiver2Forward(receiver)
        backward = CommandReceiver2Backward(receiver)

        # remote_controller can be used for various receivers
        self.remote_controller.a_button_pressed(forward)
        self.remote_controller.b_button_pressed(backward)
        self.remote_controller.undo_pressed()