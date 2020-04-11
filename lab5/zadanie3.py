
class Kwadrat():

    def __init__(self, x=0):
        self.x = x

    def __lt__(self, kwadrat):
        return self.x < kwadrat.x

    def __le__(self, kwadrat):
        return self.x <= kwadrat.x

    def __gt__(self, kwadrat):
        return self.x > kwadrat.x

    def __ge__(self, kwadrat):
        return self.x >= kwadrat.x

kw1 = Kwadrat(5)
kw2 = Kwadrat(7)
kw3 = Kwadrat(7)
kw4 = Kwadrat(6)
if(kw1<kw2):
    print("Udało się lt działa")
if(kw3<=kw2):
    print("Udało się le działa")
if(kw3>kw4):
    print("Udało się gt działa")
if(kw2>=kw2):
    print("Udało się ge działa")