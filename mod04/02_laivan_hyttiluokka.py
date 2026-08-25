#Kysy laivan hyttiluokka
print("Mikä on laivan hyttiluokka?\n" \
 "Siellä on neljä hyttiluokkaa: LUX, A, B, ja C")
luokka = str(input("Anna hyttiluokka: "))

#Kerro hyttiluokan ominaisuudet
if luokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif luokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif luokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif luokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")