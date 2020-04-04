import random

lista = []
licznik = 0
while licznik < random.randint(1, 10):
    lista.append(random.randint(1,100)*4)
    licznik += 1
plik = open("daneZad1.txt","w")
plik.write(str(lista))
plik.close()
print(lista)
