import random

numero = random.randint(1,10)

while True:
    guess = int(input("Arva numero 1 ja 10 välillä! "))

    if(guess == numero):
        print("Oikein!!")
        break

    if(numero > guess):
        print("liaan pieni arvaus! Yritä uudellan")
    else:
        print("Liian suuri arvaus! Yritä uudellan")