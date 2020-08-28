from yavs.algorithm_base import SortingAlgorithm
from yavs.sorting_visualizer import SortingVisualizer
from yavs.plotter import MatplotlibPlotter, Plotter, PlottingHistory, ConcretePlottingHistory


class Builder:
    def __init__(self):
        self._sorting_algorithms = []  # Type: List[SortingAlgorithm]
        self._plotter = self._default_plotter()  # Type: Plotter
        self._plotting_history_class = self._default_plotting_history()

    @staticmethod
    def _default_plotter():
        return MatplotlibPlotter()

    @staticmethod
    def _default_plotting_history():
        return ConcretePlottingHistory()

    def reset(self):
        self.__init__()

    def sorting_algorithm(self, algorithm: SortingAlgorithm):
        self._sorting_algorithms.append(algorithm)

    def plotter(self, plotter: Plotter):
        self._plotter = plotter

    def plotting_history(self, plotting_history_class):
        if not issubclass(plotting_history_class, PlottingHistory):
            raise ValueError("The argument class should be subclass of {}".format(PlottingHistory.__class__))
        self._plotting_history_class = plotting_history_class


    def build(self):
        return SortingVisualizer(
            plotter=self._plotter,
            sorting_algorithms=self._sorting_algorithms
        )
