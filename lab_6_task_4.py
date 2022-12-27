import matplotlib.pyplot as plt
import numpy as np
'''
def logarifm(a):
    f = np.arange(0, 8 * np.pi, 0.01)
    r = np.e**(a*f)
    x = r*np.cos(f)
    y = r*np.cos(f)
    plt.plot(x, y, label='logar')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.axis('equal')
    plt.savefig('pic_10_1.png')
logarifm(0.1)

def archim(b):
    f = np.arange(0, 8 * np.pi, 0.01)
    r = b * f
    x = r*np.cos(f)
    y = r*np.cos(f)
    plt.plot(x, y, label='arhim')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.axis('equal')
    plt.savefig('pic_10_2.png')
archim(0.2)'''

def gesl(c):
    f = np.arange(0.02, 8 * np.pi, 0.01)
    r = c / np.sqrt(f)
    x = r*np.cos(f)
    y = r*np.cos(f)
    plt.plot(x, y, label='gesl')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.axis('equal')
    plt.savefig('pic_10_3.png')
gesl(0.01)

def rosa(d):
    f = np.arange(0.01, 8, 0.01)
    r = np.sin(d*f)
    x = r*np.cos(f)
    y = r*np.cos(f)
    plt.plot(x, y, label='rosa')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.axis('equal')
    plt.savefig('pic_10_4.png')
rosa(9)