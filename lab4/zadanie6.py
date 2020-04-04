class Slowa:

    wyraz1 = ""
    wyraz2 = ""

    #slowa = []

    def wypisz_slowa(self):
        print("Słowo 1: " + self.wyraz1)
        print("Słowo 2: " + self.wyraz2)

    def palindrom(self):
        dlugosc = len(self.wyraz1)
        odwrocony_wyraz = self.wyraz1[dlugosc::-1]
        #print(odwrocony_wyraz)
        if self.wyraz1 == odwrocony_wyraz:
            return True
        if self.wyraz1 != odwrocony_wyraz:
            return False

    def metagram(self):
        if len(self.wyraz1) != len(self.wyraz2):
            return False
        licznik = 0
        liczbaNiezgodnychZnakow = 0
        while licznik < len(self.wyraz1):
            if self.wyraz1[licznik] != self.wyraz2[licznik]:
                liczbaNiezgodnychZnakow = liczbaNiezgodnychZnakow + 1
            licznik = licznik + 1
        if liczbaNiezgodnychZnakow == 1:
            return True
        else:
            return False

    def anagram(self):
        if(sorted(self.wyraz1) == sorted(self.wyraz2)):
            return True
        else:
            return False


slowa = Slowa()

slowa.wyraz1 = "mama"
slowa.wyraz2 = "mata"

slowa.wypisz_slowa()

if(slowa.palindrom() == True):
    print("Palindrom !")
if(slowa.palindrom() ==False):
    print("NIE Palindrom !")

if(slowa.metagram() == True):
    print("Metagram")
else:
    print("Nie Metagram")

if(slowa.anagram() == True):
    print("Anagram")
else:
    print("NIE anagram")


