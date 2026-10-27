# Task: design definitivo

Cartella: {{PROGETTO}} — leggi prima `CONTESTO.md` e `{{SKILL}}/references/errori-noti.md` (sezione grafica).

## Obiettivo
Il sistema grafico definitivo in `design/definitivo/`, dimostrato sulle 7 pagine campione (`design/campione-contenuti.md`). Servirà a impaginare l'intero documento: deve essere riusabile, un unico `stile.css` e componenti documentati.

## Decisioni dell'utente (VINCOLANTI)
Design diretto (senza varianti, scelto in fase 0): copertina, struttura e palette sono quelle di `{{SKILL}}/assets/` e `{{SKILL}}/assets/esempio/index.html`; cancella le prime tre voci sotto (variante X, Y, Z) e tieni le altre. Con le varianti, compila tutte le voci:
- Copertina: {{quella della variante X, ripresa fedelmente}}.
- Struttura: {{della variante Y: diagrammi, tabelle, schede, checklist, box ...}}.
- Palette e sobrietà: {{della variante Z; colori di stato solo come piccoli pallini o bordi sottili}}.
- Vietati: {{es. linguette laterali colorate, fori ad anelli, decorazioni sul bordo pagina}}.
- Difetti da non ripetere: {{es. checklist con colonne note/spunta sfalsate → colonne a larghezza fissa}}.
- Icone: una sola famiglia (stile, spessore, dimensione), allineate al testo o centrate nel contenitore; se non aggiunge informazione, via.
- Aria: corpo minimo 10 pt, interlinea generosa, poco testo vicino; meglio più pagine.
- {{Nessuna data, nessun riferimento all'evento o ai relatori nelle pagine campione.}}

## Regole tecniche
- Parti da `{{SKILL}}/assets/` (stile.css, montserrat-embedded.css, loghi, COMPONENTI.md, esempio/index.html). Copiali in `design/definitivo/` (`stile.css`, `COMPONENTI.md`, `index.html`, `assets/`).
- A4, una colonna, Montserrat incorporato, logo vero, grafiche HTML/SVG, foto reali copiate in `design/definitivo/assets/`.
- Numeri di pagina nei margin box `@page`. Il piè di pagina contiene il segnaposto `TITOLO DEL MANUALE` (lo sostituisce `assembla.py`): non scrivere il titolo a mano.
- La copertina è `<section class="copertina">` in `index.html` (l'assemblaggio la prende da lì, con lo sprite delle frecce `<svg width="0">`).

## Consegna
- `design/definitivo/index.html`, `stile.css`, `assets/`, PDF e PNG (`sh {{SKILL}}/scripts/stampa.sh design/definitivo/index.html`).
- `design/definitivo/COMPONENTI.md`: classe CSS + snippet HTML minimo per ogni componente e **mappa dei marcatori**: `[[GRAFICA: ...]]`, `[[FOTO: ...]]`, `> **Errore comune**`, `> **Dal campo**`, `> **Attenzione**`, `### Checklist`, `### Perché conta`, `### Come si fa`, `**Cosa ottieni:**`.
- Prima di chiudere guarda TU ogni PNG: icone, allineamenti, testo che sborda, checklist. Correggi.
- worker_done: file, pagine, esito controllo font, cosa hai corretto rispetto alle varianti di partenza.
