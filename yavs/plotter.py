from abc import ABC, abstractmethod
from enum import Enum
from matplotlib import pyplot as plt
from matplotlib import animation
from typing import List
import logging

logger = logging.getLogger('yavs')

class Action(Enum):
    HIGHLIGHT = 1
    SET = 2
    SET_ALL = 3


class Color(Enum):
    RED = 1
    GREEN = 2


class PlottingHistory(ABC):
    """
    This is a middleware between the custom list and a plotter
    The reason we have this interface decoupled from the plotter is
    some animation software (unlike matplotlib) might support
    diff animations, where given a diff, frame is rendered more efficiently
    """
    @abstractmethod
    def set(self, index, value):
        pass

    @abstractmethod
    def refresh(self, data):
        pass

    @abstractmethod
    def highlight(self, index):
        pass

    @abstractmethod
    def next_action(self):
        pass


class ConcretePlottingHistory(PlottingHistory):
    def __init__(self):
        self._actions = []
        self._action_index = 0

    # TODO make actions more robust with typing
    def set(self, index, value):
        self._actions.append((Action.SET, index, value))

    def refresh(self, data):
        self._actions.append((Action.SET_ALL, data))

    def highlight(self, index):
        self._actions.append((Action.HIGHLIGHT, index))

    def next_action(self):
        if self._action_index >= len(self._actions):
            return None
        action = self._actions[self._action_index]
        self._action_index += 1
        return action


class Plotter(ABC):
    """
    This class is responsible for animating the actions from a
    plotting history object
    """
    def __init__(self, plotting_histories: List[PlottingHistory]):
        self._plotting_histories = plotting_histories

    @abstractmethod
    def animate(self):
        pass


class MatplotlibPlotter(Plotter):
    def __init__(self, plotting_histories: List[PlottingHistory]):
        super(MatplotlibPlotter).__init__(plotting_histories)
        self.ACTION_DISPATCH = {
            Action.HIGHLIGHT: self._highlight,
            Action.SET_ALL: self._set_all,
            Action.SET: self._set,
        }
        self._bars = []

    def _highlight(self, index):
        return

    @staticmethod
    def _to_bars(data):


    def _set_all(self, data):
        self._bars = self._to_bars(data)
        return self._bars

    def _set(self, index, value):
        self._bars[index] = value
        return self._to_bars(self._bars)

    def animate(self):
        """
        Animates the plotting history with matplotlib implementation
        """

        n, bins, patches = plt.hist(values, bins=np.arange(50, 140, 2), align='left', color='g')
        figure = plt.figure()
        rows = len(self._plotting_histories)
        axs = figure.subplots(rows)
        axs.set_xticks([])
        axs.set_yticks([])

        while action := self._plotting_histories[0].next_action():  # TODO change
            logger.debug("Action: {}".format(action))
            action_func = self.ACTION_DISPATCH[action[0]]
            action_func(*action[1:])
        # TODO more manipulation
        anim = animation.FuncAnimation()
