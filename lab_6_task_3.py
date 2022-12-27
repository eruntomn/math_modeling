import matplotlib.pyplot as plt
import numpy as np

def ellips(a, b):
    x = np.arange(-2, 2, 0.1)
    y = np.arange(-2, 2, 0.1)
    X, Y = np.meshgrid(x, y)
    fxy = X ** 2 / a ** 2 + Y ** 2 / b ** 2
    plt.contour(x, y, fxy)
    plt.axis('equal')
    plt.legend()
    plt.savefig('pic_9.png')
ellips(3, 5)