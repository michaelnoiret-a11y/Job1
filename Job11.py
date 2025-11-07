"""Écrire un programme qui crée la liste d’entiers L = [7, 11, 42, 39, 2], votre 
programme devra pouvoir modifier la liste en augmentant de 1 la valeur de 
chaque élément de la liste. """
L = [7, 11, 42, 39, 2]
"""i = 0"""
def listeEntier(L):
    for nombre in L:
        nombre += 1
        print( nombre , end=" ")
    """for nombre in L[:]:
        L[nombre] = nombre + 1
        i += 1
        
print("Nouvelle liste :", L) 
        for i, nombre in enumerate(L):
            L[i] = nombre + 1 
        print("Nouvelle liste :", L)    
        
        L = [7, 11, 42, 39, 2]
L = [valeur + 1 for valeur in L]
print("Nouvelle liste :", L)

L = [7, 11, 42, 39, 2]

for i in range(len(L)):
    L[i] += 1  # on ajoute 1 à chaque élément

print("Nouvelle liste :", L)"""

listeEntier(L)    