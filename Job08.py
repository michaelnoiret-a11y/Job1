"""Écrire un programme qui calcule la somme de toutes les valeurs paires de la 
liste : L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]. """
fruits = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
def list (fruits) :
    resultatFruit = 0
    for fruit in fruits:
       if fruit % 2 == 0 :
            resultatFruit += fruit
    print(resultatFruit)

list(fruits)