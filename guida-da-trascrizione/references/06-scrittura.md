# Fase 5 — Scrittura per parti

Un worker per parte, in parallelo, modello medio-forte (scrittura nuova). Stesso brief per tutti (`templates/briefs/scrittura.md`, salvato come `mappa/BRIEF-scrittura.md`); il messaggio di avvio dice solo "PARTE N".

## Cosa legge lo scrittore, in ordine

1. `CONTESTO.md`.
2. `mappa/revisione-logica.md` — **tutto**. L'indice definitivo è vincolante: capitoli, ordine, titoli identici. Le sezioni su contraddizioni, errori, rischi dicono dove essere prudenti.
3. Riassunti, dubbi risolti, ricerche approvate, strategia visual (quali concetti diventano grafica).
4. `slide/indice-slide.md` per le slide citate nei suoi capitoli; foto in `slide/img/`.
5. **Le trascrizioni, ai passaggi indicati nelle fonti di ogni capitolo.** Il riassunto non basta: il testo finale rispecchia la fonte.
6. Le regole di **Voce e anti-scrittura da IA** qui sotto (sempre). Le skill `humanizer`, di voce del brand e copywriter sono facoltative: se installate, usale in più.

## Voce e anti-scrittura da IA (regole minime, valgono senza altre skill)

Voce:
- Dai del **"tu"**. Frasi corte (di norma sotto le 20 parole), una idea per frase, verbi concreti.
- **Lessico dei relatori**: usa le parole delle fonti ("quadro", "sopralluogo"), non sinonimi da manuale. Una cosa ha un nome solo, ripetuto: niente sinonimi a rotazione.
- **Perché** (2–4 righe) separato dal **come** (passi numerati). Titoli che dicono il risultato, non l'argomento.
- Poco testo vicino: al massimo ~120 parole di prosa di fila, poi una lista, una tabella, un box o una figura.

Da non fare (i segni tipici della scrittura da IA):
- Niente formule enfatiche o promozionali ("fondamentale", "cruciale", "a 360 gradi", "è importante sottolineare che", "scopriamo insieme").
- Niente elenchi di tre per abitudine: gli elementi sono quanti sono nella fonte.
- Niente trattini lunghi a raffica (—): al massimo uno ogni tanto, altrimenti punto o virgola.
- Niente "non solo… ma anche", niente "non è X, è Y" ripetuto.
- Niente conclusioni morali o riassuntive a fine capitolo ("In sintesi", "Ricorda sempre che…"), niente apertura meta ("In questo capitolo vedremo").
- Niente domande retoriche in apertura, niente "Immagina di…".
- Niente grassetto a pioggia: solo il termine chiave, la prima volta.
- Niente attribuzioni vaghe ("gli esperti dicono"): o c'è la fonte o la frase si toglie.
- Ritmo vario: non tutte frasi della stessa lunghezza, non catene di gerundi.
- Prova finale: se una frase starebbe bene in qualsiasi manuale, riscrivila con il dettaglio concreto delle fonti o toglila.

## Formato del file `testo/parte-N.md`

Una riga d'introduzione alla parte (≤40 parole), poi per ogni capitolo:

```
## <numero>. <titolo dall'indice>

**Cosa ottieni:** una frase.

### Perché conta
...

### Come si fa
1. ...

[[GRAFICA: id-breve | la frase che la figura deve far capire | dati ed etichette esatte]]
[[FOTO: slide/img/s051-5.png | didascalia]]      (solo foto aperte e verificate)

> **Errore comune** — ...
> **Dal campo** — caso reale anonimo, senza date (solo se c'è nelle fonti)
> **Attenzione** — limiti, cosa va chiesto al professionista

### Checklist        (solo dove serve davvero)
- [ ] ...
```

Box e grafiche solo dove servono, seguendo la strategia visual.

## File fonti (obbligatorio, separato)

`testo/parte-N-fonti.md`: per ogni capitolo, le affermazioni con numeri, procedure o casi e la fonte (file + timestamp, o slide). Serve al revisore, non va nel documento.

## Divieti (modalità B, salvo decisioni diverse in `CONTESTO.md`)

- Nessuna data, timestamp, riferimento all'evento ("durante il corso", "in aula", "nella slide", "il docente"); nessun nome dei relatori; nessuna citazione virgolettata dei relatori.
- Nessun fatto fuori dalle fonti; nessun numero inventato; dati variabili come voce variabile.
- Strumenti senza schermate: solo discorsivo, niente "clicca qui".
- Zero CTA, zero marketing.

Prima del worker_done lo scrittore rilegge il testo con le regole anti-IA e lancia `scripts/controlla-divieti.py testo/parte-N.md --parole "<parole vietate da CONTESTO.md>"`.

## Completamento (lo verifichi tu)

- Capitoli di ogni parte = capitoli dell'indice approvato, stessi titoli e numeri (confronto con `grep '^## '`).
- Esiste il file fonti per ogni parte.
- Ogni `[[FOTO: path]]` punta a un file esistente.
- `controlla-divieti.py` pulito.
