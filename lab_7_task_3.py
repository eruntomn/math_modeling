import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

fig, ax = plt.subplots()
btf, = plt.plot([], [], '-', color='r')

def circle_move(t):
    x = np.sin(t) * (np.exp(np.cos(t)) - 2*np.cos(4*t) + np.sin(t//12)**5)
    y = np.cos(t) * (np.exp(np.cos(t)) - 2*np.cos(4*t) + np.sin(t//12)**5)
    return x, y

plt.axis('equal')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

def animate(i):
    btf.set_data(circle_move(t=i))

ani = animation.FuncAnimation(fig, animate, frames=np.arange(0, 2*np.pi, 0.1), interval=30)
ani.save('butterfly.gif')
'''

fig, ax = plt.subplots()
hrt, = plt.plot([], [], color='r')

def circle_move(t):
    x = 16 * np.sin(t)**3
    y = 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)
    return x, y

plt.axis('equal')
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)

def animate(i):
    hrt.set_data(circle_move(t=np.arange(0, 2*np.pi, 0.1)))
ani = animation.FuncAnimation(fig, animate, frames = 100, interval=30)
ani.save('heart.gif')
'''