import numpy as np
from matplotlib import pyplot as plt

c = np.loadtxt("centers.txt", skiprows=1)
c_ = np.loadtxt("_centers.txt", skiprows=1)

ax = plt.subplot(projection="3d")
ax.scatter(*c[:, 1:].T)
ax.scatter(*c_[:, 1:].T)
ax.set_aspect("equal")
ax.plot((-1.1e-1, 1.0e-1), (0.15e-1, 0.4e-1), (-0.1e-1, 0.4e-1))
plt.show()
