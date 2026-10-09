# Peliprojekti(pelasta valtameri)

Kuten pelin nimi kertoo, sen teemana on merten pelastaminen, mikä liittyy YK:n kestävän kehityksen tavoitteeseen numero 14 (vedenalainen elämä). Pelissä pelaaja suorittaa kolme erilaista skenaariota merten pelastamiseksi: hän voi esimerkiksi kerätä roskia veneellä, taistella hirviöitä vastaan ​​sukellusveneellä tai torjua merirosvoja haiystäviensä avulla. Peli yhdistää leppoisan tunnelman ja jännittävät kohtaamiset.

# Miten peliä pelataan?

Pelin pelaaminen on yksinkertaista: pelaajan täytyy vastata Yes tai No kysymyksiin, sekä kertoa nimensä, ikänsä ja muita tietoja.

Kun peli aloitetaan, jos pelaaja on pelannut peliä aiemmin, hän voi yksinkertaisesti syöttää nimensä ja nähdä, onko hän suorittanut pelin loppuun vai ei. Jos pelaaja on suorittanut pelin loppuun, hän voi jatkaa pelaamista saadakseen lisää suoritettuja tehtäviä, jotka hän voi tarkistaa save.txt-tiedostosta. Jos peliä ei ole suoritettu loppuun, peli alkaa normaalisti.

Pelaajilla on pelissä kolme eri polkua, jotka he voivat pelata läpi. Pitäkää hauskaa!!

## Varo
Tee tiedostolle commit pelaamisen jälkeen, sillä save.txt päivittyy jokaisella pelikerralla ja aiheuttaa virheen, jos muutoksia ei tallenneta versionhallintaan.

# Koodit
## Tiedostojen järjestäminen

Pelissä on yhteensä 9 tiedostoa. **__init__.py**, **boat.py**, **common.py**, **shark.py** ja **submarine.py** sijaitsevat functions-kansiossa. Functions-kansion ulkopuolella ovat tiedostot **info.txt**, **Projekti.py**, **readme.md** ja **save.txt**.

## Functions

Functions-kansion tiedostot sisältävät funktioita, luokkia, listoja ja olioita, joita käytetään **Peliprojekti.py**-tiedostossa. **Common.py**-tiedosto sisältää funktioita, luokkia ja listoja, joita muut tiedostot käyttävät. **Boat.py**, **submarine.py** ja **shark.py** sisältävät kukin omaan pelattavuuteensa liittyviä funktioita, joihin viitataan **Peliprojekti.py**-tiedostossa.

**save.txt**-tiedostoon tallennetaan ja kirjataan jokainen pelaajan pelaama peli. Tämä toteutetaan käyttämällä ja hyödyntämällä **common.py**-tiedostossa olevia funktioita. Tallentamiseen liittyvät funktiot on kirjoitettu rivin **#SAVE GAME** alle. Funktio, jolla luetaan ja ladataan, mihin pelaaja on viimeksi jäänyt, on **check_name(name)**.

Tiedostossa **info.txt** on rivejä, joita käytetään venepelissä.

# Lähteet

**common.py**-tiedoston **check_name**-funktiossa käytetty enumerate-silmukka indeksin kanssa on otettu lähteestä <https://realpython.com/python-enumerate/>, jossa selitetään, kuinka luodaan silmukoita, jotka tarvitsevat laskentaa.


# Tekoälyn käyttö

Tekoälyä käytetään ainoastaan virheenkorjaukseen, kuten kirjoitusvirheiden etsimiseen, koska se säästää aikaa, kun pientä kirjoitusvirhettä ei tarvitse etsiä koko koodista.
