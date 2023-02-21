# Значения переменной величины взять в пределах ∈ [-1, 1], начальные значения изменяемых величин: x(0) = 5, y(0) = -7

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-1, 1, 0.01)

def div(sys, t):
    x, y = sys

    dxdt = 3*x - 2*y + (np.e)**(3*t) / np.e**t + 1
    dydt = x - (np.e**(3*t)) / np.e**t + 1

    return dxdt, dydt

x0 = 5
y0 = - 7
sys0 = x0, y0

sol = odeint(div, sys0, t)

plt.plot(t, sol[:, 1], 'b')
plt.savefig('task_2.png')