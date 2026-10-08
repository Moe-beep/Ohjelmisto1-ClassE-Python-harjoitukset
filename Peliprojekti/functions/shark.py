from .common import quit, completed_tasks, Character, save_tasks, save_choice
import random

#Simple shark game
def shark_task():
    print("Ok, We are going to call our shark friend to help us.")
    print("You tapped the water and the shark cam immediately.")

    print("ok let's go!")
    print("You get on the shark's back and it swiftly carries you through the water.")

    print("We have 2 enemies to defeat, pick one the one you want to fight.")
    print("A swarm of baby sharks will take care of the other one!")
    print("1. Pirates")
    print("2. Sea monsters")

    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        print("You have chosen to fight the pirates. Let's go!")
        health = random.randint(50, 100)
        pirate = Character("Pirate", health)

        while True:
            print()
            attacks = {"Twisted shark bite": 20, "swift tail slap": 15, "Jump and slam": 30}
            if pirate.health > 0:
                attack = input("Type 1 to attack the pirate: ")
                if attack == "1":
                    attack_name, damage = random.choice(list(attacks.items()))
                    pirate.health -= damage
                    print()
                    print(f"You used {attack_name} and dealt {damage} damage! The pirate has {pirate.health} health points left.")
                    if pirate.health <= 0:
                        print("You have defeated the pirate! Great job!")
                        completed_tasks.append("Pirate Fight")
                        save_tasks(completed_tasks)
                        break
                elif attack.lower() == "quit":
                    quit()
                else:
                    print()
                    print("Invalid answer!! Type 1")
    elif choice == "2":
        print()
        print("You have chosen to fight the sea monsters. Let's go!")
        monster_health = random.randint(50, 100)
        monster = Character("Sea Monster", monster_health)
        while True:
            attacks = {"Twisted shark bite": 20, "swift tail slap": 15, "Jump and slam": 30}
            if monster.health > 0:
                attack = input("Type 1 to attack the sea monster: ")
                if attack == "1":
                    attack_name, damage = random.choice(list(attacks.items()))
                    monster.health -= damage
                    print(f"You used {attack_name} and dealt {damage} damage! The sea monster has {monster.health} health points left.")
                    if monster.health <= 0:
                        print("You have defeated the sea monster! Great job!")
                        completed_tasks.append("Sea Monster Fight")
                        save_tasks(completed_tasks)
                        break
                elif attack.lower() == "quit":
                    quit()
                else:
                    print()
                    print("Invalid answer! Type 1")
    elif choice.lower() == "quit":
        quit()
    else:
        print()
        print("Invalid choice. Please choose 1 or 2.")

    print("Baby shark came back from fighting and you united with them")
    print("PHEWW!! Saved the ocean once again")