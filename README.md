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
