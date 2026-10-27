# Modalità A — Guida lead magnet con funnel

Guida breve (tipicamente 10–25 pagine) che regala il *cosa* e il *perché* e porta il lettore verso un evento, una lezione gratuita o una call, dove sta il *come* completo. **La guida è un funnel**: ogni capitolo spinge alla lettura del successivo, la chiusura spinge all'azione.

## Cosa resta uguale alla modalità B

Fase 0 con le domande (più quelle del funnel sotto), estrazione, fedeltà alle fonti, brief su file, verifiche, font incorporato, logo vero, una colonna, ispezione visiva di ogni pagina.

## Cosa si accorcia

| Fase B | In modalità A |
|---|---|
| 2 Mappa | Riassunti sì (corpus >10k parole); strategia visual ridotta alle 3–5 grafiche che contano; slide e dubbi solo se ci sono fonti di quel tipo |
| 3 Revisione logica | Leggera, la fa il coordinatore o un worker medio; il cancello resta (scaletta + funnel approvati) |
| 4 Design | Niente varianti se esiste già un template di guida approvato: si usa quello (o `assets/`, risposta (b) alla domanda su varianti/stile già deciso). Varianti solo per un formato nuovo |
| 5–6 Scrittura e revisione | Un solo scrittore (copywriter se disponibile) + una revisione di fedeltà |
| 7 Impaginazione | Un solo file HTML; niente frammenti per parte né indice a due passate se le pagine sono poche (indice a mano o assente) |

## Domande in più in fase 0

| Domanda | Opzioni (prima = consigliata) |
|---|---|
| Verso cosa portano le CTA? | Evento · Lezione gratuita · Call · Prodotto |
| Promessa della guida? | Proponi tu un titolo lavorabile (chi la legge, cosa ottiene) · La do io |
| URL di destinazione e nome campagna per gli UTM? | Li do io (obbligatori prima dell'impaginazione) |
| Quanto "come" regaliamo? | **Cosa e perché completi, come parziale** · Tutto il come (guida di valore pura) |
| Citazioni del relatore? | **Sì, testuali dalla trascrizione** (autorevolezza) · No |

## Funnel interno

- **Almeno 3 CTA**: dopo l'introduzione, a metà su un contenuto forte, in chiusura (pagina CTA finale a piena pagina).
- Ogni CTA ha un angolo di copy diverso ma la stessa destinazione.
- CTA come **bottoni a pillola con il gradiente del brand**: componente `a.cta` di `assets/stile.css` (documentato in `assets/COMPONENTI.md`), mai link testuali sottolineati, anche nelle pagine interne.
- Link assoluti e cliccabili nel PDF, con UTM: `utm_source=guida&utm_medium=pdf&utm_campaign=<nome-campagna>`.
- Brand voice: se installate, usa la skill di voce del brand (per Unicorn: `unicorn-brand-voice`), il copywriter e le skill di lead magnet e offerte (struttura e angolo). Se non ci sono, valgono le regole di voce e anti-scrittura da IA di `references/06-scrittura.md`: bastano a scrivere bene.
- Citazioni dirette del relatore: **testuali** dalla trascrizione, mai parafrasate.

## Come si costruisce (differenze pratiche)

- **Brief**: non esiste un brief dedicato. Usa `scrittura.md` togliendo i divieti "zero CTA, zero marketing" e le citazioni, e aggiungendo come **vincolanti** le risposte alle domande sopra (destinazione, UTM, quante CTA, angolo, citazioni). Brief salvato in `mappa/BRIEF-scrittura.md` come sempre.
- **Un solo HTML, senza `assembla.py`**: scrivi `finale/<nome>.html` completo (head con `stile.css` e `montserrat-embedded.css` copiati accanto o incorporati) partendo da `assets/esempio/index.html`, poi `sh scripts/stampa.sh finale/<nome>.html`. `build.sh` e `manuale.json` servono solo per i documenti a più parti.
- **Piè di pagina**: `stile.css` stampa il segnaposto letterale `TITOLO DEL MANUALE` (lo sostituisce solo `assembla.py`). Nel file di progetto sostituiscilo a mano: `sed -i '' 's/TITOLO DEL MANUALE/Titolo della guida/' finale/stile.css` (su Linux `sed -i` senza `''`).
- **Pulsante CTA**: usa il componente `a.cta` (dentro `div.cta-riga`; `cta-grande` per la pagina finale) già presente in `stile.css`, snippet in `assets/COMPONENTI.md`. Il `href` è il link assoluto con UTM. Serve solo qui: nei manuali (modalità B) non esiste.
- **Lezione solo audio/video**: serve la trascrizione. In fase 0 chiedi se c'è già il testo; altrimenti vedi `references/02-estrazione.md`.

## Verifiche in più

- Ogni CTA cliccabile nel PDF, UTM corretti, destinazione esistente.
- Nessun segnaposto rimasto (`controlla-divieti.py`).
- Peso del PDF <5 MB se va per email (immagini compresse).
- Consegna: percorso PDF + HTML, elenco CTA con URL e UTM usati.
