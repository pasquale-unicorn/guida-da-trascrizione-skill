# Fase 1 — Estrazione

Lavoro meccanico: script, eventualmente un worker su modello economico per lanciarli e controllarli. Nessuna interpretazione dei contenuti.

## Trascrizioni

```sh
scripts/estrai-testo.sh <progetto>
```

- PDF → `testo/<nome>.txt` con `pdftotext`; `.txt/.md/.srt/.vtt` copiati così come sono.
- Stampa le parole per file e il totale. File a 0 parole: chiedi all'utente la fonte giusta (spesso è un PDF scansionato: serve OCR, fuori da questa pipeline).
- Sotto ~10.000 parole totali il coordinatore può leggere da sé; sopra, le trascrizioni le leggono solo i worker.
- Non modificare mai `sorgenti/` né i `.txt` estratti: sono le fonti di verifica di tutte le fasi dopo.

## Slide (.pptx)

```sh
python3 scripts/estrai-pptx.py <progetto>/sorgenti/<file>.pptx <progetto>/slide
python3 scripts/foglio-immagini.py <progetto>/slide
```

- Il .pptx è uno zip: lo script legge `presentation.xml` per l'ordine, i `.rels` di ogni slide per le immagini, `notesSlides` per le note relatore. Non servono LibreOffice né python-pptx.
- Immagini in `slide/img/sNNN-K.ext`; oltre 3 MB anche una copia `-web.jpg` a 1600 px.
- `slide/indice-slide.md`: per ogni slide titolo, testo, note relatore, immagini, video sì/no. **Le note relatore sono la fonte primaria del pensiero del relatore** (cosa dire, obiettivi): i worker devono leggerle.
- `slide/contact/foglio-NNN.png`: 12 miniature per foglio con il nome file, per guardare le immagini in fretta. Molte immagini sono icone e loghi decorativi: si liquidano in blocco.
- Video: segnalati, non estratti (lo script li salta). File da GB: lo script legge a blocchi, non serve spazio extra oltre alle immagini.

## Slide (.pdf)

```sh
python3 scripts/estrai-pdf-slide.py <progetto>/sorgenti/<file>.pdf <progetto>/slide
python3 scripts/foglio-immagini.py <progetto>/slide
```

- Stesso formato dello script pptx: `slide/indice-slide.md` (per pagina titolo = prima riga di testo, testo, immagine), `slide/img/sNNN.png` (110 dpi), `slide/immagini.txt`. Usa `pdftotext -layout` e `pdftoppm` (poppler).
- Un PDF **non ha note del relatore**: l'indice lo scrive per ogni slide. Dillo ai worker: il pensiero del relatore sta solo nelle trascrizioni.
- Le pagine senza testo (solo immagine) vengono contate a fine esecuzione. Guardale nel foglio contact: il contenuto va letto dall'immagine.

## Trascrizione mancante

Se le lezioni sono audio/video **senza testo**, la skill non trascrive: la domanda sta in fase 0 ("Hai già il testo trascritto delle lezioni?"). Se la risposta è no:

1. **Chiedi all'utente la trascrizione** (di solito la esporta la piattaforma di registrazione o la fornisce chi ha tenuto la lezione). È la strada consigliata.
2. In alternativa, **facoltativo** e a scelta dell'utente, Whisper in locale (nessuna dipendenza della skill): `pip install openai-whisper`, poi `whisper <file.mp4> --language it --output_format txt --output_dir <progetto>/sorgenti`. Serve ffmpeg; i file lunghi richiedono tempo.
3. Avvertenza: una trascrizione automatica sbaglia nomi propri, sigle, cifre e termini tecnici, e non distingue i relatori. **Va controllata a mano prima di partire**: un errore di trascrizione diventa un errore del documento.

## Foto sciolte

Copia in `sorgenti/foto/` e fai il foglio: crea `slide/immagini.txt` con i nomi oppure metti le foto in una cartella con sottocartella `img/` e lancia `foglio-immagini.py` su quella.

## Brief

`templates/briefs/slide-estrazione.md` se deleghi (modello economico; per un PDF di slide sostituisci il passo 1 con `estrai-pdf-slide.py`).

## Completamento

- Ogni file in `sorgenti/` ha il suo testo non vuoto in `testo/` (o la sua estrazione in `slide/`).
- Conteggio slide nell'indice = numero di slide del pptx; immagini estratte = immagini referenziate.
- I fogli contact esistono e ne hai aperto almeno uno per controllare che le miniature si vedano.
