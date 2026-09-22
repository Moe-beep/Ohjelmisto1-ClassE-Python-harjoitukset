## Moduuli11 - teht'v' 1
## Luokka julkaisu, jonka aliluokat ovat kirja ja lehti perivät
## Julkaisulla on nimi
## Kirjalla kirjoittaja ja sivumäärä
## Lehdellä päätoimittaja
## methodi tulosta?tiedot joka tulostaa kaikki julkaisun tiedot

class julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}")

class kirja(julkaisu):
    def __init__(self,nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjoittaja: {self.kirjoittaja}")
        print(f"Sivumäärä: {self.sivumäärä}")

class lehti(julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Päätoimittaja: {self.päätoimittaja}")

lehti1 = lehti("Helsingin Sanomat", "Päätoimittaja1")
lehti1.tulosta_tiedot()

kirja1 = kirja("Python-ohjelmointi", "Kirjoittaja1", 300)
kirja1.tulosta_tiedot()