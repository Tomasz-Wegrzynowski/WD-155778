class Samogloski:
    def __init__(self, data):
        if(isinstance(data, str)):
            self.data = data
            self.index = -1
        else:
            print("Nie jest stringiem")

    def __iter__(self):
        return self

    def __next__(self):
        self.index = self.index +1
        if(self.index == len(self.data)):
            raise StopIteration
        if((self.data[self.index] =="e") |
         (self.data[self.index] =="y") |
         (self.data[self.index] =="u") |
         (self.data[self.index] =="i") |
         (self.data[self.index] =="o") |
         (self.data[self.index] =="a")):
            return self.data[self.index]

tekst = Samogloski("abcadyainoedb")
for samogloska in tekst:
    print(samogloska)

