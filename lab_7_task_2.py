import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='b', label='Ball')

def circle_move(R, vx0, vy0, time):
    x0 = vx0
    y0 = vy0
    alpha=np.arange(0, 2*np.pi, 0.1)
    x = x0 + R*np.cos(alpha)
    y = y0 + R*np.sin(alpha)
    return x, y

edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    ball.set_data(circle_move(R=0.01*i, vx0=0.01, vy0=0.01, time=i))

ani = animation.FuncAnimation(fig, animate, frames=100, interval=30)
ani.save('1.gif')


fig, ax = plt.subplots()
ball1, = plt.plot([], [], 'o', color='b', label='Bal1l')

def move(R, vx0, vy0, time):
    x0 = vx0
    y0 = vy0
    alpha=np.arange(0, 2*np.pi, 0.1)
    x = x0 + R*np.cos(alpha)
    y = y0 + R*np.sin(alpha)
    return x, y

edge = 7
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animat(i):
    ball1.set_data(move(R=0.01*i, vx0=0.03, vy0=0.03, time=i))

ani = animation.FuncAnimation(fig, animat, frames=100, interval=30)
ani.save('1.gif')