print("LES CLASSES METHODES")


class Voiture:
    voiture_cree = 0

    def __init__(self, marque, vitesse, prix):
        Voiture.voiture_cree += 1
        self.marque = marque
        self.vitesse = vitesse
        self.prix = prix

    def __str__(self):
        return f"Voiuture de marque {self.marque}, de vitesse maximale {self.vitesse} t de prix {self.prix}"

    @classmethod
    def lamborghini(cls):
        return cls(marque="Lamborghini", vitesse=250, prix=200000)

    @classmethod
    def porsche(cls):
        return cls(marque="Porsche", vitesse=200, prix=180000)

    @staticmethod
    def afficher_nombre_voitures():
        print(f"Vous avez {Voiture.voiture_cree} voitures dans votre garage")


# lambo = Voiture.lamborghini()
# lambos = Voiture.lamborghini()
# print(lambo.marque)
# porsche = Voiture.porsche()
# print(porsche.prix)
# Voiture.afficher_nombre_voitures()

porscheC = Voiture("Porsche Cayen", 200, 250000)
print("porscheC: ", porscheC)

projets = ["pr_GameOfThrones", "HarryPotter", "pr-Avengers"]


class Utilisateur:
    print()

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def __str__(self):
        return f"Utilisateur {self.nom} {self.prenom}"

    def afficher_projets(self):
        for projet in projets:
            print(projet)


class Junior(Utilisateur):
    def __init__(self, nom, prenom):
        # Utilisateur.__init__(self, nom, prenom)
        super().__init__(nom, prenom)

        # Surcharge

    def afficher_projets(self):
        for projet in projets:
            if not projet.startswith("pr_"):
                print(projet)


print("L'HERITAGE: ")
paul = Junior("Paul", "Durand")
print(paul)
paul.afficher_projets()
