# y(0) = 1, z(0) = -3

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.1)

def diff_func(sys, x): 
    y, z = sys

    dydx = y**2*z

    dzdx = z/x - y*z**2

    return dydx, dzdx

y0 =  1
z0 = -3
sys0 = y0, z0

sol = odeint(diff_func, sys0, x)

plt.plot(x, sol[:, 1], 'b')
plt.savefig('task_1.png')