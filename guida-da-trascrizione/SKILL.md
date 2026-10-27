---
name: guida-da-trascrizione
description: Trasforma trascrizioni di lezioni, corsi, audio o video (più slide e foto) in un PDF+HTML impaginato con il brand Unicorn: un manuale operativo per chi studia oppure una guida lead magnet con CTA. Usala quando l'utente chiede "manuale da trascrizioni", "manuale operativo dal corso", "guida da lezione", "PDF dalla lezione", "lead magnet da audio", "impagina questa lezione", anche se non nomina la skill.
---

# Guida da trascrizione

Dalle fonti grezze (trascrizioni, slide, foto) a un documento stampabile che **vale da solo**: chi lo legge non ha visto la lezione. Due modalità:

- **A — Lead magnet**: guida breve con funnel e CTA verso un evento, una lezione o una call. Dettagli in [references/modalita-a-lead-magnet.md](references/modalita-a-lead-magnet.md).
- **B — Manuale operativo**: manuale lungo per chi deve imparare a fare, zero CTA, zero vendita. È il percorso completo descritto sotto.

Tu sei il **coordinatore**: decidi, deleghi, verifichi. Le fonti le leggono e scrivono i worker (se il corpus è sotto ~10.000 parole puoi leggerlo tu: vedi fase 1); nel tuo contesto entrano solo esiti brevi, decisioni e percorsi di file. Come delegare (Orca o Agent tool, quali modelli, controllo stalli): [references/orchestrazione.md](references/orchestrazione.md).

## Regole d'oro

1. **Fedeltà alle fonti.** Ogni frase del documento è sostenuta da una trascrizione, una slide o una foto del progetto. Dove la fonte è incerta: formulazione prudente oppure si toglie. Conoscenza esterna solo per chiarire (es. un prodotto citato), con frase approvata dall'utente.
2. **Cancelli.** Ai cancelli ti fermi e aspetti l'approvazione esplicita dell'utente. Senza "ok" non si passa alla fase dopo.
3. **Brief su file, poi worker.** Ogni worker parte da un brief salvato in `mappa/BRIEF-<nome>.md` (modelli in `templates/briefs/`). Il messaggio di avvio contiene solo il percorso del brief e la parte assegnata.
4. **Il worker_done non è una verifica.** Ogni artefatto lo controlli tu: i PDF li guardi pagina per pagina (PNG), i testi li confronti con la fonte. Elenco completo: [references/verifiche.md](references/verifiche.md).
5. **Modello giusto per il lavoro.** Meccanico → modello economico; giudizio, revisione, strategia → modello forte. Il modello di punta resta per il ragionamento difficile.
6. **Semplice.** Una idea per frase, il *perché* separato dal *come*, una figura = una frase. Meglio una pagina in più che una pagina piena.

## Le fasi (modalità B)

Ogni fase ha una reference: leggila quando entri nella fase.

| # | Fase | Chi | Esce | Cancello |
|---|---|---|---|---|
| 0 | Pianificazione con domande | tu + utente | `CONTESTO.md`, piano | **sì: piano approvato** |
| 1 | Estrazione | script + worker economico | `testo/`, `slide/` | — |
| 2 | Mappa | worker (economico e forte) | `mappa/*.md` | — |
| 3 | Revisione logica + indice | worker frontier | `mappa/revisione-logica.md` | **sì: indice approvato** |
| 4 | Design (a varianti, oppure diretto da `assets/`) | worker forti in parallelo (varianti) o uno solo (diretto) | `design/definitivo/` | **sì: design approvato** |
| 5 | Scrittura per parti | worker in parallelo | `testo/parte-N.md` + fonti | — |
| 6 | Revisione di fedeltà | worker forte per parte | testo corretto | — |
| 7 | Impaginazione, revisione grafica, assemblaggio, rifinitura | worker | `finale/` | — |
| 8 | Verifiche finali e consegna | tu | PDF + HTML | **sì: consegna** |

