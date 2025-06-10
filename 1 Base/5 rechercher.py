texte = "Tout ceci est très claire. Ceci est un texte à lire"

print("Trouver e", texte.find("e"))
print("Trouver se", texte.find("se"))

if texte.find("e") != -1:
    print(f"la lettre 'e' existe")
else:
    print(f"la lettre 'e' n'xiste pas")


if texte.find("se") != -1:
    print(f"la lettre 'se' n'existe")
else:
    print(f"la lettre 'se' n'existe pas")

# CHERCHER UNE CHAINE DE CARACTERE
image = "image.png"
print(image.endswith(".png"))
print(image.startswith(".png"))
