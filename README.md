# Fabritius-sukuseura ry – verkkosivut

**Tila: v1.0 julkaistu 17.10.2026.**

- Sivusto: https://fabritius-sukuseura.github.io/
- Teknologia: staattinen HTML, CSS ja JavaScript
- Julkaisu: GitHub Pages, `main`-haara, `/ (root)`
- Ylläpito: yksi ylläpitäjä GitHubin kautta; maksullista hostingia ei tarvita

## Sisältö

- `index.html` – etusivu
- `sukuseura.html` ja `saannot.html` – yhdistyksen toiminta, jäsenmaksu ja säännöt
- `historia.html` ja `tutkimus.html` – suvun historia ja sukututkimus
- `kokoukset.html` ja `kokoukset/` – 17 kokoussivua vuosilta 2004–2025
- `ajankohtaista.html` – ajankohtaiset asiat
- `yhteystiedot.html` ja `tietosuojaseloste.html` – hallitus ja tietosuoja
- `assets/` – vaakuna, kuvitus, tyylit, JavaScript ja 101 kokouskuvaa

Osa etusivun kuvituksesta on havainnollistavaa, ei historiallista valokuva-aineistoa.

## Muutosten tekeminen

1. Muokkaa ja testaa uudet sisällöt `develop`-haarassa.
2. Aja ennen julkaisua:

   ```powershell
   python check_release.py
   python check_content_v13.py
   python check_decisions_v14.py
   ```

3. Tarkista lopputulos selaimessa tietokone- ja mobiilikoossa.
4. Siirrä hyväksytty versio `main`-haaraan ilman pakotettua päivitystä.
5. GitHub Pages julkaisee `main`-haaran juurihakemistosta.

Testiskriptit eivät korvaa tietosuojan, kuvaoikeuksien ja aineistojen sisällöllistä tarkistusta.

## Ensimmäisen julkaisun päätökset

- Hyväksytty vihreä-kultainen ulkoasu ja Fabritius-vaakuna.
- Hallituksen neljä nimeä ja tehtävää on vahvistettu 17.10.2026.
- Kokousarkiston 101 kuvan julkaisu on hyväksytty 17.10.2026.
- Vuoden 2026 jäsenmaksu on 30 euroa perheeltä. Tilinumero ja maksun viite lisätään vain erillisen vahvistuksen jälkeen.
- Sukurekisterin lomaketta ei julkaista tässä vaiheessa.
- Tietosuojaselosteen 5.5.2022 teksti säilytetään, ja ajantasaisuus tarkistetaan myöhemmin.
- Sivuston HTML-tiedostot eivät sisällä riippuvuuksia vanhaan verkkosivupalveluun.

## Jatkokehitys

- Jäsenmaksun vahvistetut maksutiedot haluttaessa.
- Tietosuojaselosteen päivittäminen.
- Sukurekisterin turvallisen tiedonkeruun suunnittelu tarvittaessa.
- Uutisten ja sukututkimuksen linkkien laajentaminen.
- Kokousten 2021, 2023 ja 2025 täydentäminen, jos alkuperäistä lisäaineistoa löytyy.
- Sääntöjen mahdollisen uudemman vahvistetun version tarkistus (julkaistussa lähdetekstissä 8 § puuttuu).

Tarkempi julkaisu- ja siirtopöytäkirja: [`CONTENT_MIGRATION.md`](CONTENT_MIGRATION.md).


## Päivitys v1.2 – etusivu, Facebook ja kokousarkisto (17.10.2026)

- Julkaistu sivustoversio: `b90cc6e8af1994f82b0e45f2b5d14bf5a940d694`.
- Etusivun suuri otsikko ja hero-osion korkeus pienennettiin v1.1-päivityksessä; alkuperäinen vasemmanpuoleinen sisältö säilytettiin.
- Etusivulle lisättiin näkyvä Facebook-linkki oikealle. Sama linkki löytyy Yhteystiedot-sivulta: https://fi-fi.facebook.com/people/Fabritius-Sukuseura-ry/100064779093875/
- Kokousarkiston ja sääntösivun toimituksellisia huomautuslaatikoita poistettiin.
- Vuosien 2021 ja 2023 kokoussivuille lisättiin kartanokuvat; vuoden 2021 kertomusta täydennettiin käyttäjän toimittamalla tekstillä.
- Vuosien 2021, 2023 ja 2025 kokoussivuilta poistettiin puuttuvasta aineistosta kertovia huomautuksia.
- Käyttäjä hyväksyi korjatun etusivun selaimessa; muutos julkaistiin `main`-haaraan.
- Ennen julkaisua automaattiset tarkistukset läpäistiin: 26 HTML-tiedostoa, 589 viittausta, 0 vanhaa sivustoviittausta ja 0 puuttuvaa resurssia.

Julkaisuun liittyvät hyväksynnät eivät ole lupaus kaikkien alkuperäisten arkistoaineistojen täydellisyydestä. Mahdolliset lisäaineistot lisätään myöhemmin erillisinä muutoksina.

## v1.3 – Tekstikorjaukset ja FamilySearch-linkki (17.10.2026)

- Julkaistu `main`-haaraan commitissa `1a765129927660d6273a93ded8f1a53f49550765`.
- Yhteystiedot-sivulta poistettiin GitHub-repositorion ja Issues-keskustelujen käyttöä koskeva lause. Sukurekisterin yhteydenotto-ohje jäi ennalleen.
- Tietosuojaselosteen yläosan väliaikainen huomautuslaatikko poistettiin. Alkuperäinen 5.5.2022 päivätty tietosuojaseloste säilytettiin.
- Ajankohtaista-sivun väliaikaisen ilmoituksen tilalle lisättiin tieto kahden vuoden kokousvälistä ja kesän 2027 kokouksesta.
- Sukututkimus-sivulle lisättiin FamilySearch-linkki Carl Fabritiuksen lapsiluettelon alle.
- `check_decisions_v14.py` muutettiin tarkistamaan tietosuojaselosteen alkuperäisen sisällön säilyminen poistetun väliaikaismerkinnän sijaan.
- `check_release.py`, `check_content_v13.py` ja `check_decisions_v14.py` hyväksytty; 26 HTML-tiedostoa, 590 viittausta, 0 puuttuvaa paikallista resurssia ja 0 viittausta vanhaan palveluun.
- Käyttäjän hyväksymät tekstimuutokset julkaistu ilman muita ulkoasu- tai sisältömuutoksia.
