korkeus = int(input("Anna korkeus"))
blank = korkeus -1
star = 1

while korkeus > 0:
    print(" " * blank + "*" *star )
    blank = blank -1
    star = star + 2
    korkeus = blank