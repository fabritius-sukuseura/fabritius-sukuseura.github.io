# Sisällön siirron tilanne — 2026-10-17

## Julkaisun ehdoton hyväksymisehto
Lopullisessa julkaistussa sivustossa ei ole linkkejä, kuvia, lomakkeita, tiedostoja eikä muita teknisiä riippuvuuksia vanhasta `nettisivu.org`-sivustosta.

`python check_release.py` tarkistaa HTML:n sisäiset linkit, kuvien ja skriptien polut sekä viittaukset vanhaan domainiin. Julkaisuun kelpaavan version on läpäistävä se virheittä. Tarkistus ei yksin todista sisällön täydellisyyttä eikä henkilötietojen oikeellisuutta.

## Tämänhetkinen tilanne (develop)
- Sääntösivu: paikallinen tiivistelmä, alkuperäinen sääntöteksti ei kokonaisuudessaan tallessa. 8 § puuttuu nykyisen julkisen lähdetekstin numeroinnista. Älä keksi puuttuvaa sisältöä.
- Historia ja sukututkimus: paikalliset tiivistelmät, osa alkuperäisistä teksteistä edelleen muualla.
- Kokoukset: 17 vuosittaista kohdetta listattu, mutta yksityiskohtaiset kertomukset ja kuvat ovat vielä vanhassa palvelussa.
- Jäsenmaksulomake: ei vielä paikallista PDF-tiedostoa.
- Sukurekisteri: vanha verkkolomake ja tietosuojaseloste eivät vielä ole itsenäisinä paikallisina sisältöinä.
- Yhteystiedot: ajantasaisuus on erikseen hyväksyttävä.

## Siirtotyön järjestys
1. Kokousarkiston kertomukset ja valokuvat talteen paikallisiin tiedostoihin; tarkista kuvien käyttöoikeudet ja henkilöiden tietosuoja.
2. Alkuperäinen sääntöteksti talteen paikalliseksi sisällöksi, julkaistun lähteen epävarmuus selkeästi ilmoittaen.
3. Historia- ja tutkimustekstit täydellisiksi, ilman tyhjiä viittauksia.
4. Jäsenmaksu ja yhteystietojen asiakirjat: siirrä PDF:t tai korvaa turvallisilla itsenäisillä ohjeilla.
5. Poista kaikki vanhat domain-linkit ja aja `python check_release.py`.
6. Tarkista sivujen sisällöt ja vasta sen jälkeen yhdistä develop -> main ja ota Pages käyttöön.

Älä siirrä jäsenrekisterin henkilötietoja julkiseen repositorioon.
