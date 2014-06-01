import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d

x_ax = np.linspace(-2., 2., 101)
y_ax = np.linspace(-2., 2., 101)
x, y = np.meshgrid(x_ax, y_ax)

z = (x - 0.5) * np.exp(-np.sqrt(x**2 + y**2))

fig = plt.figure()
ax = fig.gca(projection='3d')
#ax.plot_surface(x, y, z, cmap=cm.jet)
#ax.contour(x, y, z, 20)
ax.plot(x_ax, np.sin(x_ax), zs=-0.6, zdir='z')
plt.show()
