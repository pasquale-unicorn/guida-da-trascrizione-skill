# {{TITOLO_PROGETTO}} — contesto comune

Ogni worker legge questo file per primo. Scritto in fase 0 con le risposte dell'utente; aggiornalo (con data) quando cambia una decisione.

## Obiettivo
- Modalità: {{A lead magnet con CTA verso ... | B manuale operativo, zero CTA, zero vendita}}.
- Prodotto: {{un solo documento / uno per lezione}}, formato {{PDF A4 + HTML autoconsistente}}.
- Chi legge: {{principiante assoluto: il documento vale da solo, chi legge non ha visto la lezione}}.
- Riferimento di tono e taglio: {{percorso di un documento esistente, o "nessuno"}}.
- Principio guida: concetti semplici, chi legge deve capire e saper fare.

## Fonti
- Trascrizioni: `testo/` (estratte da `sorgenti/`; {{già disponibili / ottenute con Whisper e riviste a mano}}). Sigle usate nei riferimenti: {{T1 = file..., T2 = ...}}.
- Slide: `slide/indice-slide.md` (testo + note relatore = fonte primaria del pensiero del relatore), immagini in `slide/img/`.
- Foto: {{...}}. Video: {{non si usano}}.
- ESCLUSO: {{parti da non riassumere né usare}}.
- In arrivo: {{fonti attese e quando, oppure "nessuna"}}.

## Relatori
- {{Nome A}} = {{argomenti}}; {{Nome B}} = {{argomenti}} (attribuzione confermata dall'utente il {{data}}).
- Nelle trascrizioni i parlanti sono anonimi ("Speaker N"): attribuisci solo se il contesto lo rende evidente o se confermato qui.
- Relatori raggiungibili per dubbi? {{No: fedeltà 100% alle fonti; ciò che non è verificabile si formula in modo prudente o si toglie.}}

## Contenuti
- Dati variabili (mai cifre fisse, sempre "voce variabile + cosa chiedere"): {{es. notaio, tassi, tariffe}}.
- Strumenti senza schermate (parte discorsiva, niente "clicca qui"): {{...}}.
- Ricerche esterne: {{solo per chiarire un punto delle fonti, con frase approvata dall'utente}}.

## Voce e divieti
- {{Italiano semplice, del "tu", frasi corte, lessico concreto delle fonti.}}
- Nel documento: {{nessuna data, nessun timestamp, nessun nome dei relatori, nessuna citazione virgolettata, nessun riferimento all'evento ("in aula", "nella slide", "il docente").}}
- Parole vietate per `controlla-divieti.py`: {{PAROLE_VIETATE}}.

## Grafica
- Design: {{a varianti (primo manuale o brand nuovo) / diretto da `assets/`, senza varianti}}. Base: {{sistema Unicorn della skill / template ...}}. Sobrietà: {{palette tenue, colori di stato solo come pallini o bordi sottili}}. Densità: {{ariosa, corpo ≥10 pt, meglio più pagine}}.
- Fissi: Montserrat incorporato, logo vero, una colonna di testo, A4, foto reali con didascalia.

## Regole di lavoro
- Ogni worker scrive solo i file indicati nel suo brief. `sorgenti/` e le trascrizioni in `testo/` non si modificano.
- Dubbi: si chiedono al coordinatore, non si indovinano.
