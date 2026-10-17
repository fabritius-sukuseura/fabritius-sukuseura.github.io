"""Sisällön julkaisuportti: tekniset merkkijonot, ei korvaa ihmisen hyväksyntää."""
from pathlib import Path
import sys
root=Path(__file__).parent
pages={p.name:p.read_text(encoding='utf-8') for p in root.glob('*.html')}
errors=[]
for name,text in pages.items():
    if 'nettisivu.org' in text.lower(): errors.append(f'{name}: vanha domain')
    for marker in ('href="https://fabritiusry.', 'src="https://fabritiusry.'):
        if marker in text.lower(): errors.append(f'{name}: vanha riippuvuus')
if 'tietosuojaseloste.html' not in pages: errors.append('tietosuojaseloste puuttuu')
for name in ('sukuseura.html','yhteystiedot.html'):
    if name not in pages: errors.append(f'{name} puuttuu')
print('Sisältöportti:', 'OK' if not errors else 'ESTETTY')
for issue in errors: print('VIRHE:', issue)
print('HUOM: tietosuoja-, lomake-, henkilötieto- ja yhteystietotarkistus vaatii erillisen hyväksynnän.')
sys.exit(bool(errors))
