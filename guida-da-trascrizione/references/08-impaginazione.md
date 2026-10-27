# Fase 7 — Impaginazione, revisione grafica, assemblaggio, rifinitura

Quattro passi, in quest'ordine. I primi due sono per parte e girano in parallelo.

## 1. Impaginazione per parte (modello medio)

Brief `templates/briefs/impaginazione-parte.md`. Input: testo definitivo (non si cambia, si può solo spezzare un paragrafo lungo), `design/definitivo/` (stile.css, COMPONENTI.md, esempio, PNG), strategia visual, foto.

Produce `finale/parte-N.html`: **frammento** (solo sezioni, niente `<html>/<head>`) che usa solo le classi di `stile.css`. CSS nuovo solo in `finale/parte-N.css` con classi prefissate `pN-`; `stile.css` non si tocca.

Convenzioni che l'assemblaggio richiede:
- Apertura di parte: `<section class="apertura">` con `<h1>` del titolo della parte.
- Ogni capitolo: `<article class="capitolo salto">` con `<p class="occhiello">Capitolo N</p>` subito prima di `<h1>`.
- Immagini con percorsi relativi a `finale/` (es. `../slide/img/s051-5.png`, `../design/definitivo/assets/logo-unicorn-nero.png`).

Regole: ogni `[[GRAFICA]]` diventa un diagramma SVG nello stile del sistema (una figura = una frase, solo i dati del marcatore); ogni `[[FOTO]]` una foto reale con didascalia; box, tabelle e checklist con i componenti; pagine ariose, niente righe orfane in testa pagina, tabelle intere o con intestazione ripetuta.

Prova: `python3 scripts/assembla.py <progetto> prova N` → `finale/prova-parte-N.html`, poi `scripts/stampa.sh finale/prova-parte-N.html 80`. L'impaginatore guarda tutte le PNG e corregge finché è pulito.

## 2. Revisione grafica per parte (modello medio, altro worker)

Brief `templates/briefs/revisione-grafica.md`. Guarda **tutte** le PNG a piena risoluzione, annota ogni difetto con il numero di pagina, corregge in `parte-N.html/.css` (mai il testo), ristampa, riguarda. Ripete finché pulito. Scrive `mappa/grafica-parte-N.md` (difetto → correzione, difetti rimasti, max 40 righe).

Difetti da cercare: pallini e numeri non allineati alla prima riga, checklist con colonne storte, box isolato in una pagina vuota, titolo in fondo pagina staccato dal suo paragrafo, etichette dei diagrammi strette o tagliate, frecce sporche, SVG tagliati dal margine, foto non centrate, pagine di prosa fitta, colori pieni accesi dove serve sobrietà.

## 3. Assemblaggio (modello medio)

Brief `templates/briefs/assemblaggio.md`. Prepara `finale/manuale.json`:

```json
{"titolo": "Titolo del manuale", "file": "Manuale", "parti": 4,
 "design": "../design/definitivo", "lato_max_per": {"logo-unicorn-nero.png": 600}}
```

Poi `scripts/build.sh <progetto>`:
- copertina e sprite delle frecce presi da `design/definitivo/index.html`;
- indice generato dai titoli dei frammenti, con link ai capitoli;
- **indice a due passate**: `target-counter()` non funziona in Chrome, quindi stampa, `pdftotext` trova la pagina di ogni titolo, riscrive l'indice, ristampa finché i numeri sono stabili (max 4 giri);
- immagini incorporate come data URI (ridotte a 1600 px, foto in JPEG q80): l'HTML funziona anche spostato da solo;
- numerazione continua nel piè di pagina, copertina senza numero.

Se l'unione rompe qualcosa (salti pagina, overflow, sprite duplicati), si corregge nei frammenti, non nell'HTML finale.

## 4. Rifinitura (modello forte)

Brief `templates/briefs/rifinitura.md`. Legge tutto il documento (`pdftotext -layout`) come un principiante:
- **Rimandi**: ogni "capitolo N" / "Parte N" punta al capitolo che parla davvero di quella cosa.
- **Sigle e termini** spiegati alla prima occorrenza (se la fonte dà la spiegazione); se la fonte non la dà, niente conoscenza esterna.
- **Contraddizioni** tra parti: uniformate alla versione sostenuta dalla fonte.
- Correzioni **in entrambi i posti**: `testo/parte-N.md` e `finale/parte-N.html` (stesse parole), poi `build.sh`.

In più, facoltativo ma consigliato: **lettore senza contesto** (brief `lettore-principiante.md`): un worker che non ha visto nulla del progetto legge il PDF e dice dove si perde. Trova buchi che autore e revisori non vedono più.

## Completamento

- Ogni parte ha `prova-parte-N.pdf` guardata e `mappa/grafica-parte-N.md`.
- `build.sh` chiude con indice stabile; `mappa/rifinitura.md` esiste.
- Poi passi a `verifiche.md` (fase 8).
