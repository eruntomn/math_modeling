'''import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


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


fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r')

ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)

def circle(t, r):
    x = r * (t - np.sin(t))
    y = r * (1 - np.cos(t))
    return x, y


def animate(i):
    ball.set_data(circle(t=np.arange(-10, 10), r = 5))

ani = FuncAnimation(fig, animate, frames=100, interval=30)

ani.save('pr.gif')'''


import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r', label='Ball')
cyc, = plt.plot([], [], 'o', color='y', label='Ball')
traj, = plt.plot([], [], '-', color='b', label='Ball')
	
def cycloida(R, time):
    x = R*(time - np.sin(time)) - R
    y = R*(1 - np.cos(time)) - R
    return x, y

def circle_move(R, vx0, vy0, time):
    x0 = vx0 * time + R
    y0 = vy0 * time + R
    alpha = np.arange(0, 2*np.pi, 0.1)
    x = x0 + R*np.cos(alpha)- R
    y = y0 + R*np.sin(alpha)
    return x, y

edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

x, y = [], []
def animate(i):
    ball.set_data(circle_move(R=0.5, vx0=0.1, vy0=0.00, time=i))
    coords = cycloida(R=0.5, time=i/50)
    x.append(coords[0])
    y.append(coords[1])
    cyc.set_data(x[i], y[i])
    traj.set_data(x, y)
ani = animation.FuncAnimation(fig,
                              animate,
                              frames=100,
                              interval=30
                             )

ani.save('cicloida.gif')