### 0. Pianificazione — [references/01-pianificazione.md](references/01-pianificazione.md)
Fai le domande a giri (AskUserQuestion, 1–4 per volta, opzione consigliata per prima), solo quelle a cui la richiesta non risponde già. Al primo giro: c'è già il testo trascritto delle lezioni? Al giro grafica: varianti di design o design diretto da `assets/`? Scrivi `CONTESTO.md` dal modello `templates/briefs/CONTESTO.md` e un piano di 4–5 righe con fasi e modelli.
**Fatto quando:** ogni domanda della lista ha una risposta scritta in `CONTESTO.md` (data dalla richiesta o dall'utente) e l'utente ha approvato il piano.

### 1. Estrazione — [references/02-estrazione.md](references/02-estrazione.md)
`scripts/estrai-testo.sh` (PDF → testo, conteggio parole), `scripts/estrai-pptx.py` (slide pptx → immagini + testo + note relatore), `scripts/estrai-pdf-slide.py` (slide in PDF → immagini + testo, stesso formato), `scripts/foglio-immagini.py` (contact sheet). Audio/video senza testo: serve la trascrizione (vedi reference).
**Fatto quando:** ogni fonte ha il suo testo non vuoto e ogni slide è nell'indice con le sue immagini.

### 2. Mappa — [references/03-mappa.md](references/03-mappa.md)
Un riassunto per trascrizione, strategia visual (cosa diventa grafica), lettura delle slide, risoluzione dei dubbi, ricerche esterne solo per chiarire.
**Fatto quando:** ogni dubbio segnalato nei riassunti ha uno stato (RISOLTO / PARZIALE / NON RISOLVIBILE) in `mappa/dubbi-risolti.md`.

### 3. Revisione logica — [references/04-revisione-logica.md](references/04-revisione-logica.md)
Un revisore su modello frontier cerca contraddizioni, errori, buchi per il principiante, rischi, e propone l'**indice definitivo con le fonti per capitolo**.
**Cancello:** mostri l'indice all'utente; si scrive solo su indice approvato.

### 4. Design — [references/05-design.md](references/05-design.md)
Due percorsi, scelti in fase 0. **(a) A varianti** (primo manuale o brand nuovo): 7 pagine campione con contenuto fisso → 3–4 varianti dello stesso tema → l'utente sceglie o mescola → variante definitiva con `COMPONENTI.md`. **(b) Diretto** (manuali piccoli o successivi): 7 pagine campione → variante definitiva direttamente da `assets/`, senza varianti. Base: `assets/` di questa skill.
**Cancello:** l'utente approva la variante definitiva guardando le PNG.

### 5. Scrittura — [references/06-scrittura.md](references/06-scrittura.md)
Un worker per parte, in parallelo, con marcatori `[[GRAFICA]]`/`[[FOTO]]`, box *Errore comune* / *Dal campo* / *Attenzione*, file fonti separato, regole di voce anti-IA (più humanizer se installata), divieti.
**Fatto quando:** ogni capitolo dell'indice approvato esiste, con titolo identico, e ogni affermazione con numeri o procedure ha una riga nel file fonti.

### 6. Revisione di fedeltà — [references/07-revisione-fedelta.md](references/07-revisione-fedelta.md)
Un revisore forte per parte corregge direttamente il testo sulle fonti e lo asciuga (−20/−30% di parole).
**Fatto quando:** ogni parte ha il suo `mappa/revisione-parte-N.md` e `scripts/controlla-divieti.py` non trova nulla.

### 7. Impaginazione — [references/08-impaginazione.md](references/08-impaginazione.md)
Per parte: frammento HTML → revisione grafica. Poi assemblaggio (`scripts/build.sh`, indice a due passate) e rifinitura (HTML autoconsistente, test del lettore principiante).
**Fatto quando:** `build.sh` chiude con indice stabile e ogni parte ha il suo `mappa/grafica-parte-N.md`.

### 8. Verifiche finali e consegna — [references/verifiche.md](references/verifiche.md)
Font, divieti, ispezione visiva personale di ogni pagina, indice a campione, HTML spostato altrove.
**Fatto quando:** ogni voce della checklist finale di `verifiche.md` è spuntata; consegni percorsi, numero pagine e punti lasciati prudenti.

## Cartella di progetto

Tutti i percorsi sono relativi alla cartella che l'utente sceglie per il progetto:

```
<progetto>/
  CONTESTO.md      regole comuni lette da ogni worker
  sorgenti/        PDF, pptx, foto originali (non si modificano mai)
  testo/           trascrizioni estratte; parte-N.md e parte-N-fonti.md
  slide/           img/, indice-slide.md, contact/
  mappa/           BRIEF-*.md, riassunti, strategia visual, dubbi, revisione logica, revisioni
  design/          campione-contenuti.md, variante-N/, definitivo/
  finale/          parte-N.html/.css, manuale.json, <Manuale>.html e .pdf
```

Prima di tutto: `sh <cartella-skill>/scripts/controlla-strumenti.sh` (dice cosa installare). `<cartella-skill>` è dove la skill è installata (di solito `~/.claude/skills/guida-da-trascrizione`): è il valore di `{{SKILL}}` nei brief. In questo documento `scripts/…` e `assets/…` sono relativi a quella cartella.

## Riferimenti

- Errori già fatti e come evitarli: [references/errori-noti.md](references/errori-noti.md) — leggilo prima della fase 4.
- Sistema grafico: `assets/COMPONENTI.md`, `assets/stile.css`, esempio completo in `assets/esempio/index.html`.
- Script: `scripts/` (ognuno ha l'uso in testa al file).
