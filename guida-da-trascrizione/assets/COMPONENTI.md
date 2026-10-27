# Componenti del sistema grafico — manuale operativo Unicorn

Sistema nato per il manuale "affitti brevi" (esempio completo in `esempio/index.html`, testi di quel caso). In un progetto nuovo copia `stile.css`, `montserrat-embedded.css` e i loghi nella cartella `design/` del progetto e impagina con questi componenti. Se il design approvato in fase 4 cambia qualcosa, aggiorna QUESTO file nella copia di progetto: è il contratto tra designer e impaginatori.

Un solo foglio di stile: `stile.css`. Il font sta in `assets/montserrat-embedded.css` (Montserrat variabile, base64). Ogni pagina HTML parte da:

```html
<link rel="stylesheet" href="assets/montserrat-embedded.css">
<link rel="stylesheet" href="stile.css">
```

Stampa di prova: `scripts/stampa.sh <file.html>` (Chrome headless `--print-to-pdf` + `pdftoppm` + `pdfinfo` + `pdffonts`).
Esempio completo di tutti i componenti: `esempio/index.html`.

## Regole del sistema

- **A4, una colonna.** Margini pagina 18 / 16 / 24 / 16 mm (sopra, lato, sotto, lato): area di testo 178 mm. Il flusso è automatico, niente pagine fisse.
- **Corpo 10,5 pt**, tabelle e checklist 10 pt, didascalie e note 9 pt (token `--fs-corpo`, `--fs-tabella`, `--fs-nota`). Mai sotto 9 pt, nemmeno nelle grafiche SVG.
- **Mai margini negativi** (né elementi più larghi di 178 mm): Chrome rimpicciolisce tutto il documento per farli stare. Un margine negativo nell'indice ha rimpicciolito il foglio del 2,7% finché non è stato tolto.
- **Niente linguette, anelli, decorazioni sul bordo.** Le barre colorate sono ammesse solo dentro il testo (citazione).
- **Icone**: una sola famiglia, griglia 48×48, tratto 2 (1,6 se scalata), terminazioni tonde, `currentColor`, dentro un cerchio. Compaiono solo dove danno informazione: copertina e i tre impianti nell'apertura di parte. Nei box, nei titoli, nelle tabelle non ci sono icone.
- **Numeri di pagina**: margin box `@page` con `counter(page)`, in basso a destra; a sinistra il titolo del manuale (in `stile.css` c'è il segnaposto `TITOLO DEL MANUALE`, che `assembla.py` sostituisce). La copertina non li ha (pagina nominata `copertina`, margine 0).
- **Indice**: `target-counter()` NON funziona in Chrome 155 (provato, la riga resta vuota). I numeri di pagina dell'indice si scrivono a mano o con un secondo passaggio: dare un `id` a ogni capitolo, fare il PDF, `pdftotext -f N -l N` per trovare in che pagina compare il titolo, scrivere i numeri nell'indice, rifare il PDF. È ciò che fa `scripts/assembla.py`.
- **Dati citati**: le citazioni stanno senza attribuzione (niente nomi di docenti, corso, date, timestamp). Per attribuire c'è `<span class="fonte">`, da usare solo se serve.

## Palette (token `:root`)

| Uso | Token | Valore |
|---|---|---|
| Testo | `--inchiostro` | `#27313c` |
| Titoli | `--titolo` | `#261333` |
| Accento | `--viola` / `--viola-scuro` / `--viola-medio` | `#7c3aed` / `#581c87` / `#6b21a8` |
| Secondario | `--ciano` / `--ciano-scuro` | `#0891b2` / `#0e6f87` |
| Fondi tenui | `--viola-carta`, `--grigio-carta` | `#faf5ff`, `#f5f8fa` |
| Errore comune | `--ambra*` | fondo `#fffbeb`, bordo `#e4b95f`, testo `#92400e` |
| Attenzione | `--mattone*` | fondo `#fbf6f5`, bordo `#d9b8b4`, testo `#8a3a30` |
| Terra (solo schema elettrico) | `--terra-giallo`, `--terra-verde` | `#c9a800`, `#3d8b57` |

## Mappa marcatori del testo → componenti

| Marcatore nel testo | Componente | Classe |
|---|---|---|
| `[[GRAFICA: ...]]` | figura con SVG inline | `figure.grafica` |
| `[[FOTO: ...]]` | figura con foto reale | `figure.foto` |
| `> **Errore comune**` | box ambra | `aside.box.box-errore` |
| `> **Dal campo**` | box azzurro | `aside.box.box-campo` |
| `> **Attenzione**` | box mattone | `aside.box.box-attenzione` |
| `### Checklist` | tabella stampabile | `section.checklist` |
| `### Perché conta` | sezione con elenco puntato | `section.perche` |
| `### Come si fa` | passi numerati | `ol.passi` |
| citazione `> «...»` | citazione | `blockquote.citazione` |
| `**Cosa ottieni:**` | riquadro grigio | `div.cosa-ottieni` |
| `### Cosa impari` (apertura parte) | elenco con pallini ciano | `ul.elenco-punti` |
| tabella Markdown | tabella | `table.tabella` |
| tabella "l'ospite vuole / tu fai" | tabella a tappe | `table.tabella-tappe` |
| `### Come funziona`, `### Routine`… | titolo di sezione | `h2` |
| CTA (solo modalità A) | bottone a pillola | `div.cta-riga > a.cta` |

## Componenti

### Copertina — `section.copertina`
Variante 4 ripresa fedelmente: gradiente 155°, logo bianco, tag, titolo 45 pt, sottotitolo, casa con tre cerchi. Solo etichetta, titolo e sottotitolo: **nessuna data, nessun docente**. Pagina a pieno foglio (`page: copertina`).

```html
<section class="copertina">
  <img class="copertina-logo" src="assets/logo-unicorn-bianco.png" alt="Unicorn">
  <div class="copertina-tag">Manuale operativo per corsisti</div>
  <h1>Affitti brevi<br>a prova<br>di ospite</h1>
  <p class="copertina-sotto">Sottotitolo</p>
  <figure><svg viewBox="0 0 680 350">…casa + 3 cerchi…</svg></figure>
</section>
```

### Indice — `section.indice`
Un blocco per parte; `.in-evidenza` per la parte corrente. Numero in quadrato 8×8 mm, riga di guida a puntini, pagina allineata a destra con larghezza fissa.

```html
<section class="indice">
  <p class="occhiello">Il manuale</p><h1>Indice</h1>
  <div class="indice-parte in-evidenza">
    <div class="indice-titolo"><span class="indice-num">3</span><h2>Parte 3 — Cantiere e impianti</h2><span class="guida"></span><span class="pag">49</span></div>
    <div class="indice-riga"><span>3.1 Il sopralluogo</span><span class="guida"></span><span class="pag">52</span></div>
  </div>
</section>
```

### Apertura di parte — `section.apertura`
Numero gigante, titolo, riga di sintesi, tre cerchi-icona (opzionali), "Cosa impari", "Perché conta", citazione. Pagina singola, nessuna foto.

```html
<section class="apertura">
  <p class="occhiello">Parte</p>
  <div class="apertura-numero">3</div>
  <h1>Cantiere e impianti</h1>
  <p class="apertura-riga">In una riga.</p>
  <div class="apertura-icone"><svg viewBox="0 0 640 116">…</svg></div>
  <h2>Cosa impari</h2><ul class="elenco-punti"><li>…</li></ul>
  <section class="perche"><h2>Perché conta</h2><ul><li>…</li></ul></section>
  <blockquote class="citazione">«…»</blockquote>
</section>
```

### Capitolo — `article.capitolo`
Testata con logo, occhiello, titolo, "Cosa ottieni". `salto` forza una nuova pagina (usalo sull'`article`, non nel mezzo).

```html
<article class="capitolo salto">
  <header class="cap-testa"><img src="assets/logo-unicorn-nero.png" alt="Unicorn"><span>Parte 3 · Cantiere e impianti</span></header>
  <p class="occhiello">Capitolo 3.2</p>
  <h1>Titolo del capitolo</h1>
  <div class="cosa-ottieni"><b>Cosa ottieni</b><p>Frase.</p></div>
  <h2>Prima sezione</h2> <p>…</p>
</article>
```

Titoli lunghi con due punti: spezza con `<br>` dopo i due punti (`text-wrap: balance` da solo spezza male).

### Perché conta — `section.perche`
```html
<section class="perche"><h2>Perché conta</h2><ul><li>Voce.</li></ul></section>
<!-- oppure paragrafo: <section class="perche"><h2>Perché conta</h2><p>…</p></section> -->
```

### Come si fa (passi) — `ol.passi`
Cerchio = altezza di riga (6 mm), numero centrato; il testo si allinea alla prima riga. Per affiancare una foto: `div.passi-con-foto` con `ol.passi` + `figure.foto` (colonna foto 66 mm).

```html
<div class="passi-con-foto">
  <ol class="passi"><li><strong>Verbo.</strong> Spiegazione.</li></ol>
  <figure class="foto"><img src="…" width="969" height="770" alt="…"><figcaption>Didascalia.</figcaption></figure>
</div>
```

### Grafica — `figure.grafica`  (`[[GRAFICA: ...]]`)
Titolo opzionale `p.grafica-titolo`, SVG inline a tutta larghezza (`viewBox` largo 640–660 unità, così 12–13 px = 9,2–10 pt), didascalia o `p.nota-tecnica`. **Una sola** sprite di freccia per documento, subito dopo `<body>`:

```html
<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
  <marker id="dg-punta" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0 0L10 5L0 10Z"/></marker>
</defs></svg>

<figure class="grafica">
  <p class="grafica-titolo">Titolo</p>
  <svg viewBox="0 0 656 252" role="img" aria-label="Descrizione">
    <rect class="dg-nodo" x="0" y="2" width="121" height="112" rx="8"/>
    <text class="dg-titolo" x="9" y="27">Nodo</text>
    <text class="dg-testo" x="9" y="66">Riga di descrizione</text>
    <path class="dg-freccia" d="M122 58H133"/>
  </svg>
  <figcaption>Didascalia.</figcaption>
</figure>
```

Classi SVG (tutte in `stile.css`, niente colori inline): `dg-nodo` · `dg-nodo-chiave` (nodo evidenziato) · `dg-cornice` (riquadro tratteggiato) · `dg-chip` · `dg-freccia` (+ `dg-freccia-doppia`) · `dg-filo` (linea senza punta) · `dg-titolo` · `dg-sotto` · `dg-testo` · `dg-viola` · `dg-ambra` · `dg-centro` · `dg-cerchio` + `dg-num` (tappa numerata) · `dg-critico` (pallino ambra) · `dg-fascia` + `dg-fascia-testo` · `dg-terra-giallo` + `dg-terra-verde` (due path identici sovrapposti = filo giallo-verde) · `dg-terra-simbolo` · `dg-icona` · `dg-cerchio-icona`.
Tre diagrammi pronti in `esempio/index.html`: *strada della corrente* (flusso a 5 nodi con rami e terra), *sette tappe* (serpentina + fascia turnover + punti critici), *schema Kross* (cornice, 4 componenti, ospite e portali).

Legenda a righe allineate (fili elettrici): `div.legenda-fili > div > i.filo-fase|filo-neutro|filo-terra + span`.

### Foto — `figure.foto`  (`[[FOTO: ...]]`)
Foto reali dalle fonti del progetto (`slide/img/`, `foto/`), mai illustrazioni inventate al posto di una foto. Sempre con `width`/`height` e didascalia 9 pt. Variante a colonna singola: `figure.foto.foto-larga` (100 mm).

### Box — `aside.box`
Etichetta in `<b>` come primo figlio; dentro paragrafi e `blockquote` (corsivo). Nessuna icona, nessuna barra laterale.

```html
<aside class="box box-errore"><b>Errore comune</b><p><strong>Titolo breve.</strong> Spiegazione.</p></aside>
<aside class="box box-campo"><b>Dal campo</b><blockquote>«Citazione.»</blockquote><p><strong>Il caso, in breve.</strong> …</p><p><strong>Cosa impari:</strong> …</p></aside>
<aside class="box box-attenzione"><b>Attenzione</b><p>Avviso.</p></aside>
```

### Checklist stampabile — `section.checklist`  (`### Checklist`)
Tabella a larghezze fisse (colgroup in mm, somma 178). Intestazione a due righe nel `<thead>`: campi da compilare + titoli colonna; il `thead` si ripete a ogni pagina, ogni foglio stampato porta Indirizzo / Data / Con chi. Colonna 1 = casella 5×5 mm + numero; Note = colonna bianca con bordo sinistro, larga 33 mm. Le righe non si spezzano mai tra due pagine.

```html
<section class="checklist">
  <table>
    <colgroup><col style="width:12mm"><col style="width:33mm"><col style="width:57mm"><col style="width:43mm"><col style="width:33mm"></colgroup>
    <thead>
      <tr class="campi"><th colspan="5"><div class="checklist-campi"><span>Indirizzo</span><i></i><span>Data</span><i></i><span>Con chi</span><i></i></div></th></tr>
      <tr><th></th><th>Cosa guardi</th><th>Cosa cerchi</th><th>Se non va</th><th class="c-note">Note</th></tr>
    </thead>
    <tbody>
      <tr><td class="c-spunta"><span class="casella"></span><span class="c-num">1</span></td><td class="c-voce">Voce</td><td>…</td><td>…</td><td class="c-note"></td></tr>
    </tbody>
  </table>
  <div class="chiusura-checklist">
    <p class="tabella-nota"><strong>Nota.</strong></p>
    <div class="spunte-finali">Foto fatte <span class="casella"></span> Video fatto <span class="casella"></span></div>
  </div>
</section>
```

Nota di progetto: la parola più lunga della colonna 2 ("Condizionatore") deve entrare in 33 mm a 10 pt. Se una voce nuova è più lunga, accorciala o allarga la colonna togliendo spazio a Note.

### Tabelle — `table.tabella` e `table.tabella-tappe`
Larghezze sempre in `colgroup` (mm, somma 178), `table-layout: fixed`, intestazioni ripetute, righe non spezzabili. `p.tabella-nota` sotto per le note.

Tabella "l'ospite vuole / tu fai" (colonne 38 / 42 / 98 mm): tappa = `div.tappa` con `span.tappa-num` (cerchio 6 mm) + `span.tappa-nome`; `span.punto-critico` accanto al nome per i punti critici; righe secondarie in `div.extra`.

```html
<table class="tabella-tappe">
  <colgroup><col style="width:38mm"><col style="width:42mm"><col style="width:98mm"></colgroup>
  <thead><tr><th>Tappa</th><th>L'ospite vuole</th><th>Tu fai</th></tr></thead>
  <tbody><tr>
    <td><div class="tappa"><span class="tappa-num">4</span><span class="tappa-nome">Ingresso<span class="punto-critico"></span></span></div></td>
    <td>Entrare senza ostacoli.</td>
    <td><p>Azione principale.</p><div class="extra"><p>Dettaglio.</p></div></td>
  </tr></tbody>
</table>
```

### Regole numerate — `ol.regole`
Numero in quadrato arrotondato 6 mm, testo in `<span>`.

```html
<ol class="regole"><li><span>Regola.</span></li></ol>
```

### CTA a pillola — `a.cta` (SOLO modalità A, lead magnet)
Bottone a pillola con gradiente del brand (`--ciano-scuro` → `--viola` → `--viola-scuro`), testo bianco 11 pt. Mai nei manuali (modalità B: zero CTA). È sempre un link assoluto cliccabile con UTM (`utm_source=guida&utm_medium=pdf&utm_campaign=<nome-campagna>`), mai un link testuale sottolineato. `div.cta-riga` lo centra e non lo spezza tra due pagine (`cta-sinistra` per allinearlo a sinistra); `a.cta.cta-grande` per la pagina CTA finale; `p.cta-nota` per una riga di contorno sotto il bottone.

```html
<div class="cta-riga">
  <a class="cta" href="https://esempio.it/evento?utm_source=guida&amp;utm_medium=pdf&amp;utm_campaign=nome-campagna">Prenota il tuo posto</a>
  <p class="cta-nota">Evento gratuito · posti limitati</p>
</div>
```

### Altri
- `blockquote.citazione` — fondo viola tenue, barra ciano sottile a sinistra dentro il testo, corsivo.
- `div.promemoria` — riquadro grigio con `<b>` viola (es. "Prima di entrare").
- `p.nota-tecnica` — riquadro a filetto per cifre secondarie sotto un diagramma.
- `p.occhiello` — "Capitolo 3.2", "Parte", "Il manuale": 9,5 pt maiuscolo spaziato.
- `.salto` — salto pagina; `.no-spezza` — blocco indivisibile.
