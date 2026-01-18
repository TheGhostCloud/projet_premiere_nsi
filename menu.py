choix = 0
while True:
    try:
        print("=== MENU POKEDEX ===")
        print("Veuillez mettre le numéros de la fonctionnalité souhtée")
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
        print("11 - trier les pokemons")
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
    except  ValueError:
        print("Vous n'avez pas compris ce que vous devrirez me donner comme information :/")