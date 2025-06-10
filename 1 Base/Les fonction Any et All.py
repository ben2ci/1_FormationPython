files = ""
f = ""
print("VERIFIER SI TOUS LES FICHIER SE TERMINE PAR .JPG")
valeur = all([f.endswith(".jpg") for f in files])
print(valeur)


notes = [12, 14, 20, 10, 8]
reponse = any([note > 18 for note in notes])
print(notes)
print("Est-ce qu'il y'a au moins un élève qui a 18/20")
if reponse:
    print("Oui")
else:
    print("Non")
