import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random


np.random.seed(19680801)

def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot( 121 , projection = '3d' )
ax2 = fig.add_subplot(122, projection = '3d' )
n =20
z = np.linspace( 0 , 2 * np.pi, 5 )
x = np.sin(z)*np.cos(z)
y = np.tan(z)
ax2.plot(x, y, z, label = 'zadanie 1' )
for m, c, zlow, zhigh in [('o','r', -50, -25)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c=c, marker=m)

ax.set_xlabel( 'X Label' )
ax.set_ylabel( 'Y Label' )
ax.set_zlabel( 'Z Label' )
plt.show()

