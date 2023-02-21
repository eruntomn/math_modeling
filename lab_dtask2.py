# Значения переменной величины взять в пределах ∈ [0, 5], начальные значения изменяемых величин: y(0) = 0, dy(0)/dt = 1

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.01)

def div(sys, x):
    y, z = sys

    dydx = z
    dzdx = (z**2 - 3*y**2 / x**0.5) / y
    return dydx, dzdx

y0 = 0
x0 = 1
sys0 = y0, x0

sol = odeint(div, sys0, x)

plt.plot(x, sol[:, 1], 'b')
plt.savefig('task_dop_2.png')