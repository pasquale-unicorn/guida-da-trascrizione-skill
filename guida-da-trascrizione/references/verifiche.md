# Verifiche obbligatorie

Regola madre: **il worker_done non è una verifica.** I worker controllano ciò che il brief nomina, con gli strumenti che scelgono loro. Un `pdftotext` pulito non dice nulla su come appare la pagina stampata: ispezionare un PDF significa **guardarlo**.

## Dopo ogni worker (controlli del coordinatore)

| Fase | Controllo |
|---|---|
| 1 Estrazione | Parole per file >0; numero slide e immagini coerenti; un foglio contact aperto |
| 2 Mappa | Sezioni obbligatorie presenti (`grep '^## '`); ogni dubbio con stato; 3 numeri a campione cercati nella trascrizione con `grep` |
| 3 Revisione | Indice con fonti per ogni capitolo; punti con severità |
| 4 Design | `controlla-font.py`; guardi **ogni** PNG di ogni variante; foglio d'insieme per confrontarle |
| 5 Scrittura | Titoli = indice; file fonti presente; `[[FOTO]]` esistenti; `controlla-divieti.py` |
| 6 Revisione fedeltà | Calo parole 15–35%; 3 correzioni verificate sulla fonte; divieti puliti |
| 7 Impaginazione | Guardi le PNG della prova: almeno apertura, ogni pagina con diagramma, ogni checklist, 5 a caso |
| 7 Assemblaggio | Pagine = somma delle prove + copertina + indice (± bianche giustificate); 5 voci d'indice a campione |

## Checklist finale (fase 8, prima della consegna)

- [ ] `scripts/controlla-font.py finale/<Manuale>.pdf` → solo Montserrat, tutto incorporato.
- [ ] `scripts/controlla-divieti.py finale/<Manuale>.pdf testo/parte-*.md --parole "<parole vietate>"` → nessuna riga, oppure ogni riga guardata e giustificata (falsi positivi: parole spezzate a fine riga, sottostringhe).
- [ ] `pdfinfo`: A4, numero pagine atteso.
- [ ] **Ispezione visiva personale di ogni pagina**: `pdftoppm -r 55 -png` e Read delle PNG, oppure `scripts/foglio-pagine.sh` per la vista d'insieme **più** le pagine chiave a piena risoluzione (copertina, indice, apertura e prime 2 pagine di ogni parte, ogni pagina con diagramma o checklist, 10 a caso). Cerca: testo che sborda, sovrapposizioni, pagine quasi vuote, pagine piene fino al bordo, icone storte, tabelle spezzate.
- [ ] Indice: 5 voci a campione, la pagina indicata contiene davvero quel capitolo; i link dell'indice funzionano nell'HTML.
- [ ] HTML autoconsistente: copialo **da solo** in una cartella temporanea, aprilo con Chrome headless e fai screenshot di 3 punti con foto: le immagini si vedono. `grep -c 'src="[^d]'` sull'HTML = 0.
- [ ] Rimandi "capitolo N" controllati dalla rifinitura (`mappa/rifinitura.md`).
- [ ] Modalità A: ogni CTA è un link cliccabile nel PDF con UTM corretti, e la destinazione esiste.

## Consegna

All'utente: percorso del PDF e dell'HTML, numero di pagine, comando per ricostruire (`scripts/build.sh <progetto>`), punti lasciati prudenti o tolti per mancanza di fonte, decisioni ancora aperte (es. etichetta di copertina). **Cancello:** l'utente conferma la consegna o chiede correzioni puntuali.

## Insidie note dei controlli

- `pdffonts` con font variabile: i nomi delle istanze dipendono dalla versione di Chrome (lo stesso HTML ha dato "Regular/Bold" con una versione e "Thin" con la successiva). Conta la famiglia e la colonna `emb`; il peso si controlla a vista.
- pdftotext spezza le parole in maiuscolo spaziato ("CA PI TO LO"): `assembla.py` toglie gli spazi prima di cercare.
- Test di pixel o di rete in browser headless possono dare falsi allarmi: per i controlli visivi conta la PNG.
