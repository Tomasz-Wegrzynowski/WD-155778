import numpy as np

def tworz(n):
    x = np.diag([a for a in np.arange(n, 0, -1)])
    return x

print(tworz(5))