import numpy as np

# Mozliwośći 3x27 27x3 9x9 81x1 1x81
# przez podzielność 81 (liczba kolumn i liczba wierszy musi być całkowita)

a = np.arange(81).reshape(9, 9)
b = a.reshape(3, 27)
print(a)
print(b)


