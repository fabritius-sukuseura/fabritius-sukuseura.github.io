"""Check technical compliance with 17 Oct 2026 publication decisions."""
from pathlib import Path
root=Path(__file__).parent
membership=(root/'sukuseura.html').read_text(encoding='utf-8')
contact=(root/'yhteystiedot.html').read_text(encoding='utf-8')
privacy=(root/'tietosuojaseloste.html').read_text(encoding='utf-8')
errors=[]
if membership.count('Vuoden 2026 jäsenmaksu on 30 euroa perheeltä') != 1: errors.append('member fee missing or duplicated')
if 'Tilinumero ja maksun viitetiedot julkaistaan' not in membership: errors.append('payment guidance missing')
if 'ei ole verkkolomaketta tai ladattavaa lomaketta' not in contact: errors.append('registry form decision missing')
if 'Laadittu 5.5.2022' not in privacy: errors.append('privacy document date missing')
if 'EU:n yleisen tietosuoja-asetuksen 13 ja 14 artiklan mukainen tietosuojaseloste.' not in privacy: errors.append('original privacy text missing')
print('V14 päätöstarkistus:', 'OK' if not errors else ', '.join(errors))
raise SystemExit(bool(errors))
