px = [(1, "Bulbizarre", "Plante", "Poison", 45, 49, 49, 45, 1),
      (2, "Ivysaur" , "Plante" , "Poison" , 60, 62, 65, 60, 1),
      (3, "Venusaur", "Plante", "Poison", 80, 82, 83, 80, 1 ),
      (4, "Charmander", "Feu", "", 39, 52, 43, 65, 1),
      (5, "Charmeleon", "Feu", "", 58, 64, 58, 80, 1),
      (6, "Charizard", "Feu", "Vol", 78, 84, 78, 100, 1),
      (7, "Squirtle", "Eau", "", 44, 48, 65, 43, 1),
      (8, "Wartortle", "Eau", "", 59, 63, 80, 58, 1),
      (9, "Blastoise", "Eau", "", 73, 83, 100, 78, 1),
      (10, "Caterpie", "Insecte", "", 45, 30, 35, 45, 1),
      (11, "Metapod", "Insecte", "", 50, 20, 55, 30, 1),
      (12, "Butterfree", "Insecte", "Vol", 60, 45, 50, 70, 1),
      (13, "Weedle", "Insecte", "Poison",40, 35, 30, 30, 1),
      (14, "Kakuna", "Insecte", "Poison", 65, 90, 40, 75, 1),
      (15, "Beedrill", "Insecte", "Poison", 65, 90, 40, 75, 1),
      (16, "Pidgey", "Normal", "Vol", 63, 60, 55, 71, 1),
      (17, "Pidgetto", "Normal", "Vol", 63, 60, 55, 71, 1),
      (18, "Pidgeot", "Normal", "Vol", 83, 80, 75, 101, 1),
      (19, "Rattata", "Normal", "", 30, 56, 35, 72, 1),
      (20, "Raticate", "Normal", "", 55, 81, 60, 97, 1),
      #(26, "Arbok", "Poison", "", 60, 85, 69, 80, 2),		
      (21, "Spearow", "Normal", "Vol", 40, 60, 30, 70, 1),
      (22, "Fearow", "Normal", "Vol", 65, 90, 65, 100, 1),
      (23, "Ekans", "Poison", "", 35, 60, 44, 55, 1),
      (24, "Arbok", "Poison", "", 60, 85, 69, 80, 1),
      (25, "Pikachu", "Electrique", "", 35, 55, 40, 90, 1)]
    
