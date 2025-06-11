from pathlib import Path

print("LA CLASSE PATH")

print(Path.home())
print(Path.cwd())  # Dossier courant

p = Path(r"E:\PYTHONS\1_FormationPython\2 Niveau fichiers")
print(p)
print(p.parent)

# Concatener des chemins
p1 = Path.cwd().parent.parent
p2 = p1 / "Document" / "test.py"
print(p2)

p3 = p1.joinpath("documents", "tests.py")
print(p3)

# Suffix et autres
print(p3.suffix)
print(p3.exists())
print(p3.is_dir())
print(p3.is_file())
print(p3.parts)
print(p3.stem)
