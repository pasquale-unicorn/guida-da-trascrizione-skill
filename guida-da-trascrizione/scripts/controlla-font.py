#!/usr/bin/env python3
"""Controlla i font di un PDF: tutti Montserrat (o la famiglia indicata) e tutti incorporati.

Uso: controlla-font.py <file.pdf> [famiglia]     (famiglia di default: Montserrat)
Esce con 1 se trova un font diverso o non incorporato. Chrome stampa prima che i web font
carichino se il font non è incorporato nel CSS: questo controllo lo scopre.
"""
import subprocess
import sys


def colonne(intestazione_trattini):
    """pdffonts allinea le colonne a larghezza fissa: le misura dalla riga di trattini."""
    posizioni, inizio = [], None
    for i, c in enumerate(intestazione_trattini + " "):
        if c == "-" and inizio is None:
            inizio = i
        elif c != "-" and inizio is not None:
            posizioni.append((inizio, i))
            inizio = None
    return posizioni


def main():
    if len(sys.argv) not in (2, 3):
        sys.exit(__doc__)
    pdf, famiglia = sys.argv[1], (sys.argv[2] if len(sys.argv) == 3 else "Montserrat")
    uscita = subprocess.run(["pdffonts", pdf], capture_output=True, text=True, check=True).stdout
    righe = uscita.splitlines()
    if len(righe) < 3:
        sys.exit(f"{pdf}: nessun font trovato (PDF solo immagini?)")
    pos = colonne(righe[1])
    intestazioni = [righe[0][a:b + 1].strip() for a, b in pos]
    i_nome, i_emb = intestazioni.index("name"), intestazioni.index("emb")
    problemi = []
    for riga in righe[2:]:
        campi = [riga[a:b + 1].strip() for a, b in pos]
        nome, incorporato = campi[i_nome], campi[i_emb]
        if famiglia.lower() not in nome.lower():
            problemi.append(f"font estraneo: {nome}")
        if incorporato != "yes":
            problemi.append(f"non incorporato: {nome}")
        print(f"{'OK ' if famiglia.lower() in nome.lower() and incorporato == 'yes' else 'NO '} {nome}")
    if problemi:
        print("\n".join(problemi), file=sys.stderr)
        sys.exit(1)
    print(f"Font OK: solo {famiglia}, tutto incorporato.")


if __name__ == "__main__":
    main()
