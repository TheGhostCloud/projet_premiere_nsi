def rechercher_par_numero():
    numero_poke= int(input("Quel numero porte le pokemon que vous chercher ?" ))
    numero = []
    for o in range (len(px)):
        numero.append(px[o][0])								#collecte tous les num / plus simple pour après gerer les erreurs
    for i in range(len(numero)):
        if numero_poke == numero[i]:
            print("nom du pokémon: ", px[i][1] ,"\nnuméro: ", px[i][0], "\nType:",px[i][2],"Type secondaire: ",px[i][3] ,"\nPV: ", px[i][4], "Attaque: ", px[i][5], " Défense: ", px[i][6], "Vitesse: ", px[i][7], "\nGénération: ", px[i][8])
            print("=================================================================================")
            return ""
    if numero_poke not in numero:
        return("Le numero n'est pas présent dans le pokedex")