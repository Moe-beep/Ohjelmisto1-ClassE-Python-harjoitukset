käyttäjatunnus = "python"
salasana = "rules"
kerta = 0

while True:
    user = str(input("Kirjoittaa käyttäjätunnus"))
    pw = str(input("Kirjoittaa salasana"))

    if(käyttäjatunnus == user and salasana == pw):
        print("Tervetuloa!!")
        break
    else:
        kerta = kerta + 1
        print("Käyttäjatunna tai salasana on väärin!!")

    if(kerta == 5):
        print("Käytit kaikki yrityksesi!!!")
        break