import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


'''t = np.arange(-10, 10, 0.1)
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
plt.savefig('task2.png')'''

fig, ax = plt.subplots()
prymaya, = plt.plot([], [], '-', lw=2)

fig, ax = plt.subplots()
ball = plt.plot([], [], 'o', label='r')

ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)

def circle(t, r):
    x = r * (t - np.sin(t))
    y = r * (1 - np.cos(t))
    return x, y
def circle_move(t1, R):
    x1 = R * (t1 - np.sin(t1))
    y1 = R * (1 - np.cos(t1))
    return x1, y1

def animate(i):
    prymaya.set_data(circle(t=np.arange(-10, 10), r = 5))
def animate1(j):
    ball.set_data(circle_move(t1=np.arange(-10, 10), R = 10))

ani = FuncAnimation(fig, animate, frames=100, interval=30)
ani = FuncAnimation(fig, animate1, frames = 100, interval=30)
ani.save('pr.gif')