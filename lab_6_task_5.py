import matplotlib.pyplot as plt
import numpy as np

a = 1
A = 1
def lissagy(b, B, t):
    g = np.pi / 2
    x = A * np.sin(a*t + g)
    y = B * np.sin(b*t)
    X, Y = np.meshgrid(x, y)
    plt.plot(x, y, label='lissagy')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.axis('equal')
    plt.savefig('pic_11.png')
lissagy(0.5, 2, 3)