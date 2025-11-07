""" Écrire une fonction qui contient une liste nommée « fruits » qui contient les 
strings pomme, cerise, orange, melon. Cette fonction doit à son appel ajouter 
à la liste « fruits » un string « mangue » à l’index 2. """
fruits = ["pomme", "cerise", "orange"]
def returnlist (fruits) :
    fruits.insert(2, "Mangue")
    print(fruits)

returnlist(fruits)