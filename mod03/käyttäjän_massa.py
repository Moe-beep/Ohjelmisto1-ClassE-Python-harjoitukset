print("Anna leiviskät: ")   
leiviskat = float(input())

print("Anna naulat: ")
naulat = float(input())

print("Anna luodit: ")
luodit = float(input())

gramma = (leiviskat * 20 * 32 + naulat * 32 + luodit) * 13.3
kilogramma = gramma // 1000
jakogramma = round(gramma % 1000, 2)
print("Massa nykymittojen mukaan: ")
print(str(kilogramma) + " kilogrammaa ja " + str(jakogramma) + " grammaa.")