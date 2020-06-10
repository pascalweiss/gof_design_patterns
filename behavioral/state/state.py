

# --- State ----

class GateState:
    def __init__(self, gate):
        self.gate = gate

    def handle_valid(self):
        raise NotImplementedError

    def handle_entered(self):
        raise NotImplementedError


# --- Concrete States ---

class Open(GateState):
    def handle_entered(self):
        self.gate.state = Closed(self.gate)

    def handle_valid(self):
        self.gate.state = Open(self.gate)


class Closed(GateState):
    def handle_entered(self):
        self.gate.state = Closed(self.gate)

    def handle_valid(self):
        self.gate.state = Open(self.gate)
