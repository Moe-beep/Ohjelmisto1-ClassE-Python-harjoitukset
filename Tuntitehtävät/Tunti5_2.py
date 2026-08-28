print("Maria oli rohkea ritari, joka joutui kaksintaisteluun, Minkä aseeen maria ottaa?")

thing = ""

while thing != "meikka":
    
    thing = input(str())
    if(thing != "meikka"):
        print("Ei kannata, se on huono ase. Anna toinen ase!!")
    else:
        print("Meikalla Maria voittaa varmasti!")