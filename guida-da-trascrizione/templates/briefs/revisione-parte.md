# Task: revisione di fedeltà e logica di una parte

Cartella: {{PROGETTO}}. La parte è nel messaggio di avvio (PARTE N).

## Input
- `testo/parte-N.md` (testo) e `testo/parte-N-fonti.md` (affermazione → fonte).
- Fonti primarie: trascrizioni in `testo/`, slide in `slide/indice-slide.md` e `slide/img/`.
- Vincoli: `CONTESTO.md`, `mappa/revisione-logica.md`, `mappa/BRIEF-scrittura.md` (divieti e formato).

## Cosa fai — correggi DIRETTAMENTE `testo/parte-N.md` (non un report da applicare)
1. **Fedeltà**: ogni numero, procedura, caso e affermazione tecnica controllata sulla trascrizione o sulla slide. Non sostenuta → prudente o via. Niente conoscenza esterna.
2. **Logica**: ordine dei passi, cause ed effetti, rimandi tra capitoli coerenti con l'indice, nessuna contraddizione con le altre parti già in `testo/`.
3. **Divieti**: quelli del brief di scrittura.
4. **Asciugatura**: chi legge parte da zero e vuole poco testo vicino. Via ripetizioni, riempitivi, concetti detti due volte. Obiettivo −20/−30% di parole senza perdere informazione utile.
5. **Voce**: lessico delle fonti, "tu". Dopo le modifiche, nuova passata con le regole anti-IA di `{{SKILL}}/references/06-scrittura.md` (e humanizer, se installata).
6. Marcatori (`[[GRAFICA]]`, `[[FOTO]]`, box `>`): struttura intatta, salvo togliere quelli non sostenuti. Ogni `[[FOTO: path]]` esiste e mostra davvero ciò che dice la didascalia (aprila).

## Consegna
- `testo/parte-N.md` corretto; `parte-N-fonti.md` aggiornato se cambi affermazioni.
- `mappa/revisione-parte-N.md`: correzioni (cosa, perché, fonte), max 60 righe.
- worker_done: correzioni per tipo, parole prima/dopo, dubbi rimasti.
