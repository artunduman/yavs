from collections import MutableSequence
from yavs.plotter import PlottingHistory


class PlottableList(MutableSequence):
    def __init__(self, plotting_history, iterable=()):
        self._data = []
        self.extend(iterable)
        self._plotting_history = plotting_history
        self._plotting_history.refresh(self._data)

    def insert(self, index, value):
        self._data.insert(index, value)
        self._plotting_history.refresh(self._data)

    def __delitem__(self, index):
        del self._data[index]
        self._plotting_history.refresh(self._data)

    def __setitem__(self, index, value):
        self._plotting_history.set(index, value)
        self._data.__setitem__(index, value)

    def __getitem__(self, key):
        return self._data[key]

    def __len__(self):
        return len(self._data)
