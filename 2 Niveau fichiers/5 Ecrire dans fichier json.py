import json

chemin = r"E:\PYTHONS\1_FormationPython\data\ecrire.json"

# On récupère les données dans une liste
with open(chemin, "r") as f:
    donnees = json.load(f)
    print(donnees)

# On ajoute une données à cette liste et on réecrit dans le fichier json
donnees.append(4)

with open(chemin, "w") as f:
    json.dump(donnees, f, indent=4)


