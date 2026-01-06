## pokedex
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
      (21, "Spearow", "Normal", "Vol", 40, 60, 30, 70, 1),
      (22, "Fearow", "Normal", "Vol", 65, 90, 65, 100, 1),
      (23, "Ekans", "Poison", "", 35, 60, 44, 55, 1),
      (24, "Arbok", "Poison", "", 60, 85, 69, 80, 1),
      (25, "Pikachu", "Electrique", "", 35, 55, 40, 90, 1)]
    
def afficher_pokemon()->str:
    """Affiche le pokemon souhaité """
    pokemon = str(input("Quel est le pokemon que vous chercher ?")).strip().capitalize()  # pour ne mettre que des chaine de carac.
    for i in range(len(px)):
        if pokemon == px[i][1]:
            return("nom du pokémon: ", px[i][1] ,"numéro: ", px[i][0], "Type:",px[i][2],"Type secondaire: ",px[i][3] ,"PV: ", px[i][4], "Attaque: ", px[i][5], " Défense: ", px[i][6], "Vitesse: ", px[i][7], "Génération: ", px[i][8])
    if pokemon not in px :
        return "Ce pokemon est absent du pokedex" 

def afficher_tous():
    """Affiche tous les pokemon existant dans le pokedex """
    print("Voici tous les pokémon:") 
    for i in range(len(px)):
        print("nom du pokémon: ", px[i][1] ,"\nnuméro: ", px[i][0], "\nType:",px[i][2],"Type secondaire: ",px[i][3] ,"\nPV: ", px[i][4], "Attaque: ", px[i][5], " Défense: ", px[i][6], "Vitesse: ", px[i][7], "\nGénération: ", px[i][8])
        print("=================================================================================")
        # pas besoin de return parce qu'elle s'arrete apres avoir tous afficher                                                                                     
        
def rechercher_par_numero():
    """Rechercher un pokemon(et toute ses infos) grâce à son numéros """
    numero_poke= int(input("Quel numero porte le pokemon que vous chercher ?" ))
    numero = []
    for o in range (len(px)):        # essaie lste par compréhension ?
        numero.append(px[o][0])                   #collecte tous les num / plus simple pour après gerer les erreurs
    for i in range(len(numero)):
        if numero_poke == numero[i]:
            print("nom du pokémon: ", px[i][1] ,"\nnuméro: ", px[i][0], "\nType:",px[i][2],"Type secondaire: ",px[i][3] ,"\nPV: ", px[i][4], "Attaque: ", px[i][5], " Défense: ", px[i][6], "Vitesse: ", px[i][7], "\nGénération: ", px[i][8])
            print("=================================================================================")
            return ""
    if numero_poke not in numero:
        return("Le numero n'est pas présent dans le pokedex")

def rechercher_par_type():
    """Rechercher les pokemon(et toute leurs infos) grâce à leurs type """
    type_p= str(input("Quel type chercher vous ?" )).strip().capitalize() ## Pour que la chaine de caractère est une maj au début et que des minuscules + enlève les espaces inutiles
    type_recherche = []                                                   
    for i in range(len(px)):
        if type_p == px[i][2] or type_p == px[i][3]:
            type_recherche.append(px[i])
    if type_recherche == []:                                             ## verif que rechercher_par_type() n'est pas vide
        return "Ce type n'est pas dans le pokedex"
    else:
        for o in range(len(type_recherche)):
            print("=================================================================================")
            print("nom du pokémon: ", type_recherche[o][1] ,"\nnuméro: ", type_recherche[o][0], "\nType:",type_recherche[o][2],"Type secondaire: ",type_recherche[o][3] ,"\nPV: ", type_recherche[o][4], "Attaque: ", type_recherche[o][5], " Défense: ", type_recherche[o][6], "Vitesse: ", type_recherche[o][7], "\nGénération: ", type_recherche[o][8])
        return ""

def filtrer_par_pv_min():
    """Trouver des pokemon vec au moins X PV """
    pv_mini = int(input("Quel sont les PV minimun ?"))
    tab_pv_mini= []										## plus simple pour tous les affichez
    assert pv_mini >= 0, " vos PV sont négatif, c' est impossible"
    print('Les pokemon avec avec ', pv_mini ,'PV sont:')
    for i in range(len(px)):
        if pv_mini <= px[i][4]: 
            tab_pv_mini.append(px[i])
    if  tab_pv_mini== []:
        return " Aucun pokemon possède au moins ces PV"
    else:
        tab_pv_mini.sort(key=lambda p: p[4]) 
        for o in range(len(tab_pv_mini)):
            print("nom du pokémon: ", tab_pv_mini[o][1] ,"\nnuméro: ", tab_pv_mini[o][0], "\nType:",tab_pv_mini[o][2],"Type secondaire: ",tab_pv_mini[o][3] ,"\nPV: ", tab_pv_mini[o][4], "Attaque: ", tab_pv_mini[o][5], " Défense: ", tab_pv_mini[o][6], "Vitesse: ", tab_pv_mini[o][7], "\nGénération: ", tab_pv_mini[o][8])
            print("=================================================================================")
        return ""

