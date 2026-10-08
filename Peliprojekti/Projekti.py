from functions import boat_task, boat_trash_cleanup, boat_oil_cleanup
from functions import submarine_task, submarine_monster_fight
from functions import shark_task
from functions import quit, add_to_list, invalid_tarkistu, completed_tasks, supplies, Character, save_choice,saved_transport,check_name
import random
import os

#Check if theyhave played
while True:
    name_exist = False

    print("Have you played this game before?")
    play = input("Answer Y/N : ")
    if play.lower() == "n":
        break

    name = input("Write the name you used while playing: ")

    result,saved_transport = check_name(name)

    if result == "transport_no":
        print("You have only name and age entered, Let's play all the way from the start!")

    elif result == "equipment_no":
        name_exist = True
        print("You have played before, but your equipment is missing.")
        if saved_transport == "Boat":
            boat_task()
            boat_trash_cleanup()
            boat_oil_cleanup()
        elif saved_transport == "Submarine":
            submarine_task()
            submarine_monster_fight()
        elif saved_transport == "Shark":
            shark_task()

    elif result == "tasks_no":
        name_exist = True
        print("You have played before, but your completed tasks are missing.")
        if saved_transport == "Boat":
            boat_trash_cleanup()
            boat_oil_cleanup()
        elif saved_transport == "Submarine":
            submarine_monster_fight()
        elif saved_transport == "Shark":
            shark_task()

    elif result == "completed":
        print("Yes, you have played the game before and you have completed the game!")
        print("Play a new game")
    elif result == False:
        print("No saved game was found with that name.")
        # Start a new game / create player here
    break

##Ask Name
while True:
    if name_exist == True:
        break
    ##Kysy nimi käyttäjältä
    print("Mikä sinun nimesi on?")
    nimi = str(input())
    if nimi.lower() == "quit":
        quit()
    if invalid_tarkistu(nimi):
        continue

    print("Mikä on sinun ikäsi?")
    ika = input()
    if ika.lower() == "quit":
        quit()
    if invalid_tarkistu(ika):
        continue

    ##Kysy käyttäjän ika
    #if(ika < 6):
        #print("You are too young to help me!!!")
        #break

    ##Writing name and age in file
    with open(".\\Peliprojekti\\save.txt", "a") as f:
        ika = str(ika)
        f.write("\n" + "\n" + "Name : " + nimi + "\n")
        f.write("Age : " + ika + "\n")

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
            save_choice("Boat")
            print("You have chosen the boat. Let's go!")
            boat_task()
            boat_trash_cleanup()
            boat_oil_cleanup()
            break
        ## the task for submarine
        elif choice == "2":
            save_choice("Submarine")
            print("You have chosen the submarine. Let's go!")
            submarine_task()
            submarine_monster_fight()
            break
        ## the task for shark
        elif choice == "3":
            save_choice("Shark")
            print("You have chosen the shark. Let's go!")
            shark_task()
            break
        elif choice.lower() == "quit":
            quit()
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")
    break


