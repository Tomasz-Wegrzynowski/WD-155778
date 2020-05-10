import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt


df = pd.read_csv('zamowienia.csv', header=0, sep=';')
dfIlZamSprzed = df.groupby(['Sprzedawca']).agg({'idZamowienia':['count']})
dfIlZamSprzed.columns = ['Suma zamówień']
explode = (0.2, 0, 0, 0, 0, 0, 0.3, 0, 0)
wykres = dfIlZamSprzed.plot.pie(explode = explode, subplots=True, autopct='%.2f%%', shadow = True)
plt.title("Suma zamówień sprzedwacy")
plt.show()
print(dfIlZamSprzed)