import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl
from random import *

def rzut(n):
    i=0
    a =[]
    while i < n:
        x = randint(1, 6)
        y = randint(1, 6)
        a.append(x+y)
        i=i+1
    return a
x = (rzut(100))

plt.hist(x, bins=11, facecolor='g', alpha=0.75, density=True)


plt.xlabel('Wartości')
plt.ylabel('Prawdopodobieństwo')
plt.title('Histogram')
plt.grid(True)
plt.show()