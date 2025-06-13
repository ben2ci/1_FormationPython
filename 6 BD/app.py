import json


fichier = "settings.json"

with open(fichier, "r") as f:
    settings = json.load(f)


print(settings)

settings["fontSize"] = 115
with open(fichier, "w") as f:
    json.dump(settings, f, indent=4)