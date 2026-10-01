class julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi
        self.is_in_citation = False
        self.on_lainassa = False

    def tulosta_tiedot(self):
        if self.on_lainassa:
            laina = "Lainassa"
        else:
            laina = "Saatavilla"

        if self.is_in_citation:
            lainaus = "Kyllä"
        else:
            lainaus = "Ei"

        return f"Nimi: {self.nimi}\nLainassa: {laina}\nLainauksessa: {lainaus}"


class kirja(julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        tiedot = super().tulosta_tiedot()
        return f"{tiedot}\nKirjoittaja: {self.kirjoittaja}\nSivumäärä: {self.sivumäärä}"


class lehti(julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        tiedot = super().tulosta_tiedot()
        return f"{tiedot}\nPäätoimittaja: {self.päätoimittaja}"


# Julkaisut
lehti1 = lehti("Helsingin Sanomat", "Päätoimittaja1")
kirja1 = kirja("Python-ohjelmointi", "Kirjoittaja1", 300)

# Muutetaan tietoja pääohjelmassa
lehti1.is_in_citation = True
kirja1.on_lainassa = True

# Kaikki julkaisut listaan
julkaisut = [lehti1, kirja1]

# Tulostetaan tiedot ja kirjoitetaan tiedostoon
with open("library.txt", "w") as tiedosto:
    for julkaisu in julkaisut:
        tiedot = julkaisu.tulosta_tiedot()
        print(tiedot)
        print()
        tiedosto.write(tiedot + "\n\n")