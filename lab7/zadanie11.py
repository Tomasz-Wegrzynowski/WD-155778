import numpy as np

a = np.arange(12).reshape(3, 4)
b = a.reshape(4, 3)
c = a.reshape(2, 6)

a = a.ravel()
print(a)

b = b.ravel()
print(b)

c = c.ravel()
print(c)
