from yavs.algorithm_base import SortingAlgorithm
from yavs.sorting_visualizer import SortingVisualizer
from yavs.plotter import MatplotlibPlotter, Plotter

class Builder:
    def __init__(self):
        self._sorting_algorithms = []  # Type: List[SortingAlgorithm]
        self._plotter = self._default_plotter()  # Type: Plotter

    @staticmethod
    def _default_plotter():
        return MatplotlibPlotter()

    def reset(self):
        self.__init__()

    def sorting_algorithm(self, algorithm: SortingAlgorithm):
        self._sorting_algorithms.append(algorithm)

    def plotter(self, plotter: Plotter):
        self._plotter = plotter

    def build(self):
        return SortingVisualizer(
            plotter=self._plotter,
            sorting_algorithms=self._sorting_algorithms
        )
