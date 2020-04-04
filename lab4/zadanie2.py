plik = open("daneZad1.txt","r")
liczby = plik.read() # liczby stają się stringiem, gdyby było readline to były by listą
plik.close()
print(liczby) # Moja uwaga: liczby to string, tylko wyświetlam