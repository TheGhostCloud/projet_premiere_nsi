def afficher_pokemon():
    pokemon = str(input("Quel est le pokemon que vous chercher ?")).strip().capitalize()  # pour ne mettre que des chaine de carac.
    for i in range(len(px)):				# regarder dans tout la liste(= le pokedex)
        if pokemon == px[i][1]:
            return("nom du pokémon: ", px[i][1] ,"numéro: ", px[i][0], "Type:",px[i][2],"Type secondaire: ",px[i][3] ,"PV: ", px[i][4], "Attaque: ", px[i][5], " Défense: ", px[i][6], "Vitesse: ", px[i][7], "Génération: ", px[i][8])
        else:
            return "Ce pokemon est absent du pokedex" 

def afficher_tous():
    print("Voici tous les pokémon:") 
    for i in range(len(px)):
        print("nom du pokémon: ", px[i][1] ,"\nnuméro: ", px[i][0], "\nType:",px[i][2],"Type secondaire: ",px[i][3] ,"\nPV: ", px[i][4], "Attaque: ", px[i][5], " Défense: ", px[i][6], "Vitesse: ", px[i][7], "\nGénération: ", px[i][8])
        print("=================================================================================")
        # pas besoin de return parce qu'elle s'arrete apres avoir tous afficher 