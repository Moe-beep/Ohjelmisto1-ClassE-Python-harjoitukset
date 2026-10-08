class Character:
    def __init__(self,name,health,scream ="Rwahhhhhhhhh.."):
        self.name = name
        self.health = health
        self.scream = scream

##supplies and completed tasks   
supplies = []
completed_tasks = []

##Check if the player has played the game
saved_transport = ""
line_to_delete = 0
def check_name(name):
    #Globalizing the object
    global saved_transport
    global line_to_delete
    with open(".\\Peliprojekti\\save.txt", "r") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if line.startswith("Name : "):
            ##What his basically does is splitting the name line in 2 different sectors from : and
            ##[1]choose the name that will come later and strip() removes unecesssary blanks
            saved_name = line.split(":", 1)[1].strip()

            
            if saved_name.lower() == str(name).lower():
                

                age = ""
                transport = ""
                equipment = ""
                tasks = ""

                if i + 1 < len(lines) and lines[i+1].startswith("Age :"):
                    age = lines[i+1].split(":", 1)[1].strip()

                if i + 2 < len(lines) and lines[i+2].startswith("Transport choice :"):
                    transport = lines[i+2].split(":", 1)[1].strip()
                    saved_transport = str(transport)
                    print(saved_transport)

                if i + 3 < len(lines) and lines[i+3].startswith("Equipments :"):
                    equipment = lines[i+3].split(":", 1)[1].strip()

                if i + 4 < len(lines) and lines[i+4].startswith("Completed tasks :"):
                    tasks = lines[i+4].split(":", 1)[1].strip()

                if not age:
                    return "age_no"
                elif not transport:
                    line_to_delete = 2
                    return "transport_no", ""
                elif not equipment:
                    line_to_delete = 3
                    delete_save(name)
                    save_name_and_age(name,age)
                    save_choice(transport)
                    return "equipment_no", transport
                elif not tasks:
                    line_to_delete = 4
                    supplies.extend(item.strip() for item in equipment.split(","))
                    delete_save(name)
                    save_name_and_age(name,age)
                    save_choice(transport)
                    save_equipment(supplies)
                    return "tasks_no",transport
                else:
                    line_to_delete = 5
                    supplies.extend(item.strip() for item in equipment.split(","))
                    completed_tasks.extend(task.strip() for task in tasks.split(","))
                    delete_save(name)
                    save_name_and_age(name,age)
                    save_choice(transport)
                    save_equipment(supplies)
                    save_tasks(completed_tasks)
                    return "completed", ""
    return False, ""


def delete_save(name):
    with open(".\\Peliprojekti\\save.txt", "r") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if line.startswith("name : " + name):
            del lines[i:i+line_to_delete]
            break

    with open(".\\Peliprojekti\\save.txt", "w") as f:
        f.writelines(lines)
#save game
def save_name_and_age(name,age):
    with open(".\\Peliprojekti\\save.txt", "a") as f:
        f.write("Name : " + name + "\n")
        f.write("Age : " + age + "\n")

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


