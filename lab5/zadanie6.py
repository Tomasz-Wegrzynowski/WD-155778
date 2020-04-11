class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

tekst = Wspak("abcd")
for element in tekst:
    print(element)

lista = Wspak([1, 2, 3, 4, 6])
for li in lista:
    print(li)

# slownik = Wspak({"jeden" : 1, "dwa" : 2})  #Nie działa dobrze z Słownikiem
slownik = {"jeden" : 1, "dwa" : 2}
for element in slownik:
    print(element, slownik[element])

