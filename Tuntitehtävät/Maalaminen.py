##kysy käyttäjälta seinän korkeuden ja levyden
print("Anna seinän korkeus meetreinä: ")
korkeus = float(input())
print("Anna seinän leveys meetreinä: ")
leveys = float(input())

##Kysy käyttäjältä maalin peittokyky
print("Anna maalin peittokyky neliömetreinä: ")
peittokyky = float(input())

##Laske seinän pinta-ala
seinän_pinta_ala = korkeus * leveys

##Laske tarvittavan maalin määrä
maali_maara = round(seinän_pinta_ala / peittokyky, 2)
print(f"Tarvittavan maalin määrä on: {maali_maara} litraa")

