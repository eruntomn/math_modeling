import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


fig, ax = plt.subplots()
ball1, = plt.plot([], [], 'o', color='r', label='Ball')

def circle_move(R, vx0, vy0, time):
    x0 = vx0 * time
    y0 = -vy0 * time
    x = x0 + R
    y = y0 - R
    return x, y

plt.axis('equal')
ax.set_xlim(-5, 10)
ax.set_ylim(-100, 100)  # поменять направление

def animate(i):
    ball1.set_data(circle_move(R=0.1, vx0=0.01, vy0=0.01, time=2*i))

ani = animation.FuncAnimation(fig, animate, frames=360, interval=30)
ani.save('proba.gif')