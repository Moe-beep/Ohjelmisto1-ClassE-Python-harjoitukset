print("Anna vuosi")
vuosi = int(input())
while vuosi > 1896:
    
    if vuosi == 2020:
        print("koronan takia, ei ollut olympiavuosi")
    elif vuosi == 2021:
        print("koronan takia, oli olympiavuosi")
    elif(vuosi % 4) == 0 and vuosi > 1800:
        print("Oli Olympiavuosi")
    elif(vuosi % 4) != 0 and vuosi > 1800:
        print("Ei ollut olympiavuosi")     

    print("Anna vuosi")
    vuosi = int(input()) 

print("Vuosi on pienempi kuin 1896")
print("Program lopetettu!!!")

