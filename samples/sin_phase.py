import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0., 3*np.pi, 50)
phase = np.arange(0., 2 * np.pi, 2 * np.pi / 3)

for p in phase:
    plt.plot(x, np.sin(x + p))
plt.show()
