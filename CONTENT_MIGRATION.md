# Fabritius-sukuseura – v1.0-julkaisun sisältö- ja päätöspöytäkirja

## Julkaisu

- Päivä: 17.10.2026
- Sivusto: https://fabritius-sukuseura.github.io/
- Hyväksytty sisältöcommit: `fdf9d29`
- Julkaisukanava: GitHub Pages, `main` / `/ (root)`, HTTPS
- Julkaisun selaintestaus (tietokone ja mobiili): käyttäjän hyväksymä
- GitHub Pages -sivuston näkyminen oikeana: käyttäjän vahvistama

## Tekniset hyväksymistulokset

- 26 HTML-tiedostoa ja 585 tarkistettua viittausta
- 17 paikallista kokoussivua ja 101 JPEG-kuvaa
- 0 vanhan palvelun viittausta HTML-tiedostoissa
- 0 puuttuvaa paikallista linkkiä tai resurssia
- `check_release.py`, `check_content_v13.py` ja `check_decisions_v14.py` hyväksytty
- v15-lopputarkistus: 0 automaattista havaintoa
- Kuvista `2006-01.jpg` ja `2007-09.jpg` ovat matalaresoluutioisia, mutta avautuvat.

## Käyttäjän hyväksymät ratkaisut

- Etusivun ulkoasu ja sukuseuran vaakuna hyväksytty.
- Kokouskuvien julkaiseminen hyväksytty.
- Hallituksen tehtävät: puheenjohtaja Markku Fabritius, varapuheenjohtaja Jukka Fabritius, sihteeri Rita Niemi ja rahastonhoitaja Mika Oinas; vahvistettu 17.10.2026.
- Jäsenmaksu vuodelle 2026: 30 euroa/perhe; pankki- ja viitetiedot julkaistaan vain erikseen vahvistettuina.
- Sukurekisterin lomaketta ei julkaista toistaiseksi.
- Tietosuojaselosteen (5.5.2022) teksti säilytetään nykyisellään. Käyttäjä tarkistaa sen ajantasaisuuden myöhemmin.
- Vanhan sivuston viittauksia ei saa olla lopullisessa sivustossa.

## Myöhemmät kehitystehtävät

1. Pankki- ja viitetietojen vahvistaminen sekä mahdollinen julkaisu.
2. Tietosuojaselosteen ja rekisterinpitäjätietojen ajantasaisuuden tarkistus.
3. Sukurekisterin lomake tai turvallinen yhteydenottotapa, jos sitä myöhemmin tarvitaan.
4. Uutisten sekä sukututkimuksen aineisto- ja linkkiosioiden laajentaminen.
5. Vuosien 2021, 2023 ja 2025 kokousaineiston täydentäminen, jos lisämateriaalia saadaan.
6. Yhdistyksen vahvistettujen sääntöjen päivittäminen mahdollisen uuden lähteen perusteella. Alkuperäisessä verkkotekstissä puuttui 8 §.

Nämä ovat jatkokehitystä, eivät v1.0:n teknisiä julkaisun esteitä. Kuvien käyttöoikeuksiin ja tietosuojaan liittyvät velvoitteet säilyvät myös julkaisun jälkeen.

## Työtapa

- `develop`: toteutus ja testaus.
- `main`: hyväksytty julkaisuversio.
- Ennen julkaisua ajetaan testit, tarkistetaan selaimella ja dokumentoidaan muutokset.
- Julkaisu ilman `--force`-päivityksiä.


## Julkaistu päivitys v1.2 – 17.10.2026

- Tuotantoon julkaistu commit: `b90cc6e8af1994f82b0e45f2b5d14bf5a940d694`.
- Julkaisun yhteydessä `main` ja `develop` vastasivat samaa committia.
- Muutokset ennen julkaisua: `cbfe660`, `9fe4480`, `b90cc6e`.
- Etusivun pienennetty otsikko ja matalampi hero-alue säilytetty hyväksytyssä asettelussa. Facebook-kortti oikealla, alkuperäinen otsikko, johdanto ja toimintapainike vasemmalla.
- Facebook-linkki lisätty etusivulle ja Yhteystiedot-sivulle.
- 2021 Sannaisten ja 2023 Backbyn kartanokuvat sisällytetty paikallisina tiedostoina.
- Vuoden 2021 kokouksen kuvausta täydennetty käyttäjän toimittamalla tekstillä.
- Sääntösivun ja kokousarkiston toimituksellisia huomautuksia poistettu. Julkaisussa ei esitetä väitteitä puuttuvista kuvista tai aineistoista.
- Testit ennen julkaisua: 26 HTML-sivua, 589 viittausta, 0 vanhaa sivustoriippuvuutta, 0 puuttuvaa paikallista resurssia; kolme sisältöporttia OK.
- Julkisen etusivun lopullinen ulkoasu hyväksytty ennen main-haaraan siirtoa.
- Avoimet jatkotyöt säilyvät ennallaan (maksutiedot, tietosuojan ajantasaisuus, sukurekisterilomake ja mahdolliset uudet uutiset tai arkistoaineistot).
