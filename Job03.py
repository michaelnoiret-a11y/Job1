""" Écrire une fonction qui contient une liste nommée « fruits » qui contient les 
strings « pomme », « cerise », « orange ». Cette fonction doit à son appel 
ajouter à la liste « fruits » un String « Melon » à la fin de cette liste. """
fruits = ["pomme", "cerise", "orange"]
def returnlist (fruits) :
    fruits.append("Melon")
    print(fruits)

returnlist(fruits)