from classes.player import Player
from classes.room import Room
from classes.item import Item

sword = Item("Sword", 5)
shield = Item("Shield", 10)

hall = Room("Hall", sword)
stadium = Room("Stadium", shield)

player1 = Player("John", hall)

print(f"{player1.name} is in {player1.location.name} and has {len(player1.items)} items.")

print("There is a " + player1.location.item.name + " in the " + player1.location.name + ".")
print("Do you want to collect it? (yes/no)")
answer = input().lower()
if answer == "yes":
    player1.collect_item(player1.location.item)
    print(f"{player1.name} collected the {player1.location.item.name}.")
elif answer == "no":
    print("Booo! You loser!")
else:
    print("Invalid input. Please answer 'yes' or 'no'.")

print(f"{player1.name} is in {player1.location.name} and has {len(player1.items)} items.")
print("Let's Bounce to the next room!")
player1.move(stadium)

print(f"There is a {player1.location.item.name} in the {player1.location.name}.")
print("Do you want to collect it? (yes/no)")
answer = input().lower()
if answer == "yes":
    player1.collect_item(player1.location.item)
    print(f"{player1.name} collected the {player1.location.item.name}.")
elif answer == "no":
    print("Booo! You loser!")
else:
    print("Invalid input. Please answer 'yes' or 'no'.")

print(f"{player1.name} is in {player1.location.name} and has {len(player1.items)} items.")