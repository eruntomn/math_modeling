import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Определяем переменную величину и количество кадров
frames = 200
t = np.linspace(0, 5, frames)
 
# Определяем функцию для системы диф. уравнений
def move_func(z, t):
    x, v_x, y, v_y = z
    dxdt = v_x
    dv_xdt = 0
    dydt = v_y * m 
    dv_ydt = m * g + m * a 
    return dxdt, dv_xdt, dydt, dv_ydt

# Определяем начальные значения и параметры
m = 100
a = 9.8
x0 = 0
v_x0 = 0
y0 = 2
v_y0 = v0
z0 = x0, v_x0, y0, v_y0

sol = odeint(move_func, z0, t)
# Решаем систему диф. уравнений
def solve_func(i, key):
    if key == 'point': # если принимает значение точки
        x = sol[i, 0]
        y = sol[i, 2]
    else:
        x = sol[:i, 0]
        y = sol[:i, 2]
    return x, y
  
# Строим решение в виде графика и анимируем
fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([], [], '-', color='r')

def animate(i):
    ball.set_data(solve_func(i, 'point'))
    ball_line.set_data(solve_func(i, 'line'))

ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

edge = 15
ax.set_xlim(0, edge)
ax.set_ylim(0, edge)

ani.save('tt4.gif')