from pathlib import Path
import json

dictionnaire = Path(r"E:\PYTHONS\1_FormationPython\data\lire.json")

with open(dictionnaire, "r", encoding="utf-8") as f:
    data = json.load(f)


nouvel_utilisateur = {
    "nom": "Xavier",
    "âge": 42,
    "email": "xavier@example.com",
    "actif": True,
    "adresse": {
        "rue": "45 Avenue des Champs",
        "ville": "Lyon",
        "codePostal": "69001"
    }
}

data.setdefault("utilisateurs", []).append(nouvel_utilisateur)
with open(dictionnaire, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Utilisateur Xavier ajouté avec succès.")
