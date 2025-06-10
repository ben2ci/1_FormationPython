from pprint import pprint

liste = [1, 2, True, 4, "Salut"]
liste.append(3)

tuplet = (1, 2, "Bien")
pprint(liste)
pprint(tuplet)

liste2 = list(tuplet)
liste2.remove("Bien")
print(liste2)