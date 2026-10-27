# Task: rifinitura finale (lettore principiante)

Cartella: {{PROGETTO}}. Prodotto: `finale/{{NOME_FILE}}.pdf` + `.html`, ricostruibili con `sh {{SKILL}}/scripts/build.sh {{PROGETTO}}`. Frammenti in `finale/parte-N.html`, testi in `testo/parte-N.md`.

## Test del lettore principiante
Leggi tutto (`pdftotext -layout finale/{{NOME_FILE}}.pdf -`) come una persona che parte da zero.
- **Rimandi**: ogni "capitolo N" / "Parte N" punta al capitolo che parla davvero di quella cosa (controlla col titolo). Correggi i numeri sbagliati.
- **Termini e sigle** mai spiegati alla prima occorrenza: se la spiegazione esiste più avanti, va bene un rimando; se non esiste e la fonte la dà, aggiungi mezza riga. NON aggiungere conoscenza esterna (fonti: `testo/*.txt`, `slide/indice-slide.md`).
- **Un termine per concetto**: la stessa cosa chiamata in due modi in parti diverse → uniforma.
- **Contraddizioni** tra parti: uniforma alla versione sostenuta dalla fonte.
- **Divieti**: `python3 {{SKILL}}/scripts/controlla-divieti.py finale/{{NOME_FILE}}.pdf --parole "{{PAROLE_VIETATE}}"`.

Correggi sia `testo/parte-N.md` sia `finale/parte-N.html` (stesse parole), poi ricostruisci.

## Verifica
- Ricostruisci; `controlla-font.py`; `pdfinfo`; indice ancora corretto (5 voci a campione).
- Se cambiano le pagine, guarda di persona le pagine toccate (PNG).
- Copia l'HTML da solo in una cartella temporanea, aprilo con Chrome headless e fai lo screenshot di 3 punti con foto: le immagini si vedono.

## Consegna
`mappa/rifinitura.md` (correzioni: pagina, prima → dopo, fonte; max 50 righe; più "verificati senza modifiche" e "da decidere") e worker_done con l'esito.
