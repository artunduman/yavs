from abc import ABC, abstractmethod


class PlottingHistory(ABC):
    @abstractmethod
    def set(self, index, value):
        pass

    @abstractmethod
    def refresh(self, data):
        pass

    @abstractmethod
    def highlight(self, index):
        pass


class Plotter(ABC):
    def __init__(self, plotting_history: PlottingHistory):
        self._plotting_history = plotting_history

    @abstractmethod
    def animate(self):
        pass


class MatplotlibPlotter(Plotter):
    def animate(self):
        """
        Animates the plotting history with matplotlib implementation
        """
        pass
