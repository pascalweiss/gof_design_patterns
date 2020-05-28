# In this example, the invoker represents a gamepad with three buttons:
# a, b and back.

class Invoker:
    undo_command = None

    def a_button_pressed(self, command_a):
        command_a.execute()
        self.undo_command = command_a

    def b_button_pressed(self, command_b):
        command_b.execute()
        self.undo_command = command_b

    def back_pressed(self):
        self.undo_command.undo()
