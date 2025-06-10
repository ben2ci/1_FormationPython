liste = ["Utilisateur_01", "Utilisateur_02", "Utilisateur_03", "Utilisateur_04", "Utilisateur_05", "Utilisateur_06"]
print("LISTE: ", liste)
print("[1:3]: ", liste[1:3])
print("[2:]: ", liste[2:])
print("[:2]: : ", liste[:2])
print("[:-1]: ", liste[:-1])
print("[:-3]: ", liste[:-3])
print("[::2]: ", liste[::2])
print("[-1]: ", liste[-1])
# 07 97 52 58 62


employees = ["Carlos", "Max", "Martine", "Patrick", "Alex", "Max"]
resultat1 = employees.index("Max")
resultat2 = employees.count("Max")
print(resultat1)
print(resultat2)

liste_triee = sorted(employees)
# employees.sort() retourne rien mais fait le trie directement
print(liste_triee)
liste_triee.reverse()  # retourne rien mais trie inversement le trie directement
print(liste_triee)

# Supprimer un element de la liste
employe = liste_triee.pop(-1)  # Enlève le dernier
print(employe)
employees.clear()  # Vide la liste
