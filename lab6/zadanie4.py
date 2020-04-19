import numpy as np

def generuj(a,b):
    return np.logspace(1,b,b,True,base=a,dtype=int)

print(generuj(2,10))