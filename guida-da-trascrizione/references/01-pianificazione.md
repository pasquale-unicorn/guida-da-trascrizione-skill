# Fase 0 — Pianificazione con domande

Obiettivo: arrivare alla fase 1 con **tutte** le decisioni che cambiano il lavoro già prese. Nel progetto da cui nasce questa skill molte domande sono emerse tardi (date e citazioni nel testo, sobrietà della grafica, copertina, densità delle pagine, attribuzione dei relatori): ognuna è costata un giro di riscrittura o di impaginazione. Qui stanno tutte all'inizio.

## Come chiedere

- Prima leggi la richiesta e i file che l'utente ha indicato (solo `ls` e `wc -w`, non il contenuto delle trascrizioni). Se una risposta è già lì, non chiederla: scrivila in `CONTESTO.md` e mostrala nel riepilogo.
- Usa **AskUserQuestion**, 1–4 domande per chiamata, raggruppate per giro come sotto (un giro con più di 4 domande si divide in due chiamate). Opzione consigliata **per prima**, con "(consigliato)" nell'etichetta. L'utente può sempre rispondere con testo libero.
- Se lavori come worker di un coordinatore (Orca), le domande vanno al coordinatore con `orca orchestration ask`, non con AskUserQuestion.
- Dopo l'ultimo giro: scrivi `CONTESTO.md` (modello in `templates/briefs/CONTESTO.md`), mostra all'utente un **riepilogo delle decisioni** e un **piano di 4–5 righe** (fasi, worker, modelli). **Cancello:** aspetti l'ok.

Modalità A (lead magnet): fai i giri 1, 2, 3 (solo relatori, fedeltà, ricerche), 4, 5 (base grafica e copertina) e 6, poi le domande in più di `modalita-a-lead-magnet.md`. Salta le domande su strumenti senza screenshot e dati che cambiano se la lezione non ne parla.

## Giro 1 — Che cosa facciamo

Sono 5 domande: due chiamate (la modalità e la trascrizione vanno per prime).

| Domanda | Opzioni (prima = consigliata) | Perché conta |
|---|---|---|
| Modalità? | **B Manuale operativo** senza CTA (per chi ha già comprato / deve imparare a fare) · **A Lead magnet** con CTA verso evento/lezione/call | Cambia fasi, tono, lunghezza. A → leggi `modalita-a-lead-magnet.md` |
| Chi legge? | **Principiante assoluto** (parte da zero) · Clienti/corsisti che hanno seguito la lezione · Professionisti del settore | Decide quanto spiegare, sigle, esempi. Default: il documento vale da solo anche per chi non ha visto la lezione |
| Un documento o più? | **Uno solo** con parti · Uno per lezione · Una serie | Decide l'indice e il numero di build |
| Formato? | **PDF A4 + HTML autoconsistente** · Solo PDF · Solo HTML | L'HTML autoconsistente (immagini incorporate) si manda per email o si carica ovunque |
| Hai già il testo trascritto delle lezioni? | **Sì, ho i file** (PDF, txt, srt: li copio in `sorgenti/`) · No, ho solo audio/video | Se no: chiedi all'utente la trascrizione (la strada consigliata) oppure proponi, come strumento **facoltativo**, Whisper (`pip install openai-whisper`, `whisper file.mp4 --language it`) avvisando che gli errori di trascrizione vanno controllati a mano. Mai una dipendenza obbligatoria. Dettagli in `02-estrazione.md` |

## Giro 2 — Le fonti

| Domanda | Opzioni | Perché conta |
|---|---|---|
| Quali fonti ci sono? (multiSelect) | Trascrizioni (PDF/txt) · Slide pptx/PDF · Foto · Video | Le slide con le note del relatore sono spesso la fonte più ricca. Chiedi dove sono i file e copiali in `<progetto>/sorgenti/` |
| Ci sono parti da escludere? | **Sì, te le indico** (es. un blocco fuori tema, una parte promozionale) · No | Va scritto in `CONTESTO.md`: i worker la saltano anche nei riassunti |
| Fonti che arriveranno dopo? | No · Sì (quali, e cosa si fa nel frattempo) | Se le slide arrivano a metà lavoro la mappa va rifatta: meglio aspettarle prima della fase 2 |
| I video si usano? | **No** (solo per capire) · Sì, fotogrammi come foto | I fotogrammi sono spesso sfocati; servono ffmpeg e una scelta a mano |

## Giro 3 — Relatori, fedeltà, dati che cambiano

