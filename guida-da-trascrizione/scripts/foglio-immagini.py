#!/usr/bin/env python3
"""Contact sheet delle immagini: griglie da 12 miniature con il nome del file sotto.

Uso: foglio-immagini.py <cartella-slide>
Legge <cartella-slide>/immagini.txt (scritto da estrai-pptx.py) oppure, se manca, tutte le immagini
di <cartella-slide>/img/. Scrive <cartella-slide>/contact/foglio-NNN.png.

Serve a chi viene dopo per GUARDARE le foto in fretta (un Read per 12 immagini) e scegliere
quelle vere e nitide. Usa Chrome headless per lo screenshot (variabile CHROME per un percorso diverso
da quello macOS): niente librerie Python esterne.
"""

import html
import os
import subprocess
import sys
import tempfile
from pathlib import Path

PER_FOGLIO = 12
COLONNE = 4
LARGHEZZA, ALTEZZA = 1200, 940
ESTENSIONI = (".png", ".jpg", ".jpeg", ".gif", ".webp")
CHROME_MAC = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

PAGINA = """<!doctype html><meta charset="utf-8"><style>
body{{margin:0;background:#fff;font:600 13px Menlo,monospace}}
.g{{display:grid;grid-template-columns:repeat({colonne},minmax(0,1fr));gap:6px;padding:6px}}
figure{{margin:0;height:300px;display:flex;flex-direction:column;border:1px solid #ccc;min-width:0}}
img{{display:block;width:100%;height:265px;object-fit:contain;background:#f3f3f3}}
figcaption{{padding:4px;text-align:center}}
</style><div class="g">{celle}</div>"""


def immagini(cartella):
    elenco = cartella / "immagini.txt"
    if elenco.exists():
        nomi = [r.strip() for r in elenco.read_text(encoding="utf-8").splitlines() if r.strip()]
    else:
        nomi = sorted(p.name for p in (cartella / "img").iterdir() if p.suffix.lower() in ESTENSIONI)
    # le copie -web sono solo versioni ridotte: niente doppioni nel foglio
    return [n for n in nomi if not n.endswith("-web.jpg")]


def screenshot(chrome, pagina_html, destinazione):
    subprocess.run([chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    f"--window-size={LARGHEZZA},{ALTEZZA}", "--virtual-time-budget=5000",
                    f"--screenshot={destinazione}", pagina_html.as_uri()],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    cartella = Path(sys.argv[1]).resolve()
    chrome = os.environ.get("CHROME") or (CHROME_MAC if Path(CHROME_MAC).exists() else "google-chrome")
    nomi = immagini(cartella)
    if not nomi:
        sys.exit(f"nessuna immagine in {cartella / 'img'}")
    uscita = cartella / "contact"
    uscita.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        for i in range(0, len(nomi), PER_FOGLIO):
            gruppo = nomi[i:i + PER_FOGLIO]
            celle = "".join(
                f'<figure><img src="{(cartella / "img" / n).as_uri()}">'
                f"<figcaption>{html.escape(n)}</figcaption></figure>" for n in gruppo)
            pagina = Path(tmp) / f"foglio-{i // PER_FOGLIO + 1:03d}.html"
            pagina.write_text(PAGINA.format(colonne=COLONNE, celle=celle), encoding="utf-8")
            screenshot(chrome, pagina, uscita / f"foglio-{i // PER_FOGLIO + 1:03d}.png")
    print(f"{len(nomi)} immagini in {-(-len(nomi) // PER_FOGLIO)} fogli: {uscita}")


if __name__ == "__main__":
    main()
