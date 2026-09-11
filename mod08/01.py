weathers = "spring", "summer", "autumn", "winter"
months = (3,4,5), (6,7,8), (9,10,11), (12,1,2)

kuu = int(input("Anna kuukausi (1-12): "))

for i in range(len(months)):
        if kuu in months[i]:
            print(weathers[i])