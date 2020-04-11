
class Kwadrat():

    def __init__(self, x=0):
        self.x = x

    def __add__(self, kwadrat):
        return self.x + kwadrat.x

kw1 = Kwadrat(5)
kw2 = Kwadrat(2)
kw3=kw1+kw2
print(kw3)