import numpy as np

macierz = np.chararray((8,8),unicode = 'U1')

#wyraz 'FLET' w wierszu pisany wspak
flet = "FLET"
wyraz1 = np.array(list(flet), dtype='U1')
wyraz1 = np.flip(wyraz1)
w1 = 0
for element in wyraz1:
    # print(element)
    macierz[0,w1] = element
    w1 = w1 + 1

#wyraz 'PUZON' w kolumnie
puzon = "PUZON"
wyraz2 = np.array(list(puzon), dtype='U1')
w2 = 2
for element in wyraz2:
    macierz[w2,0] = element
    w2 = w2 + 1

#wyraz 'GITARA' pisany po ukosie
gitara = "GITARA"
wyraz3 = np.array(list(gitara), dtype='U1')
w3 = 2
for element in wyraz3:
    macierz[w3,w3] = element
    w3 = w3 + 1
print(macierz)