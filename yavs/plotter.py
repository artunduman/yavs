from abc import ABC, abstractmethod


class Plotter(ABC):
    @abstractmethod
    def set(self, index, value):
        pass

    @abstractmethod
    def refresh(self, data):
        pass

    @abstractmethod
    def animate(self):
        pass


class MatplotlibPlotter(Plotter):

    def __init__(self):
        pass  # TODO

    def set(self, index, value):
        pass

    def refresh(self, data):
        pass

    def animate(self):
        pass
