texte = "La fonction split, transforme du texte en une liste de sous-texte, son inverse est join"

print("texte: ", texte)
print()
print("texte.split(): ", texte.split())
print()
print("' '.join(texte.split()): ", " ".join(texte.split()))
print("'-'.join(texte.split()): ", "-".join(texte.split()))
