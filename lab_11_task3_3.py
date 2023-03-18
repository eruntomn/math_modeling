import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 200
t = np.linspace(0, 5, frames)

def move_func(z, t):
    x, v_x, y, v_y = z
    dxdt = v_x
    dv_xdt = -f
    dydt = v_y
    dv_ydt = - g + k * v_y
    return dxdt, dv_xdt, dydt, dv_ydt

f = 50
k = 1
alpha = 75 * np.pi / 180
v = 15
v0 = 20
g = 9.8
x0 = 0
v_x0 = v * np.cos(alpha)
y0 = 0
v_y0 = v * np.sin(alpha)
z0 = x0, v_x0, y0, v_y0

sol = odeint(move_func, z0, t)
def solve_func(i, key):
    if key == 'point':
        x = sol[i, 0]
        y = sol[i, 2]
    else:
        x = sol[:i, 0]
        y = sol[:i, 2]
    return x, y

fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color = 'g')
ball_line, = plt.plot([], [], '-', color = 'b')
def animate(i):
    ball.set_data(solve_func(i, 'point'))
    ball_line.set_data(solve_func(i, 'line'))

ani = FuncAnimation(fig, animate, frames=frames, interval=30)
edge = 15
ax.set_xlim(-5, edge)
ax.set_ylim(-5, edge)

ani.save('tt3_3.gif')