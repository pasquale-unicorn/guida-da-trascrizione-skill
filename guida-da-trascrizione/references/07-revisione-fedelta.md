# Fase 6 — Revisione di fedeltà per parte

Un revisore per parte, **modello forte**, diverso dallo scrittore se possibile (altro modello o altro fornitore: vede errori diversi). Brief `templates/briefs/revisione-parte.md`. Il revisore **corregge direttamente** `testo/parte-N.md`, non scrive un report da applicare.

## Cosa fa

1. **Fedeltà**: ogni numero, procedura, caso e affermazione tecnica controllata sulla trascrizione o sulla slide (aiutandosi con `parte-N-fonti.md`). Non sostenuta → prudente o tolta. Nessuna conoscenza esterna aggiunta.
2. **Logica**: ordine dei passi, cause ed effetti, rimandi tra capitoli coerenti con l'indice, nessuna contraddizione con le altre parti già scritte.
3. **Divieti**: come in fase 5.
4. **Asciugatura**: −20/−30% di parole senza perdere informazione utile. Via ripetizioni, riempitivi, concetti detti due volte.
5. **Voce**: lessico delle fonti, "tu"; dopo le modifiche, nuova passata con le regole anti-IA di `06-scrittura.md` (e humanizer, se installata).
6. Marcatori `[[GRAFICA]]`, `[[FOTO]]`, box: struttura intatta, salvo togliere quelli non sostenuti. Ogni foto aperta: mostra davvero ciò che dice la didascalia?

## Consegna del revisore

- `testo/parte-N.md` corretto; `parte-N-fonti.md` aggiornato se cambiano le affermazioni.
- `mappa/revisione-parte-N.md`: elenco breve delle correzioni (cosa, perché, fonte), max 60 righe.
- worker_done: correzioni per tipo, parole prima/dopo, dubbi rimasti.

## Controllo del coordinatore

- Parole prima/dopo (`wc -w`): calo tra 15% e 35%. Sotto: asciugatura non fatta; sopra: controlla che non siano spariti contenuti.
- Leggi a campione 3 correzioni del report e verificale sulla fonte.
- `controlla-divieti.py` pulito su tutte le parti.
- I dubbi rimasti: decidi tu se prudenza o domanda all'utente.
