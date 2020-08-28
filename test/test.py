import numpy as np

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path
import matplotlib.animation as animation
import uuid

figure = plt.figure()
rows = 1
axs = figure.add_subplot()
axs.set_xticks([])
axs.set_yticks([])

datas = [[5, 6], [1, 3], [1, 9]]


def animate(data):
    print(data)
    axs.cla()
    bar = axs.bar(
        list(range(len(datas[0]))),        # X
        data,       # data
        1,                                   # width
        color='r'  # color
    )
    return [bar]


anim = animation.FuncAnimation(figure, animate, frames=datas, interval=1000)
plt.show()
