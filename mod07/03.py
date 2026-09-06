def muutos(galloni):
    litrat = galloni * 3.785
    print(f"{galloni} gallonaa on {litrat} litraa.")

luku = float(input("Anna gallonan määrä: "))
while luku > 0 :
    muutos(luku)
    luku = float(input("Anna gallonan määrä: "))
    
    