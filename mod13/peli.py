import os

def read_file(name):
    with open(name, "r") as f:
        return f.read()

print(read_file("intro.txt"))
print(read_file("instructions.txt"))

name = input("Enter your name: ")

if os.path.exists(name + ".txt"):
    with open(name + ".txt") as f:
        position = int(f.read())
    print("Saved game loaded!")
else:
    position = 0
    print("New game started!")

while True:
    print("\nYou are at location", position)
    choice = input("Your choice: ")

    if choice == "1":
        position += 1
    elif choice == "2":
        position += 2
    elif choice == "3":
        print("Game saved. Goodbye!")
        break
    else:
        print("Invalid choice.")
        continue

    with open(name + ".txt", "w") as f:
        f.write(str(position))

    if position >= 10:
        print("You reached the goal!")
        os.remove(name + ".txt")
        break