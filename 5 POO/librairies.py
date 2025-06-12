# -*- coding: utf-8 -*-
import json
import logging

from constants import DATA_DIR

LOGGER = logging.getLogger()


class Liste(list):
    def __init__(self, nom):
        super().__init__()
        self.nom = nom

    def ajouter(self, element):
        if not isinstance(element, str):
            raise ValueError("Vous ne pouvez ajouter que des chînes de caractères")

        if element in self:
            LOGGER.error(f"{element} est déjà dans la liste.")
            return False

        self.append(element)
        return True

    def enlever(self, element):
        if element in self:
            self.remove(element)
        # raise ValueError(f"{element} n'est pas dans la liste")
        return False

    def afficher(self):
        i = 1
        print(f"Ma liste de {self.nom}:")
        for element in self:
            print(f"{i}- {element}")
            i += 1

    def sauvegarde(self):
        chemin = DATA_DIR / f"{self.nom}.json"
        if not DATA_DIR.exists():
            DATA_DIR.mkdir()

        with open(chemin, "w", encoding="utf-8") as f:
            json.dump(self, f, indent=4)

        return True


# maListe.ajouter("5")
# maListe.ajouter("6")
# maListe.remove("51")
if __name__ == "__main__":
    liste = Liste("Courses")
    # liste.ajouter(5)
    liste.ajouter("Pommes")
    liste.ajouter("Poires")
    liste.ajouter("Bananes")
    # liste.enlever("Bananes")
    liste.afficher()
    liste.sauvegarde()
