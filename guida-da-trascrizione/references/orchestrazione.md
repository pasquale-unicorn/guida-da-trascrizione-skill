# Orchestrazione: come delegare

Il coordinatore tiene il contesto **pulito**: non legge trascrizioni, slide intere o frammenti HTML. Delega lettura e scrittura ai worker, legge solo gli esiti (worker_done, report brevi in `mappa/`) e **verifica gli artefatti** di persona (PNG, grep, confronti a campione).

## 1. Rileva l'ambiente

`scripts/controlla-strumenti.sh` dice se ci sono `orca` e `codex`.

| Ambiente | Come si delega |
|---|---|
| CLI `orca` presente | Worker Orca supervisionati (skill `orchestration` per i comandi esatti: run, worker-start, check, ask). Worker Claude e Codex **bilanciati**, circa metà e metà |
| Niente Orca | Agent tool di Claude Code (subagent `general-purpose`), in background, più chiamate nello stesso messaggio per il parallelo. Stessi brief, stesse regole |

I brief sono identici nei due casi: cambia solo il comando di avvio e il modo di ricevere l'esito.

### Senza Orca: Agent tool di Claude Code, passo per passo

1. Avvio: una chiamata Agent per worker, `subagent_type: general-purpose`, `run_in_background: true`, parametro `model` secondo la tabella dei modelli (`haiku` economico, `sonnet` medio, `opus` forte/frontier). Per il parallelo metti **più chiamate Agent nello stesso messaggio**. Prompt = "Leggi ed esegui `<progetto>/mappa/BRIEF-<nome>.md`" + parte assegnata. Il subagent non conosce il progetto: il brief deve bastare.
2. Esito: il "worker_done" è l'ultimo messaggio del subagent (arriva come notifica quando finisce). Nel brief, dove c'è scritto "worker_done", vale "messaggio finale". Un subagent non può farti domande a metà lavoro: nei brief aggiungi "se hai un dubbio, non fermarti: scegli l'opzione più prudente e annotalo in fondo al report". Le domande le raccogli tu e le fai all'utente a blocchi.
3. Stalli: niente `attendi.sh` né `stalli.sh` (richiedono `orca`). Dopo l'avvio non fare polling a vuoto: aspetta le notifiche; se un worker sembra fermo, controlla che il suo file di output esista e cresca (`ls -l`, `wc -w`) e rilancia con "riprendi da: <file esistente>".
4. Codex: non c'è. Tutti i worker sono Claude; per "scrittore e revisore diversi" usa due modelli diversi (es. sonnet scrive, opus rivede).
5. Mai due worker sullo stesso file di output: ogni brief nomina i file che può scrivere.

## 2. Brief su file, sempre prima

1. Copia il modello da `templates/briefs/` in `<progetto>/mappa/BRIEF-<nome>.md` e sostituisci i segnaposto `{{...}}`.
2. Controlla che il file sia salvato (`ls`), poi avvia il worker.
3. Messaggio di avvio corto: "Leggi ed esegui `<progetto>/mappa/BRIEF-<nome>.md`" + parte assegnata (es. "PARTE 3"). Mai il brief solo nel messaggio: se il worker si ferma e va rilanciato, il brief deve esistere.

Ogni brief dice: cartella di lavoro, cosa leggere prima (`CONTESTO.md`), input, output (un file o una cartella, nient'altro da toccare), vincoli, **criterio di accettazione** e cosa scrivere nel worker_done.

## 3. Scelta dei modelli

| Tipo di lavoro | Livello | Esempi Claude | Esempi Codex/GPT |
|---|---|---|---|
| Meccanico: estrazione, render, rinomine, riassunto per sezioni fisse | economico | haiku, sonnet | modello "mini/luna" |
| Scrittura, impaginazione, revisione grafica | medio | sonnet | modello workhorse ("sol") |
| Giudizio: strategia visual, dubbi, design, revisione di fedeltà, rifinitura | forte | opus | modello forte ("astra"), effort alto |
| Revisione logica dell'intera mappa | frontier | opus, effort alto | modello frontier, effort alto |

I nomi dei modelli cambiano: controlla quelli disponibili prima di scrivere il piano, e **dichiara nel piano il modello di ogni worker**. Il modello di punta su lavoro meccanico è spreco. Scrittore e revisore della stessa parte su modelli o fornitori diversi.

## 4. Fan-out per fase

| Fase | Worker in parallelo |
|---|---|
| 2 Mappa | 1 per trascrizione + 1 strategia visual; poi 2 per le slide; poi 1 dubbi |
| 3 Revisione logica | 1 |
| 4 Design | 1 campione, poi 3–4 varianti, poi 1 definitiva (design diretto: 1 campione, poi 1 definitiva) |
| 5–6 Scrittura e revisione | 1 per parte (scrittura), poi 1 per parte (revisione) |
| 7 Impaginazione | 1 per parte, poi 1 revisione grafica per parte, poi 1 assemblaggio, 1 rifinitura |

Una parte può passare alla revisione appena il suo scrittore ha finito: non serve aspettare tutte le altre.

## 5. Loop di controllo e stalli

Il coordinatore non aspetta solo il worker_done. **Ogni ≤15 minuti** fa il controllo stalli:

- Orca: `scripts/attendi.sh <run-id>` (attende messaggi veri, conferma gli heartbeat, torna dopo 15 minuti comunque) e `scripts/stalli.sh <run-id>` (ultime righe del terminale di ogni worker attivo).
- Agent tool: controlla lo stato dei task in background e i file di output (esistono? crescono?).

Segnali di stallo e cosa fare:

| Segnale | Azione |
|---|---|
| Terminale con "Usage limit reached" (Codex senza quota) | Il worker non manderà mai escalation. Fermalo e rilascialo (worker-stop + worker-release), rilancia lo stesso brief su Claude |
| Worker fermo su una domanda o un prompt di permesso | Rispondi tu se puoi; altrimenti ferma e rilancia con il dubbio sciolto nel brief |
| Nessun heartbeat e terminale immobile da >15 minuti | Leggi il terminale, poi ferma e rilancia |
| Output parziale scritto, worker morto | Rilancia con "riprendi da: <file esistente>" nel messaggio |

Dopo ogni worker_done: **verifica l'artefatto** (vedi `verifiche.md`), non il resoconto del worker.

## 6. Domande all'utente durante il lavoro

Raccogli i dubbi dei worker e falli all'utente a blocchi (AskUserQuestion), non uno alla volta. Se sei tu stesso un worker di un coordinatore Orca, ogni domanda passa da `orca orchestration ask`.
