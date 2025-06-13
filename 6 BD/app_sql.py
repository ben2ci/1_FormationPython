import sqlite3

connx = sqlite3.connect("database.db")

c = connx.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS employees(
    prenom texte,
    nom text,
    salaire float 
)
""")

# d = {"prenom": "Ives", "nom": "GNAO", "salaire": 475000}
# c.execute("INSERT INTO employees VALUES (:prenom, :nom, :salaire)", d)

# e = {"prenom": "Adam"}
# c.execute("select * from employees")
# c.execute("select * from employees where prenom=:prenom", e)
# donnees = c.fetchall()
# print(donnees)

# s = {"salaire": 238000, "prenom": "Albertine", "nom": "ZONGO"}
# c.execute("update employees SET salaire=:salaire where prenom=:prenom", s)

c.execute("delete from employees where prenom='Kone'")

connx.commit()
connx.close()
