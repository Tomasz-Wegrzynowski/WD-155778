import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx,'Arkusz1')
dfSum = df.groupby('Plec').agg({'Liczba':['sum']})
wykres = dfSum.plot.bar()
wykres.set_ylabel('Liczba imion (tyś)')
wykres.set_xlabel('Płeć')
plt.title('Liczba urodzonych chłopców i dziewczynek')
plt.show()