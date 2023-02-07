import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


alpha = np.arange(0, 180)
def rost():
    v = r * s * np.cos(alpha) * t
    return v 

