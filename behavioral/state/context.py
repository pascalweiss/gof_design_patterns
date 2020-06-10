# --- Context ---

from behavioral.state.state import Closed


class Gate:
    def __init__(self):
        # sets the initial state
        self.state = Closed(self)

    def showed_valid(self):
        self.state.handle_valid()

    def guest_entered(self):
        self.state.handle_entered()
