"""Écrire un programme qui calcule le produit de toutes les valeurs de la liste 
comprises dans l’intervalle [25, 90]. 
L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91] """
nombres = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
def produit_liste (nombres) :
    produitListe = 1
    for nombre in nombres:
        if 25 <= nombre <= 90:
            produitListe *= nombre
    print("Le produit des valeurs comprises entre 25 et 90 est :", produitListe)

produit_liste(nombres)