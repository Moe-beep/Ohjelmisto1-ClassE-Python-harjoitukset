#Kysy vuosiluku 
print("Mikä on vuosiluku?")
vuosi = int(input("Anna vuosi: "))

#Kerro josko vuosi on karkausvuosi vai ei
if(vuosi % 4 == 0 and vuosi % 100 != 0) or (vuosi % 400 == 0):
    print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")