
teksti = input("Anna kokonaisluku:")
while teksti !="":
    luku = int(teksti)
    if(luku < 2):
        print("Luku ei ole alkuluku.")
    for i in range(2,luku):
        if(luku % i == 0):
            print("Luku ei ole alkuluku.")
            break
    else:
        print("Luku on alkuluku.")
    teksti = input("Anna seuraava kokonaisluku tai lopeta painamalla Enter: ")