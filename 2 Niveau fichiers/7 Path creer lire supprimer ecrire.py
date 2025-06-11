from pathlib import Path

# Cr
p = Path.cwd().parent  # E:\PYTHONS\1_FormationPython
# p = p / "DossierTest"
# p.mkdir(parents=True, exist_ok=True)
# p = p / "Fichiers"
# p.mkdir(parents=True, exist_ok=True)
# p = p / "texte.txt"
# p.touch()

# Supprimer un fichier par exemple texte.txt
# p.unlink()

# Supprimer un dossier
p2 = Path(r"E:\PYTHONS\1_FormationPython\DossierTest\Fichiers")
# print(p2.rmdir())  # Video 223

# Ecrire dans un fichier
ecrire = Path(r"E:\PYTHONS\1_FormationPython\DossierTest\Fichiers")
ecrire.mkdir(parents=True, exist_ok=True)
ecrire = ecrire / "textes.txt"
ecrire.touch()
ecrire.write_text("Bonjour")
print(ecrire.read_text())


# scanner un dossier
scanner = Path(r"E:\PYTHONS\1_FormationPython")
for f in scanner.iterdir():
    print(f.name)

images = Path(r"C:\Users\H P\Pictures\Screenshots")
for f in images.glob("*.png"):
    print(f.name)
