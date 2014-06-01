import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0., 3*np.pi, 50)
phase = np.arange(0., 2 * np.pi, 2 * np.pi / 3)
#style = ['r:', 'g--', 'py']
style = ['r--', 'bs', 'g^']

for p, s in zip(phase, style):
    plt.plot(x, np.sin(x + p), s)

plt.grid()
plt.show()
