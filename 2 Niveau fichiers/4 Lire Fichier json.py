import json

chemin = r"E:\PYTHONS\1_FormationPython\data\lire.json"

with open(chemin, "r") as f:
    liste = json.load(f)
    print(liste)

# with open(chemin, "r") as f:
#     contenu = json.load(f)
#     for cle, valeur in contenu.items():
#         print(cle)
#         for c, v in valeur.items():
#             print(c, v)