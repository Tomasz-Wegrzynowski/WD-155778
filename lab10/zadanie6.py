import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx,'Arkusz1')

#do wykres 1
dfCalyOkres = (df.groupby(['Plec']).agg({'Liczba':['sum']}))
dfCalyOkres.columns = ['Suma narodzin']
#do wykres 2
dfChlopcy = df[df['Plec'] == 'M']
dfCh = dfChlopcy.groupby('Rok').agg({'Liczba':['sum']})
dfCh.columns = ['Suma chłopców']
dfDziewczynki = df[df['Plec'] == 'K']
dfDz = dfDziewczynki.groupby('Rok').agg({'Liczba':['sum']})
dfDz.columns = ['Suma dziewczynek']
#do wykresu 3
dfSum = df.groupby('Rok').agg({'Liczba':['sum']})
dfSum.columns = ['Suma urodzonych dzieci']


x_ticks = np.arange(2000, 2018, 1)
w = dfCalyOkres.plot.bar()
w2 = dfCh.plot()
w3 = dfDz.plot(ax=w2)
plt.xticks(x_ticks)
w4 = dfSum.plot.bar()

plt.show()


