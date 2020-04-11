class Material:
    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.rodzaj=rodzaj
        self.dlugosc=dlugosc
        self.szerokosc=szerokosc

    def wyswietl_nazwe(self):
        print(self.rodzaj)


class Ubrania(Material):
    def __init__(self, rodzaj, dlugosc, szerokosc, rozmiar, kolor, dla_kogo):
        Material.__init__(self, rodzaj, dlugosc, szerokosc)
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.dla_kogo = dla_kogo

    def wyswietl_dane(self):
        print(self.rodzaj)
        print(self.rozmiar)
        print(self.dla_kogo)
        print(self.kolor)

class Sweter(Ubrania):

    def __init__(self, rodzaj, dlugosc, szerokosc, rozmiar, kolor, dla_kogo, rodzaj_swetra):
        Ubrania.__init__(self, rodzaj, dlugosc, szerokosc, rozmiar, kolor, dla_kogo)
        self.rodzaj_swetra = rodzaj_swetra

    def wyswietl_dane(self):
        print(self.rodzaj)
        print(self.rozmiar)
        print(self.dla_kogo)
        print(self.kolor)
        print(self.rodzaj_swetra)


material = Material("Tkanina", 4, 6)
material.wyswietl_nazwe()

bluzka = Ubrania("Tkanina", 4, 6, "M", "Biały", "Dla dzieci")
bluzka.wyswietl_dane()

kargigan = Sweter("Tkanina", 4, 6, "M", "Biały", "Dla dzieci", "Kargigan")
kargigan.wyswietl_dane()