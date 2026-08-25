print("Mikä on sun sukupuoli? (M/N)")
print("M = mies, N = nainen")
sukupuoli = str(input())

print("Mikä on sun hemoglobiiniarvo? (g/l)")
hemoglobiini = float(input())

if sukupuoli == "M":
    if 134 <= hemoglobiini <= 193:
        print("Hemoglobiiniarvo on normaali.")
    elif hemoglobiini < 134:
        print("Hemoglobiiniarvo on liian alhainen.")
    elif hemoglobiini > 193:
        print("Hemoglobiiniarvo on liian korkea.")
elif sukupuoli == "N":
    if 117 <= hemoglobiini <= 175:
        print("Hemoglobiiniarvo on normaali.")
    elif hemoglobiini < 117:
        print("Hemoglobiiniarvo on liian alhainen.")
    elif hemoglobiini > 175:
        print("Hemoglobiiniarvo on liian korkea.")
