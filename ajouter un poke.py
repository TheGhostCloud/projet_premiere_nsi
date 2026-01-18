def ajouter_pokemon():
    """Ajoute un pokémon """
    nouv_p= []
    numero= int(input("Quel esl sont numero ?"))
    nouv_p.append(numero)
    nom = str(input("Quel est son nom ?")).strip().capitalize()
    nouv_p.append(nom)
    type_p= str(input("Quel est son type pricipale ?")).strip().capitalize()
    nouv_p.append(type_p)
    type_s= str(input("Quel est son type secondaire (laissez vide s'il n'en a pas ?")).strip().capitalize()
    nouv_p.append(type_s)
    PV = int(input("Combien le pokemon a de PV ?"))
    nouv_p.append(PV)
    attaque= int(input("Quel est son attaque ?"))
    nouv_p.append(attaque)
    defense= int(input("Quelle est sa defense ?"))
    nouv_p.append(defense)
    vitesse = int(input("Quelle est sa vitesse ?"))
    nouv_p.append(vitesse)
    G = int(input("Quelle est sa generation ?"))
    nouv_p.append(G)
    nouv_poke=tuple(nouv_p)
    for i in range(len(px)):
        if nouv_poke == px[i]:
            return "Ce pokemon est déja dans le pokedex"
        else:
            px.append(nouv_p)
            print("Votre pokemon a bien été ajouté"),print("nom du pokémon: ", px[-1][1] ,"\nnuméro: ", px[-1][0], "\nType:",px[-1][2],"Type secondaire: ",px[-1][3] ,"\nPV: ", px[-1][4], "Attaque: ", px[-1][5], " Défense: ", px[-1][6], "Vitesse: ", px[-1][7], "\nGénération: ", px[-1][8])
            print("=================================================================================")
            return ""