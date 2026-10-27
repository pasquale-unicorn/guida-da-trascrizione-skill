#!/usr/bin/env python3
"""Assembla il manuale finale dai frammenti impaginati delle parti.

  assembla.py <progetto> html       scrive finale/<file>.html (indice con i numeri di finale/pagine.json)
  assembla.py <progetto> pagine     legge finale/<file>.pdf, trova la pagina di ogni parte e capitolo,
                                    aggiorna pagine.json; esce con 0 se i numeri non sono cambiati
  assembla.py <progetto> prova N    scrive finale/prova-parte-N.html (solo la parte N) per la stampa di prova

Configurazione in <progetto>/finale/manuale.json:
  {"titolo": "Titolo del manuale", "file": "Manuale", "parti": 4,
   "design": "../design/definitivo", "lato_max_per": {"logo-unicorn-nero.png": 600}}

Convenzioni dei frammenti finale/parte-N.html (+ parte-N.css facoltativo), come in assets/COMPONENTI.md:
  <section class="apertura"> ... <h1>Titolo parte</h1>
  <article class="capitolo ..."> ... <p class="occhiello">Capitolo 7</p> <h1>Titolo capitolo</h1>

Perché due passate: target-counter() non funziona in Chrome, quindi l'indice si compila stampando,
cercando con pdftotext la pagina di ogni titolo e ristampando finché i numeri non cambiano (build.sh).
Richiede macOS (usa `sips` per ridimensionare le immagini) e poppler (`pdftotext`, `pdfinfo`).
L'HTML finale incorpora le immagini come data URI: funziona anche copiato da solo su un altro computer.
"""
import base64
import html
import json
import os
import re
import subprocess
import sys
from pathlib import Path

SEGNAPOSTO = "·"
PRIMA_PAGINA_CONTENUTO = 3      # 1 = copertina, 2 = indice
TITOLO_CSS = "TITOLO DEL MANUALE"  # segnaposto del piè di pagina in stile.css
LATO_MAX = 1600                 # px, lato lungo delle immagini incorporate
JPEG_QUALITA = 80
JPEG_INTATTO_MAX = 200 * 1024   # JPEG sotto questo peso e sotto LATO_MAX restano come sono
MIME = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".svg": "image/svg+xml"}
RE_CAPITOLO = r'<p class="occhiello">Capitolo ([\d.]+)</p>\s*<h1>(.*?)</h1>'

INDICE_CSS = """
/* Indice del manuale assemblato: voci cliccabili, fitte per stare in una pagina. */
a.indice-titolo, a.indice-riga { color: inherit; text-decoration: none; }
.indice .indice-parte { margin-bottom: 1.6mm; padding-top: 1.6mm; padding-bottom: .8mm; }
.indice .indice-titolo { margin-bottom: .8mm; }
.indice .indice-riga { padding: .25mm 0; font-size: 9pt; line-height: 1.3; }
.indice .indice-riga .num { min-width: 6.5mm; font-weight: 700; color: var(--viola-medio); }
.indice .indice-riga .pag { align-self: flex-end; }
"""


class Progetto:
    def __init__(self, cartella):
        self.finale = Path(os.path.abspath(cartella)) / "finale"
        config_file = self.finale / "manuale.json"
        if not config_file.exists():
            sys.exit(f"manca {config_file} (vedi la docstring per il formato)")
        config = json.loads(config_file.read_text(encoding="utf-8"))
        self.titolo = config["titolo"]
        self.parti = int(config["parti"])
        self.design = Path(os.path.normpath(self.finale / config.get("design", "../design/definitivo")))
        self.lato_max_per = config.get("lato_max_per", {})
        nome = config.get("file", "Manuale")
        self.html_out = self.finale / f"{nome}.html"
        self.pdf_out = self.finale / f"{nome}.pdf"
        self.pagine_json = self.finale / "pagine.json"
        self.img_cache = self.finale / "_img-incorporate"


def leggi(percorso):
    return Path(percorso).read_text(encoding="utf-8")


def testo_pulito(frammento):
    senza_br = re.sub(r"<br\s*/?>", " ", frammento)
    senza_tag = re.sub(r"<[^>]+>", "", senza_br)
    return " ".join(html.unescape(senza_tag).split())


def id_capitolo(numero):
    return "cap-" + numero.replace(".", "-")


def con_id(testo_parte, numero_parte):
    """Aggiunge id ad apertura e capitoli dove mancano (non cambia testo né impaginazione)."""
    def apertura(m):
        tag = m.group(0)
        return tag if " id=" in tag else tag.replace("<section", f'<section id="parte-{numero_parte}"', 1)

    testo_parte = re.sub(r'<section class="apertura"[^>]*>', apertura, testo_parte, count=1)
    pezzi = re.split(r'(<article class="capitolo[^>]*>)', testo_parte)
    risultato = [pezzi[0]]
    for tag, corpo in zip(pezzi[1::2], pezzi[2::2]):
        trovato = re.search(r'<p class="occhiello">Capitolo ([\d.]+)</p>', corpo)
        if trovato is None:
            sys.exit(f"parte {numero_parte}: capitolo senza <p class=\"occhiello\">Capitolo N</p>")
        if " id=" not in tag:
            tag = tag.replace("<article", f'<article id="{id_capitolo(trovato.group(1))}"', 1)
        risultato.extend([tag, corpo])
    return "".join(risultato)


