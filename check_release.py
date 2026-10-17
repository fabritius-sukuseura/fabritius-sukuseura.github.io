"""Fabritius-sukuseuran julkaisun tekninen tarkistus.

Aja: python check_release.py
Palauttaa virhekoodin 1, jos julkaisuun jää vanhan sivuston riippuvuuksia,
puuttuvia paikallisia resursseja tai epäilyttäviä sivuston sisäisiä linkkejä.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parent
LEGACY = ('nettisivu.org', 'fabritiusry.nettisivu.org')

class References(HTMLParser):
    def __init__(self):
        super().__init__(); self.refs=[]
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        for field in (('href',) if tag in ('a','link') else ('src',) if tag in ('img','script','source') else ()):
            if a.get(field): self.refs.append((tag,a[field]))

def main():
    errors=[]; legacy=[]; checks=0
    for page in sorted(ROOT.rglob('*.html')):
        parser=References(); parser.feed(page.read_text(encoding='utf-8'))
        for tag,ref in parser.refs:
            checks+=1
            url=urlsplit(ref)
            if any(x in url.netloc.lower() for x in LEGACY) or any(x in ref.lower() for x in LEGACY):
                legacy.append(f'{page.relative_to(ROOT)}: {ref}')
            if url.scheme in ('https','http','mailto','tel','data') or ref.startswith('//') or ref.startswith('#'):
                continue
            if url.scheme:
                errors.append(f'{page.relative_to(ROOT)}: tunnistamaton linkki {ref}')
                continue
            target=(page.parent / unquote(url.path)).resolve() if url.path else page
            if not target.is_relative_to(ROOT) or not target.exists():
                errors.append(f'{page.relative_to(ROOT)}: puuttuu {ref}')
    print(f'Tarkistettu {len(list(ROOT.rglob("*.html")))} HTML-tiedostoa, {checks} viittausta.')
    print(f'Vanhan sivuston viittauksia: {len(legacy)}; puuttuvia/virheellisiä: {len(errors)}')
    for issue in legacy: print('VANHA:', issue)
    for issue in errors: print('VIRHE:', issue)
    if legacy or errors:
        print('JULKAISU ESTETTY: korjaa viittaukset tai siirrä aineisto ensin.')
        return 1
    print('Tekninen linkkitarkistus hyväksytty. Sisällön oikeellisuus tarkistettava erikseen.')
    return 0

if __name__=='__main__': raise SystemExit(main())
