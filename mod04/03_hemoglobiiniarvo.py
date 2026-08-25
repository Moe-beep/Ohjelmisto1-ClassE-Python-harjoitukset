#Kysy sukupuoli ja hemoglobiiniarvo
print("Mikä on sun sukupuoli? (M/N)")
print("M = mies, N = nainen")
sukupuoli = str(input())

print("Mikä on sun hemoglobiiniarvo? (g/l)")
hemoglobiini = float(input())

#Kerro onko hemoglobiiniarvo normaali, liian alhainen vai liian korkea
if sukupuoli == "M":
    if 134 <= hemoglobiini <= 193:
        print("Hemoglobiiniarvo on normaali.")
    elif hemoglobiini < 134:
        print("Hemoglobiiniarvo on liian alhainen.Se pitäisi olla 134 ja 193 välillä.")
    elif hemoglobiini > 193:
        print("Hemoglobiiniarvo on liian korkea.Se pitäisi olla 134 ja 193 välillä.")
elif sukupuoli == "N":
    if 117 <= hemoglobiini <= 175:
        print("Hemoglobiiniarvo on normaali.")
    elif hemoglobiini < 117:
        print("Hemoglobiiniarvo on liian alhainen.Se pitäisi olla 117 ja 175 välillä.")
    elif hemoglobiini > 175:
        print("Hemoglobiiniarvo on liian korkea.Se pitäisi olla 117 ja 175 välillä.")
