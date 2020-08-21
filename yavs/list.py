from collections import MutableSequence


class PlottableList(MutableSequence):
    def __init__(self, plotter, iterable=()):
        self._data = []
        self.extend(iterable)
        self._plotter = plotter
        self._plotter.refresh(self._data)

    def insert(self, index, value):
        self._data.insert(index, value)
        self._plotter.refresh(self._data)

    def __delitem__(self, index):
        del self._data[index]
        self._plotter.refresh(self._data)

    def __setitem__(self, index, value):
        self._plotter.set(index, value)
        self._data.__setitem__(index, value)

    def __getitem__(self, key):
        return self._data[key]

    def __len__(self):
        return len(self._data)
