import numpy as np

def tablica(n):
    a = np.arange(1, n*n+1, 1)
    a.shape = (n, n)
    return a

b =tablica(5)
print(b)