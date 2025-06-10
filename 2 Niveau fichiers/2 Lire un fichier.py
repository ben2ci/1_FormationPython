chemin = r"E:\PYTHONS\1_FormationPython\README.md"

with open(chemin, "r", encoding='utf-8') as f:
    contenu = repr(f.read())
    print(contenu)
