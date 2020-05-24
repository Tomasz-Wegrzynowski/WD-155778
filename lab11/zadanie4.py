import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random


def prawdaFalsz():
    a = random.randint(0, 1)
    if a==0:
        return False
    return True

colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
fig = plt.figure( figsize =( 8 , 8 ))
ax1 = fig.add_subplot( 321 , projection = '3d' )
ax2 = fig.add_subplot( 322 , projection = '3d' )
ax3 = fig.add_subplot( 323 , projection = '3d' )
ax4 = fig.add_subplot( 324 , projection = '3d' )
ax5 = fig.add_subplot( 325 , projection = '3d' )

_x = np.arange( 4 )
_y = np.arange( 5 )
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
top = x + y
bottom = np.zeros_like(top)
width = depth = 1
ax1.bar3d(x, y, bottom, width, depth, top, color = random.choice(colors), shade = prawdaFalsz() )
ax2.bar3d(x, y, bottom, width, depth, top, color = random.choice(colors), shade = prawdaFalsz() )
ax3.bar3d(x, y, bottom, width, depth, top, color = random.choice(colors), shade = prawdaFalsz() )
ax4.bar3d(x, y, bottom, width, depth, top, color = random.choice(colors), shade = prawdaFalsz() )
ax5.bar3d(x, y, bottom, width, depth, top, color = random.choice(colors), shade = prawdaFalsz() )

plt.show()