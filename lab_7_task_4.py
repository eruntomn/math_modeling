import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

fig, ax = plt.subplots()
ani_obj, = plt.plot([], [], color='r')

def circle_move(xn1, yn1, c, d):
    xn = xn1**2 - yn1**2 +c
    yn = 2*xn1 * yn1+ d
    return xn, yn
plt.axis('equal')


