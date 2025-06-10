print("LES FONCTIONS 'strip', 'replace, count")

texte = "Bonjour ceci est un bonjour"

print(texte.lower().replace("jour", "soir"))
print(texte.lower().replace(" ", "").replace("jour", "soir"))

espace = "      Salut à tous ! "
print(espace)
print(espace.strip(" "))
enlever = "enlever"
print(enlever)
e = enlever.strip(" len")
print(e)

anticonstitutionnel = "anticonstitutionnel"
print(anticonstitutionnel.count("consti"))  # Ici rien ne sera enlevé
nobreOccurentce = anticonstitutionnel.count("consti")
print(anticonstitutionnel.replace("consti", "", nobreOccurentce))
