from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
from matplotlib.widgets import Button
from matplotlib.widgets import RadioButtons


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# вершины пирамиды
v = np.array([[0, 0, 1]])
for i in range(1, 6):
    x = np.cos(2 * np.pi * i / 5)
    y = np.sin(2 * np.pi * i / 5)
    v = np.vstack([v, [x, y, 0]])

ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])

# стороны пирамиды
verts = [[v[0], v[1], v[5]], [v[0], v[1], v[2]], [v[0], v[2], v[3]], [v[0], v[3], v[4]], [v[0], v[4], v[5]],
         [v[1], v[2], v[3], v[4], v[5]]]

# отрисовка
ax.add_collection3d(Poly3DCollection(verts, facecolors='pink', linewidths=1, edgecolors='purple', alpha=0.25))



def iButton(event):
    ax.view_init(28, -136)
    plt.draw()


axes_ibutton_add = plt.axes([0.55, 0.05, 0.4, 0.075])
ibutton_add = Button(axes_ibutton_add, 'Изометрическая')
ibutton_add.on_clicked(iButton)


def oButton(event):
    ax.view_init(-2, -36)
    plt.draw()


axes_obutton_add = plt.axes([0.06, 0.05, 0.4, 0.075])
obutton_add = Button(axes_obutton_add, 'Ортографическая')
obutton_add.on_clicked(oButton)

lines_visibility = plt.axes([0.02, 0.85, 0.37, 0.11], facecolor='lavenderblush')
radio = RadioButtons(lines_visibility, ('Каркасная отрисовка', 'Убрать видимые линии'))


def lines(a):
    condition = {'Каркасная отрисовка': 0.20, 'Убрать видимые линии': 1}
    alpha = condition[a]
    ax.add_collection3d(Poly3DCollection(verts, facecolors='pink', linewidths=1, edgecolors='purple', alpha=alpha))
    plt.draw()
radio.on_clicked(lines)

plt.show()
