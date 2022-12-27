import matplotlib.pyplot as plt
import numpy as np

def ellips(z, p):
    f = np.arange(-2, 8, 0.01)
    r = p / (1 + z * np.cos(f))
    x = r * np.cos(f)
    y = r * np.sin(f)
    plt.plot(x, y, label='ellips')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.axis('equal')
    plt.savefig('pic_12.png')
ellips(10, 2)