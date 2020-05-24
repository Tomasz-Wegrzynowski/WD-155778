import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random

# Ustawiamy seed by za każdym razem wyglądało identycznie
np.random.seed( 19680801 )


def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin


fig = plt.figure()
ax = fig.add_subplot( 111 , projection = '3d' )
n = 100

markers = ['o','<','^', '>', 'p', '.', ',']
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
i = 0
while i < 5:
    for c, m, zlow, zhigh in [( random.choice(colors) , random.choice(markers) , - 50 , - 25 )]:
        xs = randrange(n, 23 , 32 )
        ys = randrange(n, 0 , 100 )
        zs = randrange(n, zlow, zhigh)
        ax.scatter(xs, ys, zs, c =c, marker =m)
    i=i+1
ax.set_xlabel( 'X Label' )
ax.set_ylabel( 'Y Label' )
ax.set_zlabel( 'Z Label' )
plt.show()