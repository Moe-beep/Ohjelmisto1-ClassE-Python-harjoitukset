omenoiden_määrä = 5
appelsiinien_määrä = 10
if omenoiden_määrä > appelsiinien_määrä:
    print("Omenoita on enemmän kuin appelsiineja.")
elif omenoiden_määrä < appelsiinien_määrä:
    print("Appelsiineja on enemmän kuin omenoita.")
else:
    print("Omenoita ja appelsiineja on yhtä paljon.")

lampotila = 25
if lampotila < 0:
    print("On pakkasta.")
elif lampotila >0 :
    print("On plussaa.")

pistettä = 170
if pistettä >= 150:
    print("Sinä pääsit")
else:
    print("Sinä et päässyt")

lampotila = 25
pilivi = False
if lampotila > 20 and not pilivi:
    print("On lämmin ja aurinkoista.")
elif lampotila > 20 and pilivi:
    print("On lämmin mutta pilvistä.")

koko = 70
vuotias = 15
if 10 > koko <= 65 or vuotias > 10:
    print("Kala on harvinainen.")

weekday = True
age = 20
if weekday and 12 <= age >= 65:
    print("Saa matkustaa ilmaiseksi.")
elif not weekday and age <=5 :
    print("Saa matkustaa ilmaiseksi.")
else:
    print("Ei saa matkustaa ilmaiseksi.")