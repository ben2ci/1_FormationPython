print("L'INSTRUCTION CONTINUE")

liste = ["1", "4", "25", "Paul", "3", "Pierre"]
for element in liste:
    if element.isdigit():
        continue  # Continue signifie passe
    print(element)


print("L'INSTRUCTION BREAK")
for item in liste:
    if item.isdigit():
        break  # break signifie sortir de la boucle
    print(item)
