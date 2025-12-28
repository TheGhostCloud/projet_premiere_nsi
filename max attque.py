def pokemon_max_attaque():
    L_attaque= []
    for i in range(len(px)):
        L_attaque.append(px[i][5])
    L_attaque.sort()
    for i in range(len(px)):
        if L_attaque[-1] == px[i][5]:				#opti avec la fonction maxi(tab) ?
            print("Le(s) pokemon(s) avec la plus grande attaque est/ sont ","\nnom du pokémon: ", px[i][1] ,"\nnuméro: ", px[i][0], "\nType:",px[i][2],"Type secondaire: ",px[i][3] ,"\nPV: ", px[i][4], "Attaque: ", px[i][5], " Défense: ", px[i][6], "Vitesse: ", px[i][7], "\nGénération: ", px[i][8])
            print("=================================================================================")
    return ""