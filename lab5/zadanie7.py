class Parzyscie:
    """Iterator zwracający wartości z parzystymi indeksami odwróconym"""
    def __init__(self, data):
        self.data = data
        self.index=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.data):
            raise StopIteration
        wartosc = self.data[self.index]
        self.index = self.index + 2
        return wartosc


tekst = Parzyscie("abcd")
ti = iter(tekst)
print(tekst)
for element in ti:
    print(element)
