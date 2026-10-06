
class Character:
    def __init__(self,name,health,scream ="Rwahhhhhhhhh.."):
        self.name = name
        self.health = health
        self.scream = scream

#save game
def read_file(filename):
    with open(filename, "r")as file:
        return file.read()
    
def save_game(name,age,completed_tasks):
    with open("save.txt", "w")as file:
        file.write(f"{name}\n{age}\n{','.join(completed_tasks)}")

def load_game(filename):
    with open(filename, "r")as file:
        data = file.read().splitlines()
        name = data[0]
        age = int(data[1])
        completed_tasks = data[2].split(",")
        return name, age, completed_tasks




##Moi Moi peli
def quit():
    print()
    print("Kiitos pelaamisesta!!")
    exit()

##Tarkistus funktio jos Input oli tyhjä tai ei
def invalid_tarkistu(input):
    if(str(input) == ""):
        print("Virheellinen vastaus!!")
        return True
    elif(str(input).lower() == "quit"):
        quit()
    return False


##Have not implemented them funtions in game yet, COMING SOON!!!
##Lisää listaan
def add_to_list(item,list):
    list.append(item)
    return list
##Tulosta listasta
def print_list(list):
    if(len(list) == 0):
        print("OstoLista on tyhjä!!")
    for item in list:
        print(item)


##Boat task    
boat_supplies = []
submarine_supplies = []
completed_tasks = []