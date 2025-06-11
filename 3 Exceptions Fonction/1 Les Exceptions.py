liste = [2, 7, "texte", 4]

# total_erreur = sum(liste)

try:
    total = sum(liste)
except TypeError:
    print("Impossible d'additionner nombre et chaînes de caractères")
