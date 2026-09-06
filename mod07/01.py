import random

def roll():
    print("Heittää noppaa!")
    count = 0
    while True:
        num = random.randint(1,6)
        if(num == 6):
            count = count + 1
            print(f"Yayyy, numero on {count} kerta heittö jalkeen!")
            break
        else:
            print(f"Numero {num}. Heittää noppaa takaisin!")
            count = count + 1

roll()