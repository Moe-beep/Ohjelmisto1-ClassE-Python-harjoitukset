import random

heittö = int(input("Kuinka monta kertaa pitaisi heittää noppaa? "))

def roll(heittö):
    for i in range(heittö):
        num = random.randint(1,6)
        print(f"Nopan silmäluku on {num}")
    print(f"Heitti noppaa {num} kertaa!")

roll(heittö)