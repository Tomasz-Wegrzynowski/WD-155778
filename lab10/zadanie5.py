import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt
import math

df = pd.read_csv('iris.data', header=None, sep=',')

df.columns = ['Sepal length', 'Sepal width','Petal lenght','Petal width', 'Class']

c = np.random.randint(0, 50, 150)
a = df['Sepal length']
b = df['Sepal width']
g = np.abs(a-b)

plt.scatter('Sepal length','Sepal width',s=g,c=c,data=df)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.show()