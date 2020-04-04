class Robaczek:

    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def w_gore(self, liczba_krokow):
        self.y = self.y + self.krok * liczba_krokow

    def w_dol(self, liczba_krokow):
        self.y = self.y - self.krok * liczba_krokow

    def w_lewo(self, liczba_krokow):
        self.x = self.x - self.krok * liczba_krokow

    def w_prawo(self, liczba_krokow):
        self.x = self.x + self.krok * liczba_krokow

    def pokaz_gdzie_jestes(self):
        print("Aktualne współrzędne robaczka:\nX: " + str(self.x) + "\nY: " + str(self.y))

    def __del__(self):
        print("Obiekt został usunięty!")



robaczek = Robaczek(0,0,2)

robaczek.pokaz_gdzie_jestes()

robaczek.w_gore(10)
robaczek.w_prawo(9)
robaczek.w_dol(5)
robaczek.w_lewo(3)

robaczek.pokaz_gdzie_jestes()

del robaczek