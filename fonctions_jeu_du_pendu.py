def roll(mot_secret, nombre_derreures_restantes, erreures, mot_en_tirets_du_bas):
    
    print(f"\nIl ne te reste que {nombre_derreures_restantes} erreures possibles restantes")
    
    print("\nPour l'instant tu as trouvé tout ça -->        ","".join(mot_en_tirets_du_bas))

    print("\nLes lettres non valides sont : ", ", ".join(erreures))
    
    essai = input("\nEssaie une lettre\n> ")

    while len(essai) != 1:
        print("\nHummm. Réessaye stp...")
        essai = input("\nEssaye une lettre\n> ")

    while not essai.isalpha():
        print("\nHummm. Réessaye stp...")
        attempt = input("\nEssaye une lettre\n> ")

    if essai in mot_secret:
        for i in range(len(mot_secret)):
            if mot_secret[i] == essai:
                mot_en_tirets_du_bas[i] = essai

    else:
            nombre_derreures_restantes -= 1
            erreures.append(essai)

    return nombre_derreures_restantes, erreures, mot_en_tirets_du_bas

def affichage(nombre_derreures_restantes):
    if nombre_derreures_restantes == 11:
        print("")
    elif nombre_derreures_restantes == 10:
        print("__")
    elif nombre_derreures_restantes == 9:
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("_|_")
    elif nombre_derreures_restantes == 8:
        print("  ______")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("_|_")
    elif nombre_derreures_restantes == 7:
        print("  ______")
        print(" |/")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("_|_")
    elif nombre_derreures_restantes == 6:
        print("  ______")
        print(" |/    |")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("_|_")
    elif nombre_derreures_restantes == 5:
        print("  ______")
        print(" |/    |")
        print(" |     O")
        print(" |")
        print(" |")
        print(" |")
        print("_|_")
    elif nombre_derreures_restantes == 4:
        print("  ______")
        print(" |/    |")
        print(" |     O")
        print(" |     |")
        print(" |")
        print(" |")
        print("_|_")
    elif nombre_derreures_restantes == 3:
        print("  ______")
        print(" |/    |")
        print(" |     O")
        print(" |    -|")
        print(" |")
        print(" |")
        print("_|_")
    elif nombre_derreures_restantes == 2:
        print("  ______")
        print(" |/    |")
        print(" |     O")
        print(" |    -|-")
        print(" |")
        print(" |")
        print("_|_")
    elif nombre_derreures_restantes == 1:
        print("  ______")
        print(" |/    |")
        print(" |     O")
        print(" |    -|-")
        print(" |    / ")
        print(" |")
        print("_|_")
    elif nombre_derreures_restantes == 0:
        print("  ______")
        print(" |/    |")
        print(" |     O")
        print(" |    -|-")
        print(" |    / \\")
        print(" |")
        print("_|_")
    return