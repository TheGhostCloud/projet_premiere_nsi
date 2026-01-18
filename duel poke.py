import random
def rechercher_par_nom_pratique(): ## 
    nom= str(input("Quel pokemon chercher vous ?")).strip().capitalize()
    for i in range(len(px)):
        if nom == px[i][1]:
            return(px[i])
        
def duel_p():
    duel = []
    print("Pour faire un duel, indiquez nous quels pokemons voulez-vous faire combattre")
    print("Noubliez pas de vérifier AVANT de faire combattre, si les pokemons sont dans le pokedex via le menu 5")
    p1 = rechercher_par_nom_pratique()
    numero1, nom1, type_principale1, type_secondaire1,PV1, attaque1, defense1 ,vitesse1, generation1 = p1
    duel.append(p1)
    p2 = rechercher_par_nom_pratique()
    numero2, nom2, type_principale2, type_secondaire2,PV2, attaque2, defense2 ,vitesse2, generation2 = p2
    duel.append(p2)
    assert nom1 != nom2 , "Faire combattre les mêmes pokemons n'est pas très intelligent/ intéressant ^^ "
    while PV1 >= 0 or PV2 >= 0:
        coup_crit = random.randint(1, 100)
        if coup_crit <= 5:
            cp = True
        else:
            cp = False
        if vitesse1 > vitesse2:
            if cp == True:
                if defense2 > attaque1:
                    PV2 = PV2 - 10
                elif attaque1 > defense2:
                    PV2 = PV2 - ( attaque1 - defense2 )*2
                elif defense1 > attaque2:
                    PV1 = PV1 - 10
                elif attaque2 > defense1:
                    PV1 = PV1 - (attaque2 - defense1 )*2
            else:
                if defense2 > attaque1:
                    PV2 = PV2 - 1
                elif attaque1 > defense2:
                    PV2 = PV2 - ( attaque1 - defense2)
                elif defense1 > attaque2:
                    PV1 = PV1 - 1
                elif attaque2 > defense1:
                    PV1 = PV1 - (attaque2 - defense1 )
        else: 
                if defense1 > attaque2:
                    PV1 = PV1 - 1
                elif attaque2 > defense1:
                    PV1 = PV1 - (attaque2 - defense1)
                elif defense2 > attaque1:
                    PV2 = PV2 - 1
                elif attaque1 > defense2:
                    PV2 = PV2 - (attaque1 - defense2)
        if PV2 <= 0:
            print("Le gagnant est: ", duel[0][1])
            return ""
        elif PV1 <= 0:
            print("Le gagnant est: ", duel[1][1])
            return ""