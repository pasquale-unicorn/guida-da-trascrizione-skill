#!/usr/bin/env python3
"""Estrazione meccanica di slide in PDF: testo e immagine di ogni pagina.

Uso: estrai-pdf-slide.py <file.pdf> <cartella-uscita>

Produce in <cartella-uscita> lo stesso formato di estrai-pptx.py:
  img/sNNN.png         una PNG per pagina (NNN = numero di pagina, 110 dpi)
  indice-slide.md      per pagina: titolo (prima riga di testo), testo, immagine
  immagini.txt         elenco delle immagini, per foglio-immagini.py

Differenze dal pptx: un PDF non ha note del relatore (l'indice lo dice) né video.
Richiede poppler (pdftotext, pdftoppm, pdfinfo) e la sola libreria standard di Python.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

DPI = 110
SENZA_TITOLO = "(senza titolo)"


def esegui(comando: list[str]) -> str:
    try:
        risultato = subprocess.run(comando, check=True, capture_output=True, text=True)
    except FileNotFoundError:
        sys.exit(f"Manca {comando[0]}. Installa: brew install poppler")
    except subprocess.CalledProcessError as errore:
        sys.exit(f"{comando[0]} ha fallito: {errore.stderr.strip()}")
    return risultato.stdout


def numero_pagine(pdf: Path) -> int:
    trovato = re.search(r"^Pages:\s+(\d+)", esegui(["pdfinfo", str(pdf)]), re.MULTILINE)
    if not trovato:
        sys.exit(f"pdfinfo non riporta il numero di pagine: {pdf} è un PDF valido?")
    return int(trovato.group(1))


def testo_pagina(pdf: Path, pagina: int) -> list[str]:
    grezzo = esegui(["pdftotext", "-layout", "-enc", "UTF-8",
                     "-f", str(pagina), "-l", str(pagina), str(pdf), "-"])
    righe = (" ".join(riga.split()) for riga in grezzo.replace("\f", "").splitlines())
    return [riga for riga in righe if riga]


def immagine_pagina(pdf: Path, pagina: int, img: Path) -> str:
    nome = f"s{pagina:03d}"
    esegui(["pdftoppm", "-r", str(DPI), "-png", "-singlefile",
            "-f", str(pagina), "-l", str(pagina), str(pdf), str(img / nome)])
    return f"{nome}.png"


def estrai(sorgente: Path, uscita: Path) -> None:
    img = uscita / "img"
    img.mkdir(parents=True, exist_ok=True)
    totale = numero_pagine(sorgente)
    righe = [f"# Indice delle slide — {sorgente.name}", "",
             "Una slide per pagina del PDF; testo estratto con pdftotext senza interpretazione. "
             "Un PDF non contiene le note del relatore: il pensiero del relatore sta solo nelle trascrizioni.", "",
             f"Slide: {totale} · Immagini estratte: {totale}", ""]
    nomi, senza_testo = [], 0
    for pagina in range(1, totale + 1):
        testo = testo_pagina(sorgente, pagina)
        senza_testo += not testo
        nome = immagine_pagina(sorgente, pagina, img)
        nomi.append(nome)
        righe += [f"## Slide {pagina:03d} — {testo[0] if testo else SENZA_TITOLO}", "", "### Testo", ""]
        righe += [f"- {riga}" for riga in testo] or ["(nessun testo)"]
        righe += ["", "### Note relatore", "", "(nessuna nota: il PDF non le contiene)",
                  "", "### Immagini", "", f"- `img/{nome}`", "", "Video: no", ""]
    (uscita / "indice-slide.md").write_text("\n".join(righe), encoding="utf-8")
    (uscita / "immagini.txt").write_text("\n".join(nomi) + "\n", encoding="utf-8")
    print(f"{totale} slide, {len(nomi)} immagini estratte, {senza_testo} slide senza testo "
          f"(solo immagine: controllale a mano)")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    sorgente_pdf = Path(sys.argv[1])
    if not sorgente_pdf.is_file():
        sys.exit(f"file non trovato: {sorgente_pdf}")
    estrai(sorgente_pdf, Path(sys.argv[2]))
