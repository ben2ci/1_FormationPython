from tinydb import TinyDB, Query, where

db = TinyDB('data.json', indent=4)

# db.insert({"name": "Patrick", "score": 0})
# db.insert_multiple([
#     {"name": "Julie", "score": 50},
#     {"name": "Paul", "score": 120},
# ])

User = Query()
patrick = db.search(User.name == "Patrick")
print(patrick)

high_scores = db.search(where("score") > 0)
print(high_scores)
print(len(db))
print(db.contains(User.name == "Patrick"))
print(db.count(User.name == "Patrick"))