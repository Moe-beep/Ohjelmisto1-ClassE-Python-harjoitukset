from .common import quit, add_to_list, completed_tasks, supplies, Character, save_equipment,save_tasks

import random

##Choosing supplies
def submarine_task():
    supplies.clear()
    print("Ok, let's stock up on supplies for our submarine journey!")
    print("We are going to fight the sea monsters threatening the ocean.")
    print("Let's choose the right tools and equipment for our mission.")

    ##choose supplies
    print("I have ")
    print("1. Trash bags")
    print("2. Spear gun")
    print("3. Underwater camera")
    print("4. Extra fuel for the submarine")

    while len(supplies) < 2:
        supply_choice = input("Choose a supply to add to your submarine, only 2 supplies can be chosen.")
        if supply_choice == "1":
            add_to_list("Trash bags", supplies)
            print("Trash bags added to your submarine supplies.")
        elif supply_choice == "2":
            add_to_list("Spear gun", supplies)
            print("Spear gun added to your submarine supplies.")
        elif supply_choice == "3":
            add_to_list("Underwater camera", supplies)
            print("Underwater camera added to your submarine supplies.")
        elif supply_choice == "4":
            add_to_list("Extra fuel for the submarine", supplies)
            print("Extra fuel for the submarine added to your submarine supplies.")
        elif supply_choice.lower() == "quit":
            quit()
        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")
    save_equipment(supplies)
    print("Ok! Supplies are ready! Let's Roll!!")

##Using Character class
def submarine_monster_fight():
    print("I see the sea Monster! It's green,big and scary!")
    m_name = str(input("What should we name the sea monster? "))
    health = random.randint(50, 100)
    monster = Character(m_name, health)
    print(f"The sea monster's name is {monster.name} and it has {monster.health} health points.")
    print(f"It screams: {monster.scream}")

    while monster.health > 0:
        if "Spear gun" in supplies:
            print("You have the spear gun. Let's use it to fight the sea monster!")
            attack = input("Type 1 to attack the sea monster: ")
            if attack == "1":
                damage = random.randint(10, 20)
                monster.health -= damage
                print("")
                print(f"You attacked the sea monster and dealt {damage} damage! The sea monster has {monster.health} health points left.")
                if monster.health <= 0:
                    print("")
                    print("You have defeated the sea monster! Great job!")
                    completed_tasks.append("Sea Monster Fight")
                    print("Oh no! We are running out tof fuel after attacking!")
                    fuel = input("Did you bring extra fuel(Y/N)?")
                    if fuel.lower() == "y":
                        print()
                        submarine_refuel()
                    elif fuel.lower() == "n":
                        print()
                        submarine_refuel()
                    elif fuel.lower() == "quit":
                        quit()
                    else:
                        print()
                        print("I don't understand! I will check myself")
                        submarine_refuel()
                    break
            elif attack.lower() == "quit":
                quit()
            else:
                print()
                print("Invalid answer!")
        else:
            print("")
            print("You don't have the spear gun. We can't fight the sea monster without it.")
            print("Let's run away!!")
            print("Ohh no. We are running out of fuel for the submarine. We need to refuel the submarine to continue our journey.")
            fuel = input("Did you bring extra fuel(Y/N)?")
            if fuel.lower() == "y":
                print()
                submarine_refuel()
            elif fuel.lower() == "n":
                print()
                submarine_refuel()
            elif fuel.lower() == "quit":
                quit()
            else:
                print()
                print("I don't understand! I will check myself")
                submarine_refuel()
            break

##Refuel
def submarine_refuel():
    if "Extra fuel for the submarine" in supplies:
        print("You have the extra fuel for the submarine. Let's use it to refuel the submarine!")
        print("The submarine is refueled and we can continue our journey!")
        completed_tasks.append("Submarine Refuel")
        save_tasks(completed_tasks)
    else:
        print("You don't have the extra fuel for the submarine. We can't refuel the submarine without it.")
        print("Let's head back to the surface and wait for rescue. Good job for trying!")
        save_tasks(completed_tasks)