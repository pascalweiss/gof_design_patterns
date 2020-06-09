

# ----------------- Products ------------------

class Button:
    pass


class AlertView:
    button = None


# --- Concrete Products ---

class LinuxButton(Button):
    pass


class MacButton(Button):
    pass


class LinuxAlertView(AlertView):
    def __init__(self, button: LinuxButton):
        self.button = button


class MacAlertView(AlertView):
    def __init__(self, button: MacButton):
        self.button = button
