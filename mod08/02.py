nimi = "nimi"
nimi_set = set()
while True:
    nimi = str(input("Anna nimi tai lopeta painamalla Enter: "))
    if nimi in nimi_set:
        print("Aiemmin syötetty nimi!")
    elif nimi == "":
        break
    else:
        print("Uusi nimi!")
        nimi_set.add(nimi)

print("Nimet ovat: ")
for nimi in nimi_set:
    print(nimi)