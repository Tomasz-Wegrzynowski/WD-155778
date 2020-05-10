import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt


df = pd.read_csv('zamowienia.csv', header=0, sep=';')
dfIlZamSprzed = df.groupby(['Sprzedawca']).agg({'idZamowienia':['count']})
wykres = dfIlZamSprzed.plot.bar()
wykres.set_ylabel('Liczba zamówień')
wykres.set_xlabel('Sprzedający')
plt.show()
print(dfIlZamSprzed)