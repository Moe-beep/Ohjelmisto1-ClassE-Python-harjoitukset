try:
    jaettava = int(input("Anna jaettava luku: "))
    jakaja = int(input("Anna jakaja: "))
    print("Jakolaskun tulos on: ", jaettava / jakaja)
except ValueError:
    print("Virhe; syöttety arvo ei ole kokkkonaisluku")
except ZeroDivisionError as e:
    print("Errorin nimi", e)