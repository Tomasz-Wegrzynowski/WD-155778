import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt

df = pd.read_csv('iris.data', header=None, sep=',')

df.columns = ['Sepal length', 'Sepal width','Petal lenght','Petal width', 'Class']
dfSetosa = df[df['Class']=='Iris-setosa']
dfVersicolor = df[df['Class']=='Iris-versicolor']
dfVirginica = df[df['Class']=='Iris-virginica']


w1 = dfSetosa.plot(kind = 'scatter', x='Sepal length', y='Sepal width', color = 'Red', label='Setosa')
w2 = dfVersicolor.plot(kind = 'scatter', x='Sepal length', y='Sepal width', color = 'DarkBlue', label='Versicolor', ax=w1)
dfVirginica.plot(kind = 'scatter', x='Sepal length', y='Sepal width', color = 'Green', label='Virginica', ax=w2)
plt.show()