import random

numero = int(input("Anna arpakuutioiden lukumäärä: "))
summa = 0

for i in range(numero):
    silmaluku = random.randint(1, 6)
    summa += silmaluku
    print(f"Arpakuution silmäluku on {silmaluku}")

print(f"Arpakuutioiden summa on {summa}")