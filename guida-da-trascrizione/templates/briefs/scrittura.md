# Task: scrittura del documento (una parte per worker)

Cartella: {{PROGETTO}}. La parte che scrivi è nel messaggio di avvio (PARTE N).

## Cosa leggere (in quest'ordine)
1. `CONTESTO.md` — regole comuni.
2. `mappa/revisione-logica.md` — TUTTO. L'indice definitivo è vincolante: scrivi esattamente i capitoli della tua parte, in quell'ordine, con quei titoli e numeri. Le altre sezioni dicono dove essere prudente, cosa togliere, cosa non affermare.
3. `mappa/riassunto-*.md`, `mappa/dubbi-risolti.md`, ricerche approvate in `mappa/`, `mappa/strategia-visual.md` (quali concetti diventano grafica).
4. `slide/indice-slide.md` — testo e note delle slide citate nei tuoi capitoli. Foto in `slide/img/`.
5. Le trascrizioni in `testo/` — per ogni capitolo rileggi i passaggi indicati nelle fonti dell'indice. Il riassunto non basta: il testo deve rispecchiare la fonte.
6. `{{SKILL}}/references/06-scrittura.md`, sezione «Voce e anti-scrittura da IA»: regole obbligatorie, bastano da sole. Le skill `humanizer`, di voce del brand e copywriter sono facoltative: se installate, usale in più.

## Chi legge
{{Una persona che parte da zero. Il documento non è il resoconto di una lezione: vale da solo.}}

## Divieti assoluti
- {{Nessuna data, nessun timestamp, nessun riferimento all'evento ("durante il corso", "in aula", "nella slide", "il docente").}}
- {{Nessuna citazione virgolettata dei relatori, nessun loro nome.}}
- Nessun fatto fuori da trascrizioni e slide. Niente conoscenza esterna, niente numeri inventati. Fonte incerta → prudente o via.
- Dati variabili ({{VOCI_VARIABILI}}): sempre voci variabili, mai cifre fisse.
- Strumenti senza schermate ({{...}}): solo discorsivo, niente "clicca qui".
- {{Zero CTA, zero marketing.}}

## Voce (regole complete e anti-scrittura da IA: sezione citata al punto 6)
- Italiano semplice, del "tu", frasi corte, una idea per frase. Lessico concreto delle fonti, non gergo da manuale.
- Anti-IA, in breve: niente formule enfatiche, niente elenchi di tre per abitudine, niente trattini lunghi a raffica, niente "non solo… ma anche", niente conclusioni morali, niente sinonimi a rotazione.
- PERCHÉ (2–4 righe) separato dal COME (passi numerati). Titoli che dicono il risultato.
- Poco testo vicino: al massimo ~120 parole di prosa di fila, poi una lista, una tabella, un box o una figura.

## Formato: `testo/parte-N.md`
In apertura una riga d'introduzione alla parte (≤40 parole). Per ogni capitolo:

```
## <numero>. <titolo dall'indice>

**Cosa ottieni:** una frase.

### Perché conta
...

### Come si fa
1. ...

[[GRAFICA: id-breve | la frase che la figura deve far capire | dati/etichette esatte]]
[[FOTO: slide/img/sNNN-K.ext | didascalia]]   (solo foto che hai aperto e verificato)

> **Errore comune** — ...
> **Dal campo** — caso reale anonimo, senza date (solo se c'è nelle fonti)
> **Attenzione** — limiti, cosa va al professionista

### Checklist   (solo dove serve davvero)
- [ ] ...
```

## File fonti (obbligatorio, separato)
`testo/parte-N-fonti.md`: per ogni capitolo, le affermazioni con numeri, procedure o casi e la fonte (file + timestamp, o slide). Serve al revisore, non va nel documento.

## Prima di consegnare
- Rileggi contro le fonti: ogni frase sostenuta.
- Passata completa con le regole anti-IA (e humanizer, se installata).
- `python3 {{SKILL}}/scripts/controlla-divieti.py testo/parte-N.md --parole "{{PAROLE_VIETATE}}"` → pulito.
- worker_done: file scritti, numero capitoli, parole totali, punti lasciati prudenti.
