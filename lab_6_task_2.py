import matplotlib.pyplot as plt
import numpy as np
def giperbola(k):
    x = np.arange(19, -0.009, 0.09)
    y = k / x
    plt.plot(x, y, label='giperbola')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.legend()
    plt.savefig('pic_8.png')