## Kysy käyttäjältä suorakulmion korkeus ja leveys
print("Anna suorakulmion korkeus: ")
korkeus = float(input())
print("Anna suorakulmion leveys: ")
leveys = float(input())


## Laske suorakulmion piiri ja pinta-ala
Suorakulmion_piiri = 2 * (korkeus + leveys)
Suorakulmion_area = korkeus * leveys
print("Suorakulmion piiri on: " + str(Suorakulmion_piiri))
print("Suorakulmion pinta-ala on: " + str(Suorakulmion_area))