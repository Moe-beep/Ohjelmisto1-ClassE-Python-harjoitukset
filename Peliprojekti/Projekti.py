from functions import boat_task, boat_trash_cleanup, boat_oil_cleanup
from functions import quit, add_to_list, invalid_tarkistu, completed_tasks, boat_supplies, submarine_supplies, Character
import random
import os





def shark_task():
    print("Ok, We are going to call our shark friend to help us.")
    print("You tapped the water and the shark cam immediately.")
    print("let's fend off ilegal fishing boats")


while True:
    ##Kysy nimi käyttäjältä
    print("Mikä sinun nimesi on?")
    nimi = str(input())
    if invalid_tarkistu(nimi):
        continue

    print("Mikä on sinun ikäsi?")
    ika = int(input())
    if invalid_tarkistu(ika):
        continue

    ##Kysy käyttäjän ika
    if(ika < 6):
        print("You are too young to help me!!!")
        break

    print()
    print("Hello " + nimi + "! Welcome to the game!!")
    ##Add code for asking what the player want to play
    print("Let's save the sea from the pollution!!")

    ##Add 2 more games for more routes
    ##Encourage player
    while True:
        print()
        yay = str(input("Say Yayyyyyyy: "))

        if(yay[:3].lower() == "yay"):
            break
        else:
            print("Try again :( ")

    ##Ask for mode of transport
    print()
    print("Let's choose how we are going to travel through water!!")
    while True:
        print("1. Boat")
        print("2. Submarine")
        print("3. Shark")
        choice = input("Choose your mode of transport: ")

        ## the task for boat
        if choice == "1":
            print("You have chosen the boat. Let's go!")
            boat_task()
            boat_trash_cleanup()
            boat_oil_cleanup()
            break
        ## the task for submarine
        elif choice == "2":
            print("You have chosen the submarine. Let's go!")
            break
        ## the task for shark
        elif choice == "3":
            print("You have chosen the shark. Let's go!")
            break
        elif choice.lower() == "quit":
            quit()
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


