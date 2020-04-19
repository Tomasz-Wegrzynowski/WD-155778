import numpy as np

def ciag(n):
    x, y, z = 0, 1, 0
    for i in range(n):
        if(z == 0):
            z = z + 1
            yield x
        x, y = y, x + y
        yield x

ciag = ciag(24)
a = []
for element in ciag:
    a.append(element)
b = np.array(a)
b.shape = (5,5)
print(b)
