class monster:
    def __init__(self,name,health,scream ="Rwahhhhhhhhh.."):
        self.name = name
        self.health = health
        self.scream = scream

##Ostopeli
##Ahhhhhh, mun Rahaaaaaaaaaaa
def minus_raha(money, amount):
    money = money - amount
    return money

def ask_to_buy(name,price):
    print()
    while True:
        print(f"What about this {name} product")
        type = str(input())

##Moi Moi peli
def quit():
    print()
    print("Kiitos pelaamisesta!!")
    print_list(osto_lista)
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
    if(ika < 12):
        print("Sinä et osaa auttaa minua!!!")
        break

    print()
    print("Hei " + nimi + "! Tervetuloa peliin!!")
    ##Add code for asking what the player want to play
    print("Mennään ostoksille!!!!!! Sen pitäisi olla HAUSKAA!")

    ##Add 2 more games for more routes
    ##Encourage player
    while True:
        print()
        yay = str(input("Sano Yayyyyyyy: "))

        if(yay[:3].lower() == "yay"):
            break
        else:
            print("Yritä uudelleen :( ")

    ##Ask for the amount
    print()
    print("Arvioikaa, kuinka paljon rahaa tarvitsemme?")
    while True:
        
        money = float(input("Kerro summa: "))

        if(money <= 1000):
            print()
            print(f"Otan {money} euroa pankkitililtäni")
            break
        elif(money > 1000):
            print()
            print("Luuletko että olen miljonääri??")
            print("Pienennä summaa!!")
        elif(str(money).lower() == "quit"):
            quit()
        else:
            print()
            print("Virheellinen vastaus!")

    ##Osto Lista
    osto_lista = []
    ##Ask to buy bed
    print("Ensin tarvitsemme sängyn.")
    print("Löysin tämän sängyn 200 eurolla, ostetaan se")
    while True:
        type = str(input("Yes tai No!!  "))

        if(type.lower() == "yes"):
            money = minus_raha(money, 200)
            print()
            print("Okei, hyvä on. Aion nukkua mukavasti!!")
            add_to_list("Sängy", osto_lista)
            ##This quit is just ffor testing, it will be removed later
            quit()
            break

        elif(type.lower() == "no"):
            print()
            print("EN minä nuku lattialla!!")
            print("Kysyn uudestaan!!")
        elif(type.lower() == "quit"):
            print()
            print("Bye Bye!!")
            quit()
        else:
            print()
            print("Virheellinen vastaus")

    ##Ask about another object