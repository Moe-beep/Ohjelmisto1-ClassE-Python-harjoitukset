#Tulosta juomat joita käyttäjät voivat tilata
print("Meillä on Kahvi, Viini, Olut ja Öljy juomat")

#Kysy käyttäjän ikä ja lajin
print("Mikä on sinun ikäsi?")
ikä = int(input())

print("Mikä on sinun lajisi?")
print("Siellä on neljä lajit. Robotti- R, Tontu - T, Ihmisen - I")
print("Syötä lajisi nimikirjaimet")
laji = str(input())

print("Sinä voit tilata kahvia.")

if laji == "I" and ikä >= 18:
    print("Sinä voit tilata viiniä.")

if laji == "T" and ikä >= 100:
    print("Sinä voit tilata olutta.")

if laji == "R":
    print("Sinä voit tilata öljyä.")