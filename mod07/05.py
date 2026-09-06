numero = input("Anna kokonaisluku: ")
lista = []
pari_li = []

while numero != "":
    numero = int(numero)
    lista.append(numero)
    if numero % 2 == 0:
        pari_li.append(numero)
    numero = input("Anna seuraava kokonaisluku tai lopeta painamalla Enter: ")

print("Lista: " + str(lista))
print("Parilliset luvut: " + str(pari_li))