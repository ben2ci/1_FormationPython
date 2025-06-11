from pathlib import Path
import json

dictionnaire = Path(r"E:\PYTHONS\1_FormationPython\data\lire.json")

with open(dictionnaire, "r", encoding="utf-8") as f:
    data = json.load(f)
    print(data.keys())  # Affiche les clefs
    for utilisateur in data["utilisateurs"]:
        print(utilisateur["nom"], utilisateur["email"])

    for commande in data["commandes"]:
        print(commande["id"], commande["produit"], commande["quantité"], commande["prix"])

    for metadonnee in data["métadonnées"].values():
        print(metadonnee)

    # Utilisation de get()
    trouve = False
    for user in data.get("utilisateurs", []):
        if user.get("nom") == "Idriss1":
            print("Utilisateur trouvé")
            trouve = True
            break

    if not trouve:
        print("Utilisateur non trouvé")