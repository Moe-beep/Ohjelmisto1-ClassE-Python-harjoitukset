i = 0
kau_li = []
while i < 5:
    kaupunki = input("Anna kaupungin nimi:")
    if kaupunki =="":
        break
    kau_li.append(kaupunki)
    i += 1

for n in kau_li:
    print(n)
