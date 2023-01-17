import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()

star, = plt.plot([], [], color='r')

alpha = np.arange(0, 4*np.pi, 0.1)
x = 12* np.cos(alpha) + 8*np.cos(1.5*alpha)
y = 12*np.sin(alpha) - 8*np.sin(1.5*alpha)

ax.set_xlim(-25, 25)
ax.set_ylim(-25, 25)
plt.axis('equal')

#вращение
def rotate(t):
    t = t * np.pi / 180
    X = x * np.cos(t) - y * np.sin(t)
    Y = y * np.cos(t) + x * np.sin(t)
    return X, Y

def animate(i):
    star.set_data(rotate(t=i))

ani = animation.FuncAnimation(fig, animate, frames=100, interval=50)
ani.save('star.gif')