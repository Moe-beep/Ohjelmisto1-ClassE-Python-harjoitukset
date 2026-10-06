# Tämä ei ole lopullinen Readme-tiedosto, vaan ainoastaan ​​luonnos tai idea siitä.
# Peliprojekti(pelasta valtameri)
Kuten pelin nimi kertoo, sen teemana on merten pelastaminen, mikä liittyy YK:n kestävän kehityksen tavoitteeseen numero 14 (vedenalainen elämä). Pelissä pelaaja suorittaa kolme erilaista skenaariota merten pelastamiseksi: hän voi esimerkiksi kerätä roskia veneellä, taistella hirviöitä vastaan ​​sukellusveneellä tai torjua merirosvoja haiystäviensä avulla. Peli yhdistää leppoisan tunnelman ja jännittävät kohtaamiset.

## koodit
### Pääpeli
Pääpeli sijaitsee tiedostossa nimeltä Projekti.py.
Tiedosto sisältää muun muassa silmukoita sekä syötteen käsittelyyn ja tallennukseen liittyvää koodia.
Kun pelaaja on syöttänyt nimensä ja ikänsä, hän voi valita kolmen eri pelivaihtoehdon välillä.
Viimeisessä while-silmukassa kutsutaan useita funktioita, kuten boat_task ja submarine_task; nämä funktiot on sijoitettu erilliseen Functions-nimiseen kansioon.

### functions kansio
Tässä kansiossa on viisi tiedostoa: __input__.py, boat.py, common.py, shark.py ja submarine.py.
Tiedostot boat.py, shark.py ja submarine.py sisältävät itse pelissä käytettäviä funktioita.
Tiedostossa common.py on metodeja ja luokka, joita kaikki muut tiedostot käyttävät.

### Tallennustoiminto
Jokaisen syötteen jälkeen pelatun pelin tiedot kirjoitetaan save.txt-tiedostoon.
