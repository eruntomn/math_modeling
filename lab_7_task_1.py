import matplotlib.pyplot as plt
import numpy as np

'''
t = np.arange(-10, 10, 0.1)
R = 5

x = R * (t - np.sin(t)**3)
y = R * (1 - np.cos(t)**3)

plt.plot(x, y, '-', lw = 3)
plt.axis('equal')
plt.savefig('task1.png')
'''

t = np.arange(-10, 10, 0.1)
R = 3

x = R * np.cos(t)**3
y = R * np.sin(t)**3

plt.plot(x, y, '-', lw = 3)
plt.axis('equal')
plt.savefig('task2.png')