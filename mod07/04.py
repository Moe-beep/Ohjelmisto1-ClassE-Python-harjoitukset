def summa(nlist):
    summa = 0
    for n in nlist:
        summa += n
    return summa

listan_numero = input("Anna kokonaisluku: ")
nlist = []

while listan_numero != "":
    listan_numero = int(listan_numero)
    nlist.append(listan_numero)
    listan_numero = input("Anna seuraava kokonaisluku tai lopeta painamalla Enter: ")


print("Lista: " + str(nlist))
print("Sen summa: " + str(summa(nlist)))
