from patterns.behavioral.command.receiver import Receiver1, Receiver2


# -----------------Command Interface---------------------------------

class Command:
    def execute(self):
        raise NotImplementedError

    def undo(self):
        raise NotImplementedError


# ------------------Concrete Commands: Receiver1---------------------------------

# Command A
class CommandReceiver1Left(Command):
    def __init__(self, receiver: Receiver1):
        self.receiver = receiver

    def execute(self):
        self.receiver.step_left()

    def undo(self):
        self.receiver.step_right()


# Command B
class CommandReceiver1Right(Command):
    def __init__(self, receiver: Receiver1):
        self.receiver = receiver

    def execute(self):
        self.receiver.step_right()

    def undo(self):
        self.receiver.step_left()


# ------------------Concrete Commands: Receiver1---------------------------------

# Command A
class CommandReceiver2Forward(Command):
    def __init__(self, receiver: Receiver2):
        self.receiver = receiver

    def execute(self):
        self.receiver.step_forward()

    def undo(self):
        self.receiver.step_backward()


# Command B
class CommandReceiver2Backward(Command):
    def __init__(self, receiver: Receiver2):
        self.receiver = receiver

    def execute(self):
        self.receiver.step_backward()

    def undo(self):
        self.receiver.step_forward()
