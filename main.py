# Jeu du pendu en français par NoéLeTroubadour

import random
import os
import fonctions_jeu_du_pendu
import msvcrt

os.system("cls")

with open("liste_de_mots.txt") as f:
    liste_de_mots = f.readlines()

mot_secret = random.choice(liste_de_mots).strip()
mot_secret = mot_secret.lower()
mot_secret = list(mot_secret)

mot_en_tirets_du_bas = "-" * len(mot_secret)
mot_en_tirets_du_bas = list(mot_en_tirets_du_bas)

erreures = []

nombre_derreures_restantes = 11

print("\nBIENVENUE DANS LE MEILLEUR JEU DU PENDU AU MONDE\n\nAppuie sur un bouton pour continuer")
msvcrt.getch()

while nombre_derreures_restantes > 0:
    os.system("cls")

    print("\n\n")
    fonctions_jeu_du_pendu.affichage(nombre_derreures_restantes)

    if "-" in mot_en_tirets_du_bas:
        recuperation_des_variables = fonctions_jeu_du_pendu.roll(mot_secret, nombre_derreures_restantes, erreures, mot_en_tirets_du_bas)
        nombre_derreures_restantes = recuperation_des_variables[0]
        erreures = recuperation_des_variables[1]
        mot_en_tirets_du_bas = recuperation_des_variables[2]
        pass
    else:
        os.system("cls")
        
        fonctions_jeu_du_pendu.affichage(nombre_derreures_restantes)

        print(f"\nIl ne te reste que {nombre_derreures_restantes} erreures possibles restantes")
    
        print("\nPour l'instant tu as trouvé tout ça -->        ","".join(mot_en_tirets_du_bas))

        print("\nLes lettres non valides sont : ", ", ".join(erreures))

        print("\n\nBien joué ! Tu as gagné (plus qu'à refaire une partie pour découvrir plus de 500 mots) !\n")
        break
    
if "-" in mot_en_tirets_du_bas:
    os.system("cls")
    fonctions_jeu_du_pendu.affichage(nombre_derreures_restantes)
    print(f"\nLe mot était ","".join(mot_secret))
    print("\n\nBAHAHAHAHA t'es nul bah alors même un nul il dirait 'oh il est nul lui'. Bon aller sauve l'honneur et refais une partie.\n")