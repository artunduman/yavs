from yavs.algorithm_base import SortingAlgorithm
from yavs.plotter import Plotter, MatplotlibPlotter
from typing import List
from yavs.list import PlottableList
import random


class SortingVisualizer:
    def __init__(self, plotting_history, plotter: Plotter, sorting_algorithms: List[SortingAlgorithm]):
        self._plotting_history = plotting_history
        self._plotter = plotter
        self._sorting_algorithms = sorting_algorithms

    def fill_array(self, array: PlottableList):
        # TODO allow for custom array types and length
        for i in range(1, 400):
            array.append(i)
        random.shuffle(array)  # TODO check if correct

    def run(self):
        array = PlottableList(self._plotting_history)
        self.fill_array(array)

        for algorithm in self._sorting_algorithms:
            algorithm.sort(array)



    def _create_list(self):
        pass
