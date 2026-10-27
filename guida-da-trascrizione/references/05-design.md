# Fase 4 — Design

Si sceglie il design guardando pagine vere, non descrizioni. Prima leggi `errori-noti.md` (sezione grafica).

## Due percorsi (scelti in fase 0)

La risposta alla domanda "Varianti di design o stile già deciso?" sta in `CONTESTO.md`.

- **(a) A varianti** — consigliato per il primo manuale o per un brand nuovo. Passi 1–4 qui sotto.
- **(b) Diretto da `assets/`, senza varianti** — consigliato per manuali piccoli o successivi, quando il sistema Unicorn va bene com'è. Fai il passo 1 (contenuto campione, serve a provare i componenti sul testo vero), **salta i passi 2 e 3** e vai al passo 4 con il brief `design-definitivo.md` in versione "design diretto": copertina, struttura e palette di `assets/`, nessuna decisione da varianti. Il cancello resta: l'utente approva le PNG della definitiva. Se non gli piace, si passa al percorso (a) su ciò che non va.

## 1. Contenuto campione (un worker, modello medio)

Brief `templates/briefs/campione.md`. Scrive `design/campione-contenuti.md`: il testo **definitivo-di-prova** di 7 pagine, identico per tutti i designer, preso dalle fonti e dall'indice approvato:

1. Copertina (titolo lavorabile, sottotitolo, etichetta).
2. Indice (parti e capitoli veri, numeri di pagina fittizi).
3. Apertura di una parte (cosa impari, perché conta).
4. Pagina procedura: spiegazione breve, passi numerati, specifica testuale di un **diagramma**, un box "Errore comune", **una foto reale** dalle fonti (file esatto, verificato con `ls`).
5. Pagina con diagramma a tappe (percorso, processo) + testo breve per tappa.
6. Checklist stampabile + box "Dal campo" con un caso reale.
7. Pagina discorsiva con un piccolo schema e una tabella.

Così ogni variante mette alla prova gli stessi componenti: diagrammi, foto, box, checklist, tabelle.

## 2. Varianti (3–4 worker in parallelo, modello forte)

Brief `templates/briefs/design-variante.md`, uno per variante con una **direzione** diversa dentro lo stesso tema. Direzioni che hanno funzionato:

- **Manuale tecnico rifinito**: evoluzione fedele del template di riferimento, più spazio bianco, gerarchia più forte (la variante "sicura").
- **Libro editoriale**: margini ampi, testatine, aperture di parte a piena pagina con grande numerale, colore usato con parsimonia.
- **Quaderno di campo / schede operative**: ogni capitolo una scheda da portare sul posto, checklist grandi, box molto riconoscibili.
- **Visual-first**: il diagramma comanda la pagina (metodo Visual Explainer: una figura = una frase, ogni numero un'immagine), testo ridotto attorno agli schemi.

Ogni variante produce in `design/variante-N/`: `index.html` (percorsi relativi), PDF con Chrome headless (`scripts/stampa.sh`), PNG per pagina, `NOTE.md` (5–8 righe su scelte e differenze). Il worker **guarda ogni sua PNG** prima del worker_done.

Vincoli fissi in ogni brief di design (verificati alla consegna):
- Montserrat **incorporato** (`assets/montserrat-embedded.css`), verificato con `scripts/controlla-font.py`.
- Logo vero (`assets/logo-unicorn-*.png`), mai la sola scritta.
- Testo in **una colonna**; tabelle e schemi possono avere colonne; affiancare grafica e testo va bene.
- A4 verticale, niente contenuti tagliati, niente pagine mezze vuote non volute.
- Diagrammi in HTML/SVG inline, testo ≥9 pt; foto reali con didascalia, mai illustrazioni inventate al posto di una foto.
- Zero CTA in modalità B.

## 3. Scelta (cancello, solo percorso a)

Per ogni variante fai il foglio d'insieme (`scripts/foglio-pagine.sh design/variante-N/<pdf> design/sheet-vN.png`), guardalo tu, poi mostra all'utente fogli e PDF. Chiedi con AskUserQuestion: quale variante, oppure **cosa prendere da quale** (copertina, struttura, palette, componenti). Chiedi anche cosa **non** vuole vedere più: è la fonte dei vincoli del brief definitivo.

## 4. Variante definitiva (un worker, modello forte)

Brief `templates/briefs/design-definitivo.md`. Parte da `assets/` della skill (stile.css, componenti, esempio) e dalle decisioni dell'utente, scritte nel brief come **vincolanti**. Produce `design/definitivo/`:

- `stile.css` unico (nessun CSS inline nelle pagine), `assets/` (font, loghi, foto usate), `index.html` con le 7 pagine, PDF, `png/`.
- `COMPONENTI.md`: classe CSS + snippet HTML minimo per ogni componente, e la **mappa marcatori → componenti** (`[[GRAFICA]]`, `[[FOTO]]`, box `> **Errore comune**` / `> **Dal campo**` / `> **Attenzione**`, `### Checklist`, `### Perché conta`, `### Come si fa`). È il contratto con gli impaginatori.
- Nel piè di pagina `stile.css` usa il segnaposto `TITOLO DEL MANUALE`: lo sostituisce `assembla.py`.

**Cancello:** l'utente approva guardando le PNG della definitiva. Correzioni puntuali → stesso worker, nuovo giro.

## Completamento

- Percorso a: le varianti sono state confrontate e l'utente ha deciso cosa prendere da quale. Percorso b: nessuna variante, base `assets/`.
- `design/definitivo/` contiene stile.css, COMPONENTI.md, index.html, PDF, PNG.
- `controlla-font.py` OK; hai guardato tu ogni PNG (icone, allineamenti, checklist, testo che sborda).
- Approvazione registrata.
