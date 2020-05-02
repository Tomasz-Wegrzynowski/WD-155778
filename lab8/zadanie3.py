import pandas as pd
import numpy as np
import xlrd
import openpyxl

df = pd.read_csv('zamowienia.csv', header=0, sep=';')

def a():
    dfNazwiska = df['Sprzedawca'].unique()
    print(dfNazwiska)

def b():
    dfDane = df.sort_values('Utarg',ascending=False)
    print(dfDane['Utarg'].head(5))

def c():
    dfIlZamSprzed = df.groupby(['Sprzedawca']).agg({'idZamowienia':['count']})
    print(dfIlZamSprzed)

def d():
    dfSumZamKraj = df.groupby(['Kraj']).agg({'idZamowienia':['count']})
    print(dfSumZamKraj)

def e():
    start_date = pd.Timestamp(2005,1,1)
    end_date = pd.Timestamp(2005,12,31)
    df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia'])
    dfZam2005 = df[(df['Data zamowienia'] >= start_date) & (df['Data zamowienia'] <= end_date) & (df['Kraj'] == 'Polska')]
    dfSuma = dfZam2005.agg({'idZamowienia':['count']})
    print(dfSuma)

def f():
    start_date = pd.Timestamp(2004,1,1)
    end_date = pd.Timestamp(2004,12,31)
    df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia'])
    dfZam2004 = df[(df['Data zamowienia'] >= start_date) & (df['Data zamowienia'] <= end_date)]
    dfSuma = dfZam2004.agg({'Utarg':['mean']})
    print(dfSuma)

def g():
    start_date_2004 = pd.Timestamp(2004,1,1)
    end_date_2004 = pd.Timestamp(2004,12,31)
    start_date_2005 = pd.Timestamp(2005,1,1)
    end_date_2005 = pd.Timestamp(2005,12,31)
    df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia'])
    dfZam2004 = df[(df['Data zamowienia'] >= start_date_2004) & (df['Data zamowienia'] <= end_date_2004)]
    dfZam2005 = df[(df['Data zamowienia'] >= start_date_2005) & (df['Data zamowienia'] <= end_date_2005)]
    dfZam2004.to_csv('Zamowienia_2004.csv', header=0, sep=';')
    dfZam2005.to_csv('Zamowienia_2005.csv', header=0, sep=';')

# a()
# b()
# c()
# d()
# e()
# f()
# g()