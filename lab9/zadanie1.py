import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx,'Arkusz1')
dfSum = df.groupby('Rok').agg({'Liczba':['sum']})
wykres = dfSum.plot.line()
wykres.set_ylabel('Liczba imion')
wykres.set_xlabel('Rok')
plt.title('Liczba urodzonych dzieci dla każdego roku')
x_ticks = np.arange(2000, 2018, 1)
plt.xticks(x_ticks)
plt.show()
