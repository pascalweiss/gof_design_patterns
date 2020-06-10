from random import random


# ---------------------- Observable --------------------------

class IObservable:
    def __init__(self):
        self.__observers = []

    def attach(self, observer):
        self.__observers.append(observer)

    def detach(self, observer):
        self.__observers = [obs for obs in self.__observers if obs is not observer]

    def notify(self):
        for obs in self.__observers:
            obs.update()


# --- Concrete Observables ---

class TempObservable(IObservable):
    temp = 0

    def test_run(self):
        for _ in range(3):
            self.temp = random() + 25
            self.notify()

    def get_temp(self):
        return self.temp


class HumidObservable(IObservable):
    humid = 0

    def test_run(self):
        for _ in range(4):
            self.humid = random() + 74
            self.notify()

    def get_humid(self):
        return self.humid
