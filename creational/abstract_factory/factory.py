from patterns.creational.abstract_factory.product import LinuxButton, LinuxAlertView, Button, MacButton, MacAlertView


# --- Factory ---

class UIFactory:
    def create_button(self):
        raise NotImplementedError

    def create_alert_view(self, button: Button):
        raise NotImplementedError


# --- Concrete Factories ---

class LinuxFactory(UIFactory):
    def create_button(self):
        return LinuxButton()

    def create_alert_view(self, button: LinuxButton):
        return LinuxAlertView(button)


class MacFactory(UIFactory):
    def create_button(self):
        return MacButton()

    def create_alert_view(self, button: MacButton):
        return MacAlertView(button)
