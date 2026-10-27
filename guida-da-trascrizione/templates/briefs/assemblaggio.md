# Task: assemblaggio del documento finale

Cartella: {{PROGETTO}}.

## Input
- Frammenti impaginati e rivisti: `finale/parte-1.html` … `parte-{{NUM_PARTI}}.html` (+ `parte-N.css`).
- Sistema grafico: `design/definitivo/` (stile.css, assets, copertina e sprite in `index.html`).
- Indice definitivo: `mappa/revisione-logica.md` (i titoli veri sono quelli nei frammenti).

## Cosa fai
1. Scrivi `finale/manuale.json`:
   `{"titolo": "{{TITOLO}}", "file": "{{NOME_FILE}}", "parti": {{NUM_PARTI}}, "design": "../design/definitivo", "lato_max_per": {"logo-unicorn-nero.png": 600}}`
2. `sh {{SKILL}}/scripts/build.sh {{PROGETTO}}` — copertina → indice → parti; indice a due passate (target-counter non funziona in Chrome); immagini incorporate; PDF.
3. Se l'unione rompe qualcosa (salti pagina, overflow, sprite doppi), correggi nei frammenti, non nell'HTML finale. Non cambiare testo né impaginazione interna delle parti.

## Verifica obbligatoria
- `python3 {{SKILL}}/scripts/controlla-font.py finale/{{NOME_FILE}}.pdf`.
- `pdfinfo`: pagine = somma delle prove + copertina + indice (± bianche giustificate).
- Guarda di persona copertina, indice, le prime 2 pagine di ogni parte e 10 pagine a caso (PNG).
- 5 voci d'indice a campione: la pagina contiene quel capitolo.
- `python3 {{SKILL}}/scripts/controlla-divieti.py finale/{{NOME_FILE}}.pdf --parole "{{PAROLE_VIETATE}}"`.

## Consegna
worker_done: pagine, esito font, esito divieti, giri dell'indice, problemi risolti.