def tri():
    cu = 0
    while cu != 'Stop':
        print("Cette fonctionnalité sert à trier les pokemons present dans le pokedex selon certains critères comme; Nom, type, Pv, Vitesse, Attaque, Defense, Generation, ")
        print("Si voulez arreter le programme inserer dans la console: stop")
        print("Selon quels criteres voulez-vous trier les pokemon du pokedex ?")
        cu = str(input("Comment voulez-vous trier les pokemons ?")).strip().capitalize()	# cu = choix utilisateur
        if cu == 'Stop':
            break
        elif cu == 'Attaque':
            attaque_liste = []
            for i in range(len(px)):
                attaque_liste.append(px[i])
            for i in range(len(attaque_liste)):
                attaque_liste.sort(key=lambda p: p[5]) ## sert à trier grâce à cette indice précis, peut même le faire à l'envers
                print("nom du pokémon: ", attaque_liste[i][1] ,"\nnuméro: ", attaque_liste[i][0], "\nType:",attaque_liste[i][2],"Type secondaire: ",attaque_liste[i][3] ,"\nPV: ", attaque_liste[i][4], "Attaque: ", attaque_liste[i][5], " Défense: ", attaque_liste[i][6], "Vitesse: ", attaque_liste[i][7], "\nGénération: ", attaque_liste[i][8])
                print("=========================================================")
        elif cu == 'Pv':
            pv_liste= []
            for i in range(len(px)):
                pv_liste.append(px[i])
            for i in range(len(pv_liste)):
                pv_liste.sort(key=lambda p: p[4]) ## sert à trier grâce à cette indice précis, peut même le faire à l'envers
                print("nom du pokémon: ", pv_liste[i][1] ,"\nnuméro: ", pv_liste[i][0], "\nType:",pv_liste[i][2],"Type secondaire: ",pv_liste[i][3] ,"\nPV: ", pv_liste[i][4], "Attaque: ", pv_liste[i][5], " Défense: ", pv_liste[i][6], "Vitesse: ", pv_liste[i][7], "\nGénération: ", pv_liste[i][8])
                print("=========================================================")
        elif cu == 'Defense':
            defense_liste= []
            for i in range(len(px)):
                defense_liste.append(px[i])
            for i in range(len(defense_liste)):
                defense_liste.sort(key=lambda p: p[6]) ## sert à trier grâce à cette indice précis, peut même le faire à l'envers
                print("nom du pokémon: ", defense_liste[i][1] ,"\nnuméro: ", defense_liste[i][0], "\nType:",defense_liste[i][2],"Type secondaire: ",defense_liste[i][3] ,"\nPV: ", defense_liste[i][4], "Attaque: ", defense_liste[i][5], " Défense: ", defense_liste[i][6], "Vitesse: ", defense_liste[i][7], "\nGénération: ", defense_liste[i][8])
                print("=========================================================")
        elif cu == 'Vitesse':
            vitesse_liste= []
            for i in range(len(px)):
                vitesse_liste.append(px[i])
            for i in range(len(vitesse_liste)):
                vitesse_liste.sort(key=lambda p: p[7]) 
                print("nom du pokémon: ", vitesse_liste[i][1] ,"\nnuméro: ", vitesse_liste[i][0], "\nType:",vitesse_liste[i][2],"Type secondaire: ",vitesse_liste[i][3] ,"\nPV: ", vitesse_liste[i][4], "Attaque: ", vitesse_liste[i][5], " Défense: ", vitesse_liste[i][6], "Vitesse: ", vitesse_liste[i][7], "\nGénération: ", vitesse_liste[i][8])
                print("=========================================================")
        elif cu == 'Generation':
            gen_liste= []
            for i in range(len(px)):
                gen_liste.append(px[i])
            for i in range(len(gen_liste)):  
                gen_liste.sort(key=lambda p: p[8])
                print("nom du pokémon: ", gen_liste[i][1] ,"\nnuméro: ", gen_liste[i][0], "\nType:",gen_liste[i][2],"Type secondaire: ",gen_liste[i][3] ,"\nPV: ", gen_liste[i][4], "Attaque: ", gen_liste[i][5], " Défense: ", gen_liste[i][6], "Vitesse: ", gen_liste[i][7], "\nGénération: ", gen_liste[i][8])
                print("=========================================================")
        elif cu == 'Type':                            
            px_trie_par_type = sorted(px, key= lambda p: p[2] )
            for i in range(len(px_trie_par_type)):          
                print("nom du pokémon: ", px_trie_par_type[i][1] ,"\nnuméro: ", px_trie_par_type[i][0], "\nType:",px_trie_par_type[i][2],"Type secondaire: ",px_trie_par_type[i][3] ,"\nPV: ", px_trie_par_type[i][4], "Attaque: ", px_trie_par_type[i][5], " Défense: ", px_trie_par_type[i][6], "Vitesse: ", px_trie_par_type[i][7], "\nGénération: ", px_trie_par_type[i][8])
                print("=========================================================")
        elif cu == 'Nom':                            
            px_trie_par_nom = sorted(px, key= lambda p: p[1] )
            for i in range(len(px_trie_par_nom)):          
                print("nom du pokémon: ", px_trie_par_nom[i][1] ,"\nnuméro: ", px_trie_par_nom[i][0], "\nType:",px_trie_par_nom[i][2],"Type secondaire: ",px_trie_par_nom[i][3] ,"\nPV: ", px_trie_par_nom[i][4], "Attaque: ", px_trie_par_nom[i][5], " Défense: ", px_trie_par_nom[i][6], "Vitesse: ", px_trie_par_nom[i][7], "\nGénération: ", px_trie_par_nom[i][8])
                print("=========================================================")
        else:
             print("Attention, tu as peut-etre mal orthographie, il ne faut pas mettre les accents")