def rechercher_par_nom():
    nom= str(input("Quel pokemon chercher vous ?")).strip().capitalize()
    for i in range(len(px)):
        if nom == px[i][1]:
            print("nom du pokémon: ", px[i][1] ,"\nnuméro: ", px[i][0], "\nType:",px[i][2],"Type secondaire: ",px[i][3] ,"\nPV: ", px[i][4], "Attaque: ", px[i][5], " Défense: ", px[i][6], "Vitesse: ", px[i][7], "\nGénération: ", px[i][8])
            print("=================================================================================")
            return ""
    if nom not in px:
            return("Ce pokemon n'est pas dans le pokedex ")
        
def pokemon_max_attaque():
    """Rechercher un pokemon(et toute ses infos) grâce à son nom """
    L_attaque= []
    for i in range(len(px)):
        L_attaque.append(px[i][5])
    L_attaque.sort()
    for i in range(len(px)):
        if L_attaque[-1] == px[i][5]:                              
            print("Le(s) pokemon(s) avec la plus grande attaque est/ sont ","\nnom du pokémon: ", px[i][1] ,"\nnuméro: ", px[i][0], "\nType:",px[i][2],"Type secondaire: ",px[i][3] ,"\nPV: ", px[i][4], "Attaque: ", px[i][5], " Défense: ", px[i][6], "Vitesse: ", px[i][7], "\nGénération: ", px[i][8])
            print("=================================================================================")
    return ""

def moyenne_pv()-> float:
    """Fait une moyenne des PV des pokedex """
    somme =0
    for i in range(len(px)):
        somme= somme + px[i][4]
    moyenne= round(somme / len(px),2)
    print( "La moyenne des PV s'eleve à", moyenne)
    return ""



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

def rechercher_par_nom_pratique():
    """Return que le nom du pokemon donc pratique à utiliser dans les autres fonction"""
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
    assert duel[0][1] != duel[1][1] , "Faire combattre les mêmes pokemons n'est pas très intelligent/ intéressant ^^ "
    while PV1 >= 0 or PV2 >= 0:
        if vitesse1 > vitesse2:
                if defense2 > attaque1:
                    PV2 = PV2 - 1
                elif attaque1 > defense2:
                    PV2 = PV2 - ( attaque1 - defense2 )
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

def supprimer_poke():
    supp = str(input("Quel pokemon voulait vous-supprimez ?(Inserer le nom)")).strip().capitalize()
    for i in range(len(px)):
        if supp == px[i][1]:
            del(px[i])
            return "Voici le nouveau pokedex", px
    if supp not in px:
        return "Ce pokemon n'est pas dans le pokedex"

def tri():
    """Tri les pokémon selon certains critère """
    cu = 0
    while cu != 'Stop':
        print("Cette fonctionnalité sert à trier les pokemons present dans le pokedex selon certains critères comme; Nom, type, Pv, Vitesse, Attaque, Defense, Generation, ")
        print("Si voulez arreter le programme inserer dans la console: stop")
        print("Selon quels criteres voulez-vous trier les pokemon du pokedex ?")
        cu = str(input("Comment voulez-vous trier les pokemons ?")).strip().capitalize()      # cu = choix utilisateur
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
                pv_liste.sort(key=lambda p: p[4])
                print("nom du pokémon: ", pv_liste[i][1] ,"\nnuméro: ", pv_liste[i][0], "\nType:",pv_liste[i][2],"Type secondaire: ",pv_liste[i][3] ,"\nPV: ", pv_liste[i][4], "Attaque: ", pv_liste[i][5], " Défense: ", pv_liste[i][6], "Vitesse: ", pv_liste[i][7], "\nGénération: ", pv_liste[i][8])
                print("=========================================================")
        elif cu == 'Defense':
            defense_liste= []
            for i in range(len(px)):
                defense_liste.append(px[i])
            for i in range(len(defense_liste)):
                defense_liste.sort(key=lambda p: p[6]) 
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


choix = 0
while True: 
    print("=== MENU POKEDEX ===")
    print(" 1 - Affichez tous les pokemons")
    print(" 2 - Recherchez les pokemons par numéro")
    print(" 3 - Rechercher les pokemons par type")
    print(" 4 - Filtrer les pokémons par PV minimum")
    print(" 5 - Rechercher par nom")
    print(" 6 - Pokemon avec la plus grande attaque")
    print(" 7 - Moyenne des PV")
    print(" 8 - Ajouter un pokemon")
    print(" 9 - Faire un duel entre pokemon")
    print("10 - Supprimer un pokemon du pokedex")
    print("11 - trier les pokemons selon diverses critères")
    print("12 - Quitter")                           
    choix= int(input("Q'est-ce que vous voulez faire ?"))

    if choix == 1 :
        print(afficher_tous())
    elif choix == 2 :
        print(rechercher_par_numero())
    elif choix == 3 :
        print(rechercher_par_type())
    elif choix == 4 :
        pv_mini =0
        print(filtrer_par_pv_min())
    elif choix == 5:
        print(rechercher_par_nom())
    elif choix == 6:
        print(pokemon_max_attaque())
    elif choix == 7:
        print(moyenne_pv())
    elif choix == 8:
        print(ajouter_pokemon())
    elif choix == 9:
        print(duel_p())
    elif choix == 10:
        print(supprimer_poke())
    elif choix == 11:
        print(tri())
    elif choix == 12:
        break
    else:
        print("Ce choix n'est pas disponible")  

## pour chercher un type secondaire "" on fait mets rien dans la recherche (juste une enter), pour rechercher par type