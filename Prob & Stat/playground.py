from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-4,4,0.001)
print(x)
print(norm.pdf(x))