def carica_parte(prog, n):
    file = prog.finale / f"parte-{n}.html"
    if not file.exists():
        sys.exit(f"frammento mancante: {file}")
    corpo = con_id(leggi(file), n)
    apertura = re.search(r'<section[^>]*class="apertura"[^>]*>.*?<h1>(.*?)</h1>', corpo, re.S)
    if apertura is None:
        sys.exit(f"parte {n}: manca <section class=\"apertura\"> con <h1>")
    capitoli = [(m.group(1), testo_pulito(m.group(2))) for m in re.finditer(RE_CAPITOLO, corpo, re.S)]
    return {"numero": n, "titolo": testo_pulito(apertura.group(1)), "capitoli": capitoli, "html": corpo}


def carica_parti(prog):
    return [carica_parte(prog, n) for n in range(1, prog.parti + 1)]


def esempio_design(prog):
    file = prog.design / "index.html"
    if not file.exists():
        sys.exit(f"manca {file}: serve per copertina e sprite delle frecce")
    return leggi(file)


def copertina(prog):
    blocco = re.search(r'<section class="copertina">.*?</section>', esempio_design(prog), re.S)
    if blocco is None:
        sys.exit("nessuna <section class=\"copertina\"> nell'index.html del design")
    relativo = Path(os.path.relpath(prog.design, prog.finale)).as_posix()
    return blocco.group(0).replace('src="assets/', f'src="{relativo}/assets/')


def sprite(prog):
    trovato = re.search(r'<svg width="0".*?</svg>', esempio_design(prog), re.S)
    return trovato.group(0) if trovato else ""


def senza_sprite(corpo):
    """Lo sprite delle frecce (dg-punta) sta una volta sola, in testa al documento."""
    return re.sub(r'<svg width="0"[^>]*>.*?</svg>', "", corpo, flags=re.S)


def css(prog, parti):
    stile = leggi(prog.design / "stile.css").replace(TITOLO_CSS, prog.titolo.replace('"', '\\"'))
    blocchi = [leggi(prog.design / "assets" / "montserrat-embedded.css"), stile]
    for n in parti:
        file = prog.finale / f"parte-{n}.css"
        if file.exists():
            blocchi.append(leggi(file))
    return "\n".join(blocchi + [INDICE_CSS])


def pagine_salvate(prog):
    return json.loads(leggi(prog.pagine_json)) if prog.pagine_json.exists() else {}


def indice(parti, pagine):
    def pag(chiave):
        return pagine.get(chiave, SEGNAPOSTO)

    blocchi = []
    for p in parti:
        righe = [
            f'    <a class="indice-titolo" href="#parte-{p["numero"]}"><span class="indice-num">{p["numero"]}</span>'
            f'<h2>Parte {p["numero"]} — {html.escape(p["titolo"])}</h2><span class="guida"></span>'
            f'<span class="pag">{pag("parte-%d" % p["numero"])}</span></a>'
        ]
        for numero, titolo in p["capitoli"]:
            righe.append(
                f'    <a class="indice-riga" href="#{id_capitolo(numero)}"><span class="num">{numero}</span>'
                f'<span>{html.escape(titolo)}</span><span class="guida"></span>'
                f'<span class="pag">{pag(id_capitolo(numero))}</span></a>'
            )
        blocchi.append('  <div class="indice-parte">\n' + "\n".join(righe) + "\n  </div>")
    return ('<section class="indice">\n  <p class="occhiello">Il manuale</p>\n  <h1>Indice</h1>\n\n'
            + "\n\n".join(blocchi) + "\n</section>")


def documento(titolo, stile, corpo):
    return f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titolo)}</title>
