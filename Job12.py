L = [7, 11, 42, 39, 2]
def ordreCroissant(L):
    for nombre in L:
        if L[0] > L[1]:
            L[1], L[0] = L[0], L[1]
    print(L)

ordreCroissant(L)