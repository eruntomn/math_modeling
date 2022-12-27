import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
object = plt.plot([], [], 'o', color='r', label='ball')

def update(R):
    t = np.arange(0, 2*np.pi, 0.1)
    x = R * np.cos(t)
    y = R * np.sin(t)
    return x, y

edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    ball.set_data(update(R-i))

ani = FuncAnimation(fig, update, frames=np.arange(0, 3, 0.1), interval=100)
ani.save('task3.gif')