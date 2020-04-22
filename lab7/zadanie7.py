import numpy as np

a = np.arange(6).reshape(2,3)
a = np.sin(a)
b = np.arange(6).reshape(2,3)
b = np.cos(b)
c=a+b
print(c)