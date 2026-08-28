numero = int(input("Anna Numeroa: "))
smallest = 0
biggest = 0
while True:
    if numero == "":
        break

    numero = int(numero)
    if(numero > biggest):
        biggest = numero
    elif(numero < smallest):
        smallest = numero

    numero = input("Anna Numeroa: ")
print(f"Pienin on {smallest} ja suurin on {biggest}")
    