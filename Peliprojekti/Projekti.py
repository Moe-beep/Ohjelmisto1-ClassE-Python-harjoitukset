
while True:
    ##Kysy nimi käyttäjältä
    print("Mikä sinun nimesi on?")
    nimi = str(input())
    print("Mikä on sinun ikäsi?")
    ika = int(input())
    if(ika < 12):
        print("Sinä olet liian nuori!!!")
        break

    print("Hei " + nimi + "! Tervetuloa peliin!!")
    print("Mennään ostoksille!!!!!! Sen pitäisi olla HAUSKAA!")

    ##Encourage player
    while True:
        yay = str(input("Sano Yayyyyyyy: "))

        if(yay[:3].lower() == "yay"):
            break
        else:
            print("Yritä uudelleen :( ")

    ##Ask for the amount
    print("Arvioikaa, kuinka paljon rahaa tarvitsemme?")
    while True:
        
        money = float(input("Kerro summa: "))

        if(money <= 1000):
            print(f"Otan {money} euroa pankkitililtäni")
            break
        elif(money > 1000):
            print("Luuletko että olen miljonääri??")
            print("Pienennä summaa!!")
        elif(str(money).lower() == "quit"):
            quit()
        else:
            print("Virheellinen vastaus!")

    ##Ask to buy bed
    print("Ensin tarvitsemme sängyn.")
    print("Löysin tämän sängyn 200 eurolla, ostetaan se")
    while True:
        type = str(input("Yes tai No!!  "))

        if(type.lower() == "yes"):
            money = money - 200
            print("Okei, hyvä on. Aion nukkua mukavasti!!")
            ##This quit is just ffor testing, it will be removed later
            quit()
            break

        elif(type.lower() == "no"):
            print("EN minä nuku lattialla!!")
            print("Kysyn uudestaan!!")
        elif(type.lower() == "quit"):
            print("Bye Bye!!")
            quit()
        else:
            print("Virheellinen vastaus")



