def rechercher_par_nom():
    nom= str(input("Quel pokemon chercher vous ?")).strip().capitalize()
    for i in range(len(px)):
        if nom == px[i][1]:
            print("nom du pokémon: ", px[i][1] ,"\nnuméro: ", px[i][0], "\nType:",px[i][2],"Type secondaire: ",px[i][3] ,"\nPV: ", px[i][4], "Attaque: ", px[i][5], " Défense: ", px[i][6], "Vitesse: ", px[i][7], "\nGénération: ", px[i][8])
            print("=================================================================================")
            return ""
    if nom not in px:
            return("Ce pokemon n'est pas dans le pokedex ")