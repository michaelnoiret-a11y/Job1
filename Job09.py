"""Écrire un programme qui récupère la valeur, maximum et le minimum des 
éléments de la liste : L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]. """
nombres = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
def max_min_liste (nombres) :
    maxnombres = nombres[0]
    minnombres = nombres[0]
    for nombre in nombres:
        #print(max(L),min(L))
        if nombre > maxnombres :
            maxnombres = nombre
            if nombre < minnombres :
                minnombres = nombre
                
    print("Valeur max:", maxnombres,"Valeur min:", minnombres)            

max_min_liste(nombres)