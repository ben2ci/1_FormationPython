def afficher_personne(**kwargs):
    for cle, valeur in kwargs.items():
        print(f"{cle}: {valeur}")


afficher_personne(nom="Mael", age=28, email="mael@gmail.com", sexe="Masculin")

from typing import List, Dict, Tuple

notes: List[int] = [2, 7, "e", 78]
print(notes)
