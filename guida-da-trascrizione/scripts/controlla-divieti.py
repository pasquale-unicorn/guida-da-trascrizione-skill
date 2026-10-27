#!/usr/bin/env python3
"""Cerca nei testi e nei PDF le cose che non devono restare nel prodotto finale.

Uso: controlla-divieti.py <file...> [--parole "nome1,nome2,corso,..."]

Funziona su .md/.txt/.html e su .pdf (via pdftotext). Cerca sempre:
  timestamp tipo 01:23:45, marcatori rimasti [[...]], "Speaker N", TODO/segnaposto/lorem ipsum.
Con --parole aggiunge le parole vietate decise in pianificazione (nomi dei relatori, mesi e anno
dell'evento, "corso", "docente", "in aula"...). Confronto senza maiuscole, a parola intera.

Attenzione ai falsi positivi: parole spezzate a fine riga nel PDF, sottostringhe in parole più
lunghe, orari legittimi nel contenuto (es. "check-in dalle 15:00" non è un timestamp a tre campi).
Ogni riga segnalata va guardata, non corretta alla cieca. Esce con 1 se trova qualcosa.
"""
import re
import subprocess
import sys
from pathlib import Path

SEMPRE = {
    "timestamp": r"\b\d{1,2}:\d{2}:\d{2}\b",
    "marcatore rimasto": r"\[\[|\]\]",
    "parlante anonimo": r"\bSpeaker\s*\d+\b",
    "segnaposto": r"\bTODO\b|\bsegnaposto\b|lorem ipsum|\bXXX\b",
}


def testo(file):
    if file.suffix.lower() == ".pdf":
        return subprocess.run(["pdftotext", "-layout", str(file), "-"],
                              capture_output=True, text=True, check=True).stdout
    return file.read_text(encoding="utf-8", errors="replace")


def regole(parole):
    tutte = dict(SEMPRE)
    for p in parole:
        tutte[f"parola vietata «{p}»"] = r"(?<!\w)" + re.escape(p) + r"(?!\w)"
    return {nome: re.compile(rx, re.I) for nome, rx in tutte.items()}


def main():
    argomenti = sys.argv[1:]
    parole = []
    if "--parole" in argomenti:
        i = argomenti.index("--parole")
        parole = [p.strip() for p in argomenti[i + 1].split(",") if p.strip()]
        argomenti = argomenti[:i] + argomenti[i + 2:]
    if not argomenti:
        sys.exit(__doc__)
    controlli = regole(parole)
    trovati = 0
    for nome_file in argomenti:
        file = Path(nome_file)
        for n, riga in enumerate(testo(file).splitlines(), 1):
            for nome, rx in controlli.items():
                if rx.search(riga):
                    trovati += 1
                    print(f"{file.name}:{n}: {nome}: {riga.strip()[:140]}")
    if trovati:
        print(f"{trovati} righe da guardare", file=sys.stderr)
        sys.exit(1)
    print("Divieti OK: nessuna occorrenza.")


if __name__ == "__main__":
    main()
