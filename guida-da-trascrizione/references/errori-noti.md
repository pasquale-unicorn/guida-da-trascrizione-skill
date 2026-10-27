# Errori noti e lezioni apprese

Raccolti dai progetti reali. Ognuno è costato almeno un giro di lavoro.

## Processo

- **Domande fatte tardi.** Date e citazioni nel testo, sobrietà della grafica, copertina, densità, attribuzione dei relatori, etichetta di copertina: tutte decise a lavoro avviato. → Si chiedono tutte in fase 0 (`01-pianificazione.md`).
- **Fonti arrivate a metà.** Le slide sono arrivate dopo i riassunti: la mappa è stata ripresa e i dubbi riaperti. → Chiedi in fase 0 se arriva altro e, se possibile, aspettalo prima della fase 2.
- **Ordine delle lezioni ≠ ordine di esecuzione.** Copiare l'ordine dei moduli fa scegliere finiture prima delle verifiche che dicono se si possono fare. → Il revisore logico riordina per esecuzione e mette i prerequisiti prima.
- **Due scale fuse in una.** Due classificazioni diverse (es. estensione dei lavori e priorità) presentate come una scala sola fanno credere che "piccolo" significhi "non urgente". → Attributi separati, una matrice invece di un albero.
- **Il riassunto non basta.** Scrivere solo dai riassunti fa perdere sfumature e introduce errori del worker. → L'indice porta le fonti per capitolo e lo scrittore rilegge quei passaggi.
- **Ricerca esterna che entra nel testo.** → Solo per chiarire, con frase approvata; il resto della ricerca resta in `mappa/`.

## Worker e orchestrazione

- **worker_done con verifiche "passate" e difetti veri.** Cornici aperte su un lato, bottoni resi identici, ultima pagina vuota per tre quarti, un titolo copiato da un file gemello. → Il coordinatore guarda sempre l'artefatto.
- **Grep pulito, design rotto.** Una pagina passava tutti i controlli testuali ed era impresentabile. → Screenshot/PNG prima di consegnare.
- **Worker Codex muti senza quota.** Con "Usage limit reached" cinque worker sono rimasti fermi ore senza escalation. → Controllo stalli ogni ≤15 minuti leggendo i terminali; rilancio su Claude.
- **Modello di punta per lavoro banale.** → Tabella dei modelli in `orchestrazione.md`, dichiarata nel piano.
- **Worker che copia da un file gemello** e si porta dietro elementi non suoi. → Nel brief: "usa VERBATIM il contenuto di X", e confronto col sorgente.

## Grafica e stampa

- **Font non incorporato**: Chrome stampa prima che i web font carichino e il PDF esce con un font di sistema anonimo. → Montserrat in base64 nel CSS (`assets/montserrat-embedded.css`) + `--virtual-time-budget`; `controlla-font.py`.
- **Logo finto** (solo la scritta). → Logo vero da `assets/`.
- **Testo su due colonne**: bocciato. → Una colonna, ritmo da libro.
- **Margine negativo**: un solo elemento più largo dell'area di testo fa rimpicciolire a Chrome tutto il documento (−2,7%: copertina con fascia bianca, corpo sotto misura). → Mai margini negativi né elementi oltre 178 mm.
- **`target-counter()` non funziona in Chrome**: l'indice resta senza numeri. → Indice a due passate (`build.sh`).
- **Colori accesi e decorazioni**: linguette laterali colorate, fori ad anelli, barre arancioni piene, icone decorative di famiglie diverse e storte. → Sobrietà: colori di stato solo come piccoli pallini o bordi sottili; una famiglia di icone, solo dove informano.
- **Checklist con colonne storte** (note e spunta sfalsate). → Tabella con `colgroup` in mm (somma 178), casella e numero centrati sulla riga, righe indivisibili, intestazione ripetuta.
- **Pagine fitte** e, all'opposto, **box isolati in pagine vuote**. → Più pagine, ma ogni blocco resta con il contenuto vicino; titoli attaccati al paragrafo che segue.
- **Diagrammi con etichette strette o tagliate dal margine**. → Testo SVG ≥9 pt, `overflow: visible`, passo regolare tra le righe.
- **Schema preso da una slide** (PNG con colori saturi) non si ricolora. → Ridisegnarlo in SVG se pesa sulla sobrietà, altrimenti accettarlo e segnalarlo.
- **Immagini con percorsi relativi**: l'HTML spostato altrove perde le foto. → Data URI in `assembla.py` (immagini ridotte a 1600 px, JPEG q80).

## Testo

- **Riferimenti all'evento rimasti** ("in aula", "come ha detto…", date, timestamp). → Divieti nel brief + `controlla-divieti.py` con le parole decise in fase 0.
- **Stessa cosa con due nomi** in parti diverse (es. "lamina" e "canalina"; "manuale del team" e "manuale della casa"). → Rifinitura: un termine per concetto.
- **Rimandi a capitoli sbagliati** dopo il riordino dell'indice. → Rifinitura controlla ogni "capitolo N" col titolo.
- **Sigle mai spiegate** (es. pratiche edilizie). → Spiegate alla prima occorrenza se la fonte lo fa; altrimenti rimando o nulla, mai conoscenza esterna.
