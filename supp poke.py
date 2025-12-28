def supprimer_poke():
    supp = str(input("Quel pokemon voulait vous-supprimez ?(Inserer le nom)")).strip().capitalize()
    for i in range(len(px)):
        if supp == px[i][1]:
            del(px[i])
            return "Voici le nouveau pokedex", px
    if supp not in px:
        return "Ce pokemon n'est pas dans le pokedex"