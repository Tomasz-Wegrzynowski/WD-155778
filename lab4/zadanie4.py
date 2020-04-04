class NaZakupy:

    def __init__(self, nazwa, ilosc, cena, jednostka):
        self.nazwa_produktu = nazwa
        self.ilosc = ilosc
        self.cena_jed = cena
        self.jednostka_miary = jednostka

    def wyswietl_produkt(self):
        print(self.nazwa_produktu)
        print(self.ilosc)
        print(self.cena_jed)
        print(self.jednostka_miary)

    def ile_produktu(self):
        print(str(self.ilosc) +" "+ str(self.jednostka_miary))

    def ile_kosztuje(self):
        return self.cena_jed*self.ilosc

por = NaZakupy("Por", 4, 2.70, "kg")
por.wyswietl_produkt()
por.ile_produktu()
print(por.ile_kosztuje())