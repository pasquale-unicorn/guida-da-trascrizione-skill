# Task: impaginazione di una parte

Cartella: {{PROGETTO}}. La parte è nel messaggio di avvio (PARTE N).

## Input
- Testo definitivo: `testo/parte-N.md` (già rivisto: NON cambiare il contenuto; ammesso solo spezzare paragrafi lunghi).
- Sistema grafico: `design/definitivo/` → `stile.css`, `COMPONENTI.md`, `index.html` (esempi), `assets/`, PNG. Guarda le PNG per capire lo stile.
- Strategia grafiche: `mappa/strategia-visual.md`. Foto: `slide/img/`.

## Cosa produci
`finale/parte-N.html`: frammento HTML (solo le sezioni, niente `<html>/<head>`), che usa SOLO le classi di `stile.css`. CSS nuovo solo in `finale/parte-N.css` con classi prefissate `pN-`. Non modificare `stile.css`.

Convenzioni obbligatorie (le usa l'assemblaggio):
- Apertura: `<section class="apertura">` … `<h1>Titolo della parte</h1>`.
- Ogni capitolo: `<article class="capitolo salto">` con `<p class="occhiello">Capitolo N</p>` subito prima del suo `<h1>`.
- Immagini con percorsi relativi a `finale/` (es. `../slide/img/...`, `../design/definitivo/assets/...`).

Prova: `python3 {{SKILL}}/scripts/assembla.py {{PROGETTO}} prova N` e poi `sh {{SKILL}}/scripts/stampa.sh finale/prova-parte-N.html 80` (serve `finale/manuale.json`: se manca crealo come in `{{SKILL}}/references/08-impaginazione.md`).

## Regole
- Apertura di parte come nel design (numero grande, titolo, riga d'introduzione, "Cosa impari"). Niente citazioni.
- Ogni capitolo su pagina nuova, con "Cosa ottieni" se il testo lo ha.
- Ogni `[[GRAFICA: id | frase | dati]]` → diagramma SVG nello stile del sistema. Una figura = una frase. Solo i dati del marcatore e del testo. Niente icone decorative.
- Ogni `[[FOTO: path | didascalia]]` → foto reale con didascalia; il file esiste.
- Box e checklist → componenti di `COMPONENTI.md`. Tabelle e checklist con colonne a larghezza fissa.
- Pagine ariose: corpo come da sistema, mai pagine piene fino al bordo, mai testo che sborda o tagliato, niente righe orfane in testa pagina, tabelle intere o con intestazione ripetuta. Meglio una pagina in più.

## Verifica (obbligatoria, di persona)
Guarda TUTTE le PNG della prova: testo che sborda, sovrapposizioni, icone storte, etichette strette nei diagrammi, pagine quasi vuote o troppo piene, tabelle spezzate. Correggi e ristampa finché è pulito.

## Consegna
worker_done: numero pagine, numero grafiche/foto, problemi corretti, dubbi.
