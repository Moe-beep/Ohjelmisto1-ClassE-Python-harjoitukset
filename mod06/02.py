luku = input("Anna luku: ")
list = []
while luku != "":
    luku = int(luku)
    list.append(luku)
    luku = input("Anna seuraava luku tai lopeta painamalla Enter: ")

list.sort()
print(list[-5:])