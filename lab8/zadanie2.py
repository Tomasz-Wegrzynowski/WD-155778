import pandas as pd
import numpy as np
import xlrd
import openpyxl

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx,'Arkusz1')


def a():
    dfSumaImionRok = df.groupby('Rok').agg(liczba_imion=pd.NamedAgg(column='Imie', aggfunc='count'))
    dfFinal = dfSumaImionRok[dfSumaImionRok.liczba_imion > 1000]
    print(dfFinal)
def b():
    print(df[df['Imie'] == "TOMASZ"])
def c():
    print(df.agg({'Liczba':['sum']}))
def d():
    print(df[(df['Rok'] >= 2000) & (df['Rok'] <= 2005)].agg({'Liczba':['sum']}))
def e():
    print(df.groupby(['Plec']).agg({'Liczba':['sum']}))
def g():
    dfChlopcy = df[df['Plec'] == 'M']
    dfPopularChlopcy = dfChlopcy.groupby('Imie').agg(liczba_imion=pd.NamedAgg(column='Liczba', aggfunc='sum'))
    dfDaneChlopcow = dfPopularChlopcy.sort_values(['liczba_imion'], ascending=False)

    dfDziewczynki = df[df['Plec'] == 'K']
    dfPopularDziewczynki = dfDziewczynki.groupby('Imie').agg(liczba_imion=pd.NamedAgg(column='Liczba', aggfunc='sum'))
    dfDaneDziewczynek = dfPopularDziewczynki.sort_values(['liczba_imion'], ascending=False)

    print(dfDaneChlopcow.head(1))
    print(dfDaneDziewczynek.head(1))
    

# a()
# b()
# c()
# d()
# e()
# g()