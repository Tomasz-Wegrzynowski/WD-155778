import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx,'Arkusz1')

dfChlopcy = df[df['Plec'] == 'M']
dfCh = dfChlopcy.groupby('Rok').agg({'Liczba':['sum']})
dfCh.columns = ['Suma chłopców']
dfDziewczynki = df[df['Plec'] == 'K']
dfDz = dfDziewczynki.groupby('Rok').agg({'Liczba':['sum']})
dfDz.columns = ['Suma dziewczynek']

suma_chlopcow = list(dfCh['Suma chłopców'])
suma_dziewczat = list(dfDz['Suma dziewczynek'])


index = np.arange(18)
width = 0.30

plt.bar(index, suma_chlopcow ,width,color='blue')
plt.bar(index, suma_dziewczat, width, color='red', bottom=suma_chlopcow)

years = np.arange(2000, 2018, 1)
plt.xticks(index,years)

plt.show()