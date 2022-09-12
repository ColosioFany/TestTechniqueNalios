def Output(): 
    for i in range(1, 100): 
        three = i / 3 
        five = i / 5 

        if type(three) == 'int': 
            if type(five) == 'int': 
                print("FizzBuzz")
            else: 
                print("Fizz")
        else: 
            if type(five) == 'int':
                print("Buzz")
            else: 
                print(i)
 
    
# Bonus 
# Je calcule le nombre d'éléments dans le tableau 
# je fais une boucle qui parcourt chaque clé 
# pour chaque clé je vérifie si le nombre est un multiple de la clé 
# si le nombre est un multiple de la clé, j'affiche le texte correspondant 
# Je boucle pour chaque nombre 