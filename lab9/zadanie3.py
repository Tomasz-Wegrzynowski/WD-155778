import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx,'Arkusz1')
dfPo = df[(df['Rok'] >= 2013)]
print(dfPo)
dfSum = dfPo.groupby('Plec').agg({'Liczba':['sum']})
wykres = dfSum.plot.pie(subplots=True, autopct='%.2f%%')
plt.title('Ilość urodzonych chłopców i dziewczynek w latach 2013-2017')
plt.show()