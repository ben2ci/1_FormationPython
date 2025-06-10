import time


print("LA BOUCLE FOR")
liste = ['Riz,', 'Pommes,', 'Lait', 'Salade', 'Saumon', 'Beurre']

for i in liste:
    print(i)

    if i == 'Lait':
        continue


for n in range(0, 10):
    print(n)

print("LA BOUCLE WHILE 1")
m = 0
while m < 10:
    print(m)
    m += 1

point = 0
print("Sauvegarde en cours", end='', flush=False)
while True:
    print(".", end='', flush=True)
    point += 1
    time.sleep(2)

