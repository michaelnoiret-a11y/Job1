""" Écrire un programme qui compte le nombre de multiples de 3 présents dans 
la liste : L = [8, 24,48,2,16]. """
fruits = [8, 24, 48, 2, 16]
def returnlist (fruits) :
    for fruit in fruits:
       if fruit % 3 == 0 :
        print(fruit)

returnlist(fruits)