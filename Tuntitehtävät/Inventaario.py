import random

class Inventory:
    def __init__(self, loitsut_lista = [], reppu = {}):
        self.ll = loitsut_lista
        self.r = reppu

inventory = Inventory()
latu = ("Hyvä", "keskeinen", "Huono")
print("Give items and break loop when empty")
while True:
    quality = random.choice(latu)
    item = input(str())
    if(item == ""):
        break
    inventory.ll.append(item)
    inventory.r[item] = quality

for item in inventory.r:
    print(item + ":" + inventory.r[item])

        