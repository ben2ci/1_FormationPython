import os

chemin = r"D:\Python\1_FormationPython"
dossier1 = os.path.join(chemin, "dossier1")
dossier2 = os.path.join(chemin, "dossier2", "test")
dossier3 = os.path.join(chemin, "dossier3", "test3")
if not os.path.exists(dossier1):
    os.mkdir(dossier1)  # Pour crée un dossier

if not os.path.exists(dossier2):
    os.makedirs(dossier2)  # Pour crée plusieurs dossiers

os.makedirs(dossier3, exist_ok=True)

if os.path.exists(dossier3):
    os.removedirs(dossier3)

# Module dir
import random

# print(dir(random))
# help(random.uniform(1, 20))
help(random.randint)

# Module pprint
from pprint import pprint

pprint(dir(random))
