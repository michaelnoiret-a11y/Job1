""" Écrire un programme qui échange les valeurs de la première et de la 
dernière case d’une liste quelconque non vide. """
fruits = [1, 2, 3, 4, 5]
def returnlist (fruits) :
    #fruits.insert(1,4)
    #fruits.insert(4,1)
    fruits[4], fruits[0] = fruits[0], fruits[4]
    print(fruits)

returnlist(fruits)