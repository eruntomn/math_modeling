import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 200
t = np.linspace(0, 5, frames)

def move_func(z, t):
    x, v_x, y, v_y = z
    dxdt = v_x
    dv_xdt = 0
    dydt = v_y
    dv_ydt = - g - k * v_y0**2
    return dxdt, dv_xdt, dydt, dv_ydt

k = 0.1
v = 1
v0 = 20
g = 9.8
x0 = 0
v_x0 = 0 #тк мяч кидают вверх, то x0 будет равен 0
y0 = 0
v_y0 = v0
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

ball, = plt.plot([], [], 'o', color = 'b')
ball_line, = plt.plot([], [], '-', color = 'r')
def animate(i):
    ball.set_data(solve_func(i, 'point'))
    ball_line.set_data(solve_func(i, 'line'))

ani = FuncAnimation(fig, animate, frames=frames, interval=30)
edge = 15
ax.set_xlim(-5, 5)
ax.set_ylim(-200, 6)

ani.save('tt2.gif')