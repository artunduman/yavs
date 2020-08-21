from yavs.algorithm_base import SortingAlgorithm
from yavs.list import PlottableList


class QuickSort(SortingAlgorithm):
    def sort(self, array: PlottableList[int]):
        self._quicksort(array, 0, len(array) - 1)

    def _partition(self, arr, low, high):
        i = low - 1
        pivot = arr[high]     # pivot

        for j in range(low, high):

            # If current element is smaller than or
            # equal to pivot
            if arr[j] <= pivot:

                # increment index of smaller element
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i + 1

    def _quicksort(self, arr, low, high):
        if low < high:

            # pi is partitioning index, arr[p] is now
            # at right place
            pi = self._partition(arr, low, high)

            # Separately sort elements before
            # partition and after partition
            self._quicksort(arr, low, pi-1)
            self._quicksort(arr, pi+1, high)
