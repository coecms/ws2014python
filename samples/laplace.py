import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

plt.ion()

x_ax = np.linspace(0., 1., 101)
y_ax = np.linspace(0., 1., 101)
x, y = np.meshgrid(x_ax, y_ax)

phi = np.zeros_like(x)
phi[-1, :] = np.sin(np.pi * x_ax)

N_iter = 100000
for i in xrange(N_iter):
    phi[1:-1, 1:-1] = 0.25 * (phi[:-2, 1:-1] + phi[2:, 1:-1]
                                    + phi[1:-1, :-2] + phi[1:-1, 2:])

plt.pcolormesh(x, y, phi)
plt.show()

#fig = plt.figure()
#ax = fig.gca(projection='3d')
#ax.plot_surface(x, y, phi)

#phi_exact = np.sinh(np.pi * y) / np.sinh(np.pi) * np.sin(np.pi * x)
#ax.(x, y, phi - phi_exact, color='r')

raw_input('press enter')
