import random
nad = random.randint(1,100)
print ("Bienvenue dans le jeu")
print("Choisi un nombre entre 1 et 100")
essais = 7
while essais > 0 :
    devinette = int(input("Entrez votre devinette :"))
    if devinette < nad :
        print("Too low")
        essais = essais-1
    elif devinette > nad :
        print ("Too high")
        essais = essais-1
    else:
        print("Good you found.")
        break
else:
    print("You LOSE bahahahaha anis t un rageur ")