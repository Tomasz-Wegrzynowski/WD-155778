import numpy as np

def dzienie(mat, k):
    dl_w = np.size(mat, 0)
    dl_k = np.size(mat, 1)
    if k == 0:
        if(dl_w%2!=0):
            print("Ilość wierszy nie pozwala na operacje")
        else:
            a = int(dl_w/2)
            gora = mat[0:a,:]
            dol = mat[a:,:]
            print(gora)
            print(dol)
    if k == 1:
        if(dl_k%2!=0):
            print("Ilość kolumn nie pozwala na operacje")
        else:
            a = int(dl_k/2)
            lewa = mat[:,0:a]
            prawa = mat[:,a:]
            print(lewa)
            print(prawa)

mat = np.arange(20)
mat = mat.reshape((5,4))
dzienie(mat,0)
dzienie(mat,1)