| Domanda | Opzioni | Perché conta |
|---|---|---|
| Chi sono i relatori e su cosa parla ciascuno? | Te lo dico io · Ricavalo dalle trascrizioni **e poi me lo fai confermare** (consigliato) | Le trascrizioni automatiche dicono "Speaker 1, 2…": attribuire a caso crea errori. Si attribuisce solo con prova o conferma |
| Se un punto è ambiguo, chi decide? | **Relatori non raggiungibili: fedeltà 100% alle fonti, prudenza dove incerto** · Posso chiedere ai relatori (chi, entro quando) | Se nessuno può rispondere, ciò che non è verificabile si formula in modo prudente o si toglie |
| Dati che cambiano nel tempo (costi, tassi, tariffe, prezzi di prodotti)? | **Mai cifre fisse: voce variabile + cosa chiedere** · Cifre delle fonti con data | Una cifra vecchia stampata diventa un errore. Elenca le voci note in `CONTESTO.md` |
| Strumenti/software senza screenshot? | **Parte discorsiva: cosa fa e come organizzarsi, niente "clicca qui"** · Mi procuro le schermate | Istruzioni basate su pulsanti che non vedi sono inventate |
| Ricerche esterne? | **Solo per chiarire un punto delle fonti, con frase approvata da te** · Mai · Libere | Il documento deve rispecchiare le fonti; le ricerche aggiungono rischio |

## Giro 4 — Voce e riferimenti all'evento

| Domanda | Opzioni | Perché conta |
|---|---|---|
| Date, nomi dei relatori, citazioni testuali, riferimenti all'evento ("in aula", "nella slide")? | **No: il documento vale da solo** (default modalità B) · Sì, citazioni con nome · Solo in copertina | Deciso tardi costringe a ripulire tutto il testo. In modalità A spesso le citazioni servono (autorevolezza) |
| Lingua e tono? | **Italiano semplice, del "tu", frasi corte, lessico concreto delle fonti** · Formale (lei) · Altro | Il lessico dei relatori ("quadro", "collettore", "sopralluogo") si conserva: niente gergo da manuale |
| Titolo ed etichetta di copertina? | Proponi tu un titolo lavorabile · Lo do io | Chiedi anche se l'etichetta (es. "Manuale per corsisti") è un riferimento all'evento da evitare |
| Riferimento di tono/taglio? | Un documento esistente (percorso) · Nessuno | I designer e gli scrittori lo studiano prima di partire |

## Giro 5 — Grafica

Sono 6 domande: due chiamate.

| Domanda | Opzioni | Perché conta |
|---|---|---|
| Varianti di design o stile già deciso? | **(a) 3–4 varianti da confrontare** (consigliato per il primo manuale o un brand nuovo) · **(b) Design diretto da `assets/`, senza varianti** (consigliato per manuali piccoli o successivi) | (b) salta campione e varianti e va dritto alla variante definitiva: meno giri e meno costo. Dettagli in `05-design.md` |
| Base grafica? | **Sistema Unicorn della skill** (`assets/`) · Un template esistente (percorso) · Brand diverso (servono logo e font) | Le varianti di design restano nello stesso tema |
| Sobrietà? | **Sobria: palette tenue, colori di stato solo come piccoli pallini o bordi sottili** · Colori pieni e accesi | Con colori accesi le pagine operative diventano rumorose; è stata una correzione tardiva |
| Densità? | **Ariosa: corpo ≥10 pt, poco testo vicino, meglio più pagine** · Compatta (meno pagine) | Cambia il numero di pagine di parecchio |
| Icone e decorazioni? | **Solo dove danno informazione, una sola famiglia, niente decorazioni sul bordo pagina** · Icone ovunque | Linguette laterali, anelli, icone decorative sono state tolte a fine lavoro |
| Copertina? | **La scegli tra le varianti di design** (con la risposta (b) sopra: quella di `assets/`) · Ho già un'idea · Copertina fotografica | Nelle varianti la copertina si sceglie a parte dalla struttura interna (si possono mescolare) |

## Giro 6 — Lavoro e consegna (facoltativo)

| Domanda | Opzioni |
|---|---|
| Come deleghiamo? | **Rilevo da solo** (Orca se c'è, altrimenti subagent) · Solo Claude · Bilanciato Claude/Codex |
| Dove va consegnato? | **Cartella `finale/` del progetto** · Altro (il caricamento su piattaforme lo fa l'utente) |

## Esempio (dal progetto reale)

Manuale operativo affitti brevi: modalità B; pubblico principiante; un solo manuale in 4 parti; trascrizioni già disponibili; 4 trascrizioni + 1 pptx da 141 slide con note relatore; esclusa la parte sulla community; video non usati; due relatori attribuiti per argomento e confermati dall'utente; relatori non raggiungibili → fedeltà 100%; notaio e tassi voci variabili; software gestionale senza schermate → discorsivo; niente date, nomi, citazioni; grafica sobria e ariosa, 4 varianti di design a confronto (primo manuale), copertina scelta tra le varianti.