<style>
{stile}
</style>
</head>
<body>
{corpo}
</body>
</html>
"""


# ---------- immagini incorporate -------------------------------------------------

def sips(sorgente, destinazione, *opzioni):
    subprocess.run(["sips", *opzioni, str(sorgente), "--out", str(destinazione)],
                   capture_output=True, text=True, check=True)


def proprieta(immagine):
    uscita = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", "-g", "hasAlpha",
                             str(immagine)], capture_output=True, text=True, check=True).stdout
    valori = dict(re.findall(r"^\s+(\w+): (\S+)$", uscita, re.M))
    return max(int(valori["pixelWidth"]), int(valori["pixelHeight"])), valori.get("hasAlpha") == "yes"


def versione_leggera(prog, sorgente):
    """Ridimensiona e comprime nella cache: foto in JPEG, PNG trasparenti restano PNG, SVG intatti."""
    if sorgente.suffix.lower() == ".svg":
        return sorgente
    lato_max = prog.lato_max_per.get(sorgente.name, LATO_MAX)
    lato, trasparente = proprieta(sorgente)
    e_jpeg = sorgente.suffix.lower() in (".jpg", ".jpeg")
    if lato <= lato_max and (trasparente or (e_jpeg and sorgente.stat().st_size <= JPEG_INTATTO_MAX)):
        return sorgente
    destinazione = prog.img_cache / (sorgente.stem + (".png" if trasparente else ".jpg"))
    if destinazione.exists() and destinazione.stat().st_mtime >= sorgente.stat().st_mtime:
        return destinazione
    prog.img_cache.mkdir(exist_ok=True)
    opzioni = ["-Z", str(lato_max)] if lato > lato_max else []
    if not trasparente:
        opzioni += ["-s", "format", "jpeg", "-s", "formatOptions", str(JPEG_QUALITA)]
    sips(sorgente, destinazione, *opzioni)
    return destinazione


def con_immagini_incorporate(prog, testo):
    cache = {}

    def sostituisci(m):
        percorso = m.group(1)
        if percorso not in cache:
            sorgente = (prog.finale / percorso).resolve()
            if not sorgente.exists():
                sys.exit(f"immagine mancante: {percorso}")
            file = versione_leggera(prog, sorgente)
            codifica = base64.b64encode(file.read_bytes()).decode("ascii")
            cache[percorso] = f"data:{MIME[file.suffix.lower()]};base64,{codifica}"
        return f'src="{cache[percorso]}"'

    return re.sub(r'src="(?!data:|https?:|#)([^"]+)"', sostituisci, testo)


# ---------- comandi --------------------------------------------------------------

def costruisci_html(prog):
    parti = carica_parti(prog)
    corpo = "\n\n".join([sprite(prog), copertina(prog), indice(parti, pagine_salvate(prog))]
                        + [senza_sprite(p["html"]) for p in parti])
    finale = con_immagini_incorporate(
        prog, documento(prog.titolo, css(prog, range(1, prog.parti + 1)), corpo))
    if re.search(r'src="(?!data:)', finale):
        sys.exit("restano immagini non incorporate")
    prog.html_out.write_text(finale, encoding="utf-8")
    print(f"{prog.html_out.name}: {len(finale) // 1024} KB")


def costruisci_prova(prog, n):
    parte = carica_parte(prog, n)
    corpo = sprite(prog) + "\n" + senza_sprite(parte["html"])
    uscita = prog.finale / f"prova-parte-{n}.html"
    uscita.write_text(documento(f"Prova parte {n}", css(prog, [n]), corpo), encoding="utf-8")
    print(f"{uscita.name}: stampa con scripts/stampa.sh {uscita}")


def numero_pagine(pdf):
    info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True, check=True).stdout
    return int(re.search(r"Pages:\s+(\d+)", info).group(1))


def righe_pagina(pdf, n):
    testo = subprocess.run(["pdftotext", "-f", str(n), "-l", str(n), "-layout", str(pdf), "-"],
                           capture_output=True, text=True, check=True).stdout
    return [r.strip() for r in testo.splitlines() if r.strip()]


def compatta(riga):
    """La spaziatura delle maiuscole spezza le parole in pdftotext ("CA PI TO LO 1"): via gli spazi."""
    return re.sub(r"\s+", "", riga).lower()


def trova_pagine(prog):
    if not prog.pdf_out.exists():
        sys.exit(f"manca {prog.pdf_out}: prima stampa l'HTML")
    parti = carica_parti(prog)
    righe = {n: [compatta(r) for r in righe_pagina(prog.pdf_out, n)]
             for n in range(PRIMA_PAGINA_CONTENUTO, numero_pagine(prog.pdf_out) + 1)}

    def primo(controllo, chiave):
        for pagina, testa in righe.items():
            if controllo(testa):
                return pagina
        sys.exit(f"pagina non trovata per {chiave}: controlla occhielli e titoli nei frammenti")

    trovate = {}
    for p in parti:
        num = str(p["numero"])
        trovate[f"parte-{num}"] = primo(lambda t: "parte" in t[:4] and num in t[:4], f"parte-{num}")
        for numero, _ in p["capitoli"]:
            trovate[id_capitolo(numero)] = primo(
                lambda t, n=numero: f"capitolo{n}" in t[:6], f"capitolo {numero}")
    precedenti = pagine_salvate(prog)
    prog.pagine_json.write_text(json.dumps(trovate, indent=1) + "\n", encoding="utf-8")
    print("pagine:", ", ".join(f"{k}={v}" for k, v in trovate.items()))
    return 0 if precedenti == trovate else 1


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    progetto, comando = Progetto(sys.argv[1]), sys.argv[2]
    if comando == "html":
        costruisci_html(progetto)
    elif comando == "pagine":
        sys.exit(trova_pagine(progetto))
    elif comando == "prova" and len(sys.argv) == 4:
        costruisci_prova(progetto, int(sys.argv[3]))
    else:
        sys.exit(__doc__)
