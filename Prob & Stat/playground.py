import numpy as np

#some example data
np.random.seed(0)
x = np.random.randint(1, 10, 30)
y = x+np.random.normal(0, 1, 30)
#some confidence interval
print(type(x))
print(x)