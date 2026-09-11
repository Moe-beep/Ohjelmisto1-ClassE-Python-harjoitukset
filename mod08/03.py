lentoasemat = [
    #Ensimäinen lentokenta
    {
        "lentoasema": "HELSINKI-VANTA",
        "ICAO-koodi": "EFHK"
    },
    ##Toinen lentoasema
    {
        "lentoasema": "HELSINKI-YANGON",
        "ICAO-koodi": "EDGH"
    },
    ##Kolmas 
    {
        "lentoasema": "HELSINKI-VALENCIA",
        "ICAO-koodi": "EGGH"
    }   
]
while True:
    print("Haluatko tallentaa lentoaseman vai etsiä sellaisen?")
    process = input("Paina 1 tallentaaksesi ja 2 etsiäksesi.")
    if(process.lower() == "quit" ):
        break

    if(process != "1" and process != "2"):
        print("Virheellinen input!!")
        continue

    if(process == "1"):
        lentoreitti = str(input("Anna lentoaseman nimi: "))
        koodi = str(input("Anna lentoaseman ICAO koodi: "))
        lentoasemat.append(
            {
                "lentoasema": lentoreitti,
                "ICAO-koodi": koodi
            }
        )

    if(process == "2"):
        print("Esitko lentoaseman nimi tai koodi")
        while True:
            etsitus = str(input("Nimi tai Koodi: "))
            if(etsitus.lower() == "koodi"):
                found = False
                nimi = str(input("Anna aseman nimi: "))
                for lentoasema in lentoasemat:
                    if lentoasema["lentoasema"] == nimi:
                        print(f"Lentoaseman koodi on {lentoasema['ICAO-koodi']}")  
                        found = True
                if not found:
                    print("Lentoasemaa ei löytynyt.")
                break

            elif(etsitus.lower() == "nimi"):
                found = False
                koodi = str(input("Anna aseman koodi: "))
                for lentoasema in lentoasemat:
                    if lentoasema["ICAO-koodi"] == koodi:
                        print(f"Lentoaseman nimi on {lentoasema['lentoasema']}")  
                        found = True
                if not found:
                    print("Lentoaseman koodi ei löytynyt.")
                break
            else:
                print("Virheellinen input!!")
                continue

    