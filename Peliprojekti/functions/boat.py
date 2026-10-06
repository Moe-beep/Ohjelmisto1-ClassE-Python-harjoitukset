import os
from .common import quit, add_to_list, completed_tasks, boat_supplies, invalid_tarkistu

def boat_task():
    ##this print the loction of the file of the method
    print(os.getcwd())
    with open(".\\Peliprojekti\\info.txt", "r") as file:
        lines = file.readlines()
        print("".join(lines[0:4]))
        print("".join(lines[6:11]))

    while len(boat_supplies) < 2:
        supply_choice = input("Choose a supply to add to your boat, only 2 supplies can be chosen.")
        if supply_choice == "1":
            add_to_list("Trash bags", boat_supplies)
            print("Trash bags added to your boat supplies.")
        elif supply_choice == "2":
            add_to_list("Oxygen Tanks", boat_supplies)
            print("Oxygen Tanks added to your boat supplies.")
        elif supply_choice == "3":
            add_to_list("Oil spill cleanup kit", boat_supplies)
            print("Oil spill cleanup kit added to your boat supplies.")
        elif supply_choice == "4":
            add_to_list("Spear gun", boat_supplies)
            print("Spear gun added to your boat supplies.")
        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")
    print("Ok! Supplies are ready! Let's Roll!!")

def boat_trash_cleanup():
    print("We are here at the trash cleanup site. Let's get to work!")
    print("Let's take out the trash bags and start picking up the trash in the ocean.")

    if "Trash bags" in boat_supplies:
        print("You have the trash bags. Let's start picking up the trash!")
        print("Type 1 to pick up trashes.")

        i = 0
        while i<5:
            i += 1
            pick_up = input("Type 1 to pick up trashes: ")
            if pick_up == "1":
                if i < 3:
                    print(f"Good job!Keep going!")
                elif i == 3:
                    print("We are halfway there! Don't give up!")
                elif i == 4:
                    print("We are almost done! You got this!")
                elif i == 5:
                    print("You have picked up all the trash! Great work!")
                    completed_tasks.append("Trash Cleanup")
                    break
            elif pick_up.lower() == "quit":
                quit()
            else:
                print("Invalid choice. Please type 1 to pick up trashes.")
    else:
        print("You don't have the trash bags. We can't pick up the trash without them.")
        print("Let's just head to Oil spill cleanup site instead.")

def boat_oil_cleanup():
    print("We are here at the oil spill cleanup site. Let's get to work!")
    print("Let's take out the oil spill cleanup kit and start cleaning up the oil spill in the ocean.")

    if "Oil spill cleanup kit" in boat_supplies:
        print("You have the oil spill cleanup kit. Let's start cleaning up the oil spill!")
        print("Type 1 to clean up the oil spill.")

        i = 0
        while i<5:
            i += 1
            clean_up = input("Type 1 to clean up the oil spill: ")
            if clean_up == "1":
                if i < 3:
                    print(f"Good job!Keep going!")
                elif i == 3:
                    print("We are halfway there! Don't give up!")
                elif i == 4:
                    print("We are almost done! You got this!")
                elif i == 5:
                    print("You have cleaned up all the oil spill! Great work!")
                    completed_tasks.append("Oil Spill Cleanup")
                    break
            elif clean_up.lower() == "quit":
                quit()
            else:
                print("Invalid choice. Please type 1 to clean up the oil spill.")
    else:
        print("You don't have the oil spill cleanup kit. We can't clean up the oil spill without it.")
        print("Let's just head home and save the ocean another day. Good job for trying!") 

