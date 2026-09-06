import math

##Diameter as parameter
def pizzan_halkaisija(diameter, hinta):
    r = (diameter / 2) / 100
    pinta_ala = math.pi * r ** 2
    return hinta/pinta_ala

###Kysy ensimmäisen pizzan tiedot
halkaisija1 = float(input("Anna  ensimmäisen pizzan halkaisija centtimetreinä: "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta euroina: "))

##Kysy toisen pizzan tiedot
halkaisija2 = float(input("Anna  toisen pizzan halkaisija centtimetreinä: "))
hinta2 = float(input("Anna toisen pizzan hinta euroina: "))

pizza1 = pizzan_halkaisija(halkaisija1, hinta1)
pizza2 = pizzan_halkaisija(halkaisija2, hinta2)

if pizza1 < pizza2:
    print("Ensimmäinen pizza on edullisempi.")
elif pizza1 > pizza2:
    print("Toinen pizza on edullisempi.") 
else:
    print("Pizzat ovat yhtä edullisia.")