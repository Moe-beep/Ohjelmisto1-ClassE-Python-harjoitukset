#Kysy kuhan pitus
print("Mikä on kuhan pituus senttimetreinä?")
pitus = float(input())

# Tarkista onko kuha tarpeeksi pitkä
if pitus < 37:
    print(f"Laskee kuhan takaisin järveen!!! Kuha on {37 - pitus} cm normaalia lyhyempi")
else:
    print("Saat ottaa kuhan kotiin.")

