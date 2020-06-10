

# ----------------- Observer ----------------------

class IObserver:
    def __init__(self, observable):
        self.observations = []
        self.observable = observable
        self.observable.attach(self)

    def update(self):
        raise NotImplementedError


# --------------- Concrete Observers ------------------

class TempObserver(IObserver):
    def update(self):
        self.observations.append(self.observable.get_temp())

    def get_temp_observations(self):
        return self.observations


class HumidObserver(IObserver):
    def update(self):
        self.observations.append(self.observable.get_humid())

    def get_humid_observations(self):
        return self.observations
