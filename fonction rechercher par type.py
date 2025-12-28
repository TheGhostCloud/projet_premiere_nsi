def rechercher_par_type():  
    type_p= str(input("Quel type chercher vous ?" )).strip().capitalize() ## Pour que la chaine de caractère est une maj au début et que des minuscules + enlève les espaces inutiles
    type_recherche = []                                                   ## verif que rechercher_par_type() n'est pas vide
    for i in range(len(px)):
        if type_p == px[i][2] or type_p == px[i][3]:
            type_recherche.append(px[i])
    if type_recherche == []:
        return "Ce type n'est pas dans le pokedex"
    else:
        for o in range(len(type_recherche)):
            print("=================================================================================")
            print("nom du pokémon: ", type_recherche[o][1] ,"\nnuméro: ", type_recherche[o][0], "\nType:",type_recherche[o][2],"Type secondaire: ",type_recherche[o][3] ,"\nPV: ", type_recherche[o][4], "Attaque: ", type_recherche[o][5], " Défense: ", type_recherche[o][6], "Vitesse: ", type_recherche[o][7], "\nGénération: ", type_recherche[o][8])
        return ""