
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r', label='Ball')
cyc, = plt.plot([], [], 'o', color='y', label='Ball')
traj, = plt.plot([], [], '-', color='b', label='Ball')
	
def cycloida(R, time):
    x = R*np.cos(time)**3
    y = R*np.sin(time)**3
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
    coords = cycloida(R=0.5, time=i/47)
    x.append(coords[0])
    y.append(coords[1])
    cyc.set_data(x[i], y[i])
    traj.set_data(x, y)
ani = animation.FuncAnimation(fig,
                              animate,
                              frames=280,
                              interval=30
                             )

ani.save('astroida.gif')