import numpy as np

a = np.array([2, 1, 4, 5, 5, 6, 2, 1, 7]).reshape(3, 3)
b = np.array([3, 2, 1, 4, 5, 1, 5, 6, 9, 2, 1, 7, 2, 8, 5, 3]).reshape(4, 4)

print(a.min(axis=0))
print(a.min(axis=1))
print(b.min(axis=0))
print(b.min(axis=1))
