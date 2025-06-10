print("COMPREHENSION DE LISTE PREMET D'ITERER SUR UNE LISTE ET")
print(" DE FILTRER LES ELEMENTS TOUT CA SUR UNE SEULE LIGNE")

prenoms = ["PACOME", "2", "CONSTY", "BORIS", "6", "AHO", "DIARRASSOUBA", "25"]

# Le for traditionnel retourne chaque element
for agent in prenoms:
    if agent.isdigit():
        print(agent)


# La comprehension de liste retourne une liste
liste = [element for element in prenoms if element.isdigit()]
print("Compréhesion de liste")
print(liste)
