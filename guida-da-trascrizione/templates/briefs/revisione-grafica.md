# Task: revisione grafica di una parte impaginata

Cartella: {{PROGETTO}}. La parte è nel messaggio di avvio (PARTE N).

## Input
- `finale/parte-N.html`, `finale/parte-N.css`, la prova `finale/prova-parte-N.pdf` e le sue PNG.
- Riferimento: PNG e `stile.css` di `design/definitivo/` (NON modificare `stile.css`).

## Cosa vuole l'utente (vincolante)
- {{Sobrietà: niente barre o blocchi di colore pieni accesi; colori di stato solo come piccoli pallini o bordi sottili; niente linguette laterali.}}
- Icone: una sola famiglia, stessa dimensione e spessore, allineate al testo o centrate; se non informa, via.
- Pagine non congestionate: niente blocchi di prosa fitti; se una pagina è piena, spezza o dai respiro (spaziature, sottotitoli già presenti). Meglio più pagine.
- Ma niente pagine quasi vuote senza motivo: un box isolato in una pagina vuota va riunito al contenuto vicino.
- Checklist e tabelle: colonne allineate, larghezze fisse, numeri e caselle sulla stessa riga, intestazioni ripetute a pagina nuova.
- Diagrammi: etichette mai strette o tagliate, frecce pulite, testo ≥8–9 pt.

## Cosa fai
1. Guarda TUTTE le PNG a piena risoluzione (`sh {{SKILL}}/scripts/stampa.sh finale/prova-parte-N.html 110`), una per una. Annota ogni difetto con il numero di pagina.
2. Correggi in `finale/parte-N.html` / `parte-N.css` (classi `pN-`). NON cambiare il testo.
3. Ristampa, riguarda. Ripeti finché pulito.
4. `python3 {{SKILL}}/scripts/controlla-font.py finale/prova-parte-N.pdf`.

## Consegna
`mappa/grafica-parte-N.md` (difetti → correzione, difetti rimasti, max 40 righe) e worker_done: pagine prima/dopo, difetti corretti, difetti rimasti.
