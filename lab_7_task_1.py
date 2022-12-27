import matplotlib.pyplot as plt
import numpy as np


t = np.arange(-10, 10, 0.1)
R = 5

x = R * (t - np.sin(t))
y = R * (1 - np.cos(t))

plt.plot(x, y, '-', lw = 3)
plt.axis('equal')
plt.savefig('task1.png')


t1 = np.arange(-10, 10, 0.1)
R1 = 3

x = R1 * np.cos(t1)**3
y = R1 * np.sin(t1)**3

plt.plot(x, y, '-', lw = 3)
plt.axis('equal')
plt.savefig('task2.png')