import itertools
liczby = [1, 2, 3, 5, 6, 1, 2, 6, 7, 8]
zbior = itertools.combinations(liczby, 3)
for elemen in zbior:
    print(elemen)