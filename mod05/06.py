import random

print("Anna n numero")
numero = int(input())

kerta = 0
i = 0

while True:
    if(i == numero):
        break 

    x_numero = random.uniform(-1, 1)
    y_numero = random.uniform(-1, 1)

    summa = (x_numero * x_numero) + (y_numero * y_numero)

    if(summa < 1):
        kerta = kerta + 1

    i = i + 1

pi = (4 * kerta) / numero

print("Piin likiarvo on " + str(pi))
