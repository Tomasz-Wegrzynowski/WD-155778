import sys

class ciagArytmetyczny:

    pierszy_wyraz = 0
    roznica = 0
    liczba_wyrazow = 0
    elementy_ciagu = []

    def wyswietl_elementy(self):
        for element in self.elementy_ciagu:
            print(element)

    def pobierz_elementy(self):
        x = 0
        while x < self.liczba_wyrazow:
            self.elementy_ciagu.append(sys.stdin.readline())
            x = x + 1

    def pobierz_parametry(self, pierwszy_wyraz, liczba_wyrazow, roznica):
        self.pierszy_wyraz = pierwszy_wyraz
        self.liczba_wyrazow = liczba_wyrazow
        self.roznica = roznica


    def policz_elementy(self):
        return len(self.elementy_ciagu)

    def suma_elementow(self):
        suma = 0
        for element in self.elementy_ciagu:
            suma = suma + int(element)
        return suma


cA = ciagArytmetyczny()
cA.pobierz_parametry(1,5,3)
cA.pobierz_elementy()
print(cA.policz_elementy())
print(cA.suma_elementow())
