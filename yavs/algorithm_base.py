from abc import ABC, abstractmethod
from yavs.list import PlottableList


class SortingAlgorithm(ABC):
    @abstractmethod
    def sort(self, array: PlottableList[int]):  # This list has the same interface as a Python list
        pass
