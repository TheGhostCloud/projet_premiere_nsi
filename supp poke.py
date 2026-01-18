def supprimer_poke():
    supp = str(input("Quel pokemon voulait vous-supprimez ?(Inserer le nom)")).strip().capitalize()
    for i in range(len(px)):
        if supp == px[i][1]:
            del(px[i])
    for i in range(len(px)):
        print("nom du pokémon: ", px[i][1] ,"\nnuméro: ", px[i][0], "\nType:",px[i][2],"Type secondaire: ",px[i][3] ,"\nPV: ", px[i][4], "Attaque: ", px[i][5], " Défense: ", px[i][6], "Vitesse: ", px[i][7], "\nGénération: ", px[i][8])
        print("=================================================================================")
    return ""
    if supp not in px:
        return "Ce pokemon n'est pas dans le pokedex"