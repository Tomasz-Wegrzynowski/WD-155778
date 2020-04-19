import numpy as np

def macierz(m):
    i = 1
    mat = np.diag([2 for a in range(m)])
    while i < m:
        mat_1 = np.diag([2+2*i for a in range(m - i)], i)
        mat_2 = np.diag([2+2*i for a in range(m - i)], -i)
        mat = mat + mat_1 + mat_2
        i=i+1
    return mat


print(macierz(5))
