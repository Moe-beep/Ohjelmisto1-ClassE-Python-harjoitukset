
class Character:
    def __init__(self,name,health,scream ="Rwahhhhhhhhh.."):
        self.name = name
        self.health = health
        self.scream = scream

#save game
def save_choice(name):
    with open(".\\Peliprojekti\\save.txt", "a") as f:
        f.write("Transport choice : " + name + "\n")

def save_equipment(list):

    line = ", ".join(list)
    with open(".\\Peliprojekti\\save.txt", "a") as f:
        f.write("Equipments : " + line + "\n")

def save_tasks(list):
    if len(list) > 0:
        line =  ", ".join(list)
        with open(".\\Peliprojekti\\save.txt", "a") as f:
            f.write("Completed tasks : " + line)
    else:
        with open(".\\Peliprojekti\\save.txt", "a") as f:
            f.write("Completed tasks : None")




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