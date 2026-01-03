def filtrer_par_pv_min():
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