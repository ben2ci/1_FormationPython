chemin = r"E:\PYTHONS\1_FormationPython\data\texte.md"

with open(chemin, "w") as f:  # a est pour ajouter contrairement a w qui écrase la données présentes
    f.write("Bonjour")
