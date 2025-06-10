print("CHERCHER A L'INTERIEUR d'UNE LISTE")

prenoms = ["PACOME", "CONSTY", "BORIS", "AHO", "DIARRASSOUBA"]

for prenom in prenoms:
    if prenom == "BORIS":
        print("BORIS a été trouvé")
        break  # Dès qu'il trouve BORIS il sort de la boucle
else:
    print("BORIS est introuvable")
