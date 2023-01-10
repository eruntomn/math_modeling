'''import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='b')

def circle_move(t, y0, vy, x, g=9.8):
    y = y0 + vy*t + g*t**2/2
    return y

plt.axis('equal')
ax.set_ylim(0, 10)
ax.set_xlim(-5, 5)

def animate(i):
    ball.set_data(circle_move(y0=10, vy=5, t=i, x=5))

ani =animation.FuncAnimation(fig, animate, frames=np.arange(0, 2*np.pi), interval=20)
ani.save('proba.gif')'''


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


fig, ax = plt.subplots()
ball1, = plt.plot([], [], 'o', color='b', label='Ball')

def circle_move(R, vx0, vy0, time):
    x0 = vx0 * time
    y0 = vy0 * time
    alpha=np.arange(0, 2*np.pi, 0.1)
    x = x0 + R
    y = y0 + R
    return x, y

plt.axis('equal')
ax.set_xlim(True)
ax.set_ylim(1, -1)

def animate(i):
    ball1.set_data(circle_move(R=0.1, vx0=0.1, vy0=0.01, time=i))

ani = animation.FuncAnimation(fig, animate, frames=300, interval=30)
ani.save('proba.gif')