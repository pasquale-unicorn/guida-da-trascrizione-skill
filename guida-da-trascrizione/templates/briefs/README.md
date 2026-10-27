# Brief dei worker

Modelli generalizzati dai brief usati davvero. Per usarne uno:

1. copialo in `<progetto>/mappa/BRIEF-<nome>.md`;
2. sostituisci i segnaposto;
3. controlla che sia salvato, poi avvia il worker con: "Leggi ed esegui `<progetto>/mappa/BRIEF-<nome>.md`" (+ "PARTE N" o "VARIANTE N" dove serve).

Segnaposto:

| Segnaposto | Valore |
|---|---|
| `{{PROGETTO}}` | percorso assoluto della cartella di progetto |
| `{{SKILL}}` | percorso assoluto della cartella di questa skill |
| `{{FILE}}` | file di input specifico (es. una trascrizione) |
| `{{N}}` | numero di parte, riassunto o variante |
| `{{PAROLE_VIETATE}}` | parole decise in fase 0, separate da virgola (nomi dei relatori, mese/anno dell'evento, "corso", "docente"…) |
| `{{NUM_PARTI}}` | quante parti ha il documento (dall'indice approvato) |
| `{{TITOLO}}`, `{{NOME_FILE}}` | titolo del documento e nome dei file finali senza estensione (es. `Manuale`): vanno in `finale/manuale.json` |
| `{{DA}}`, `{{A}}` | primo e ultimo numero delle slide assegnate a un worker (es. 1 e 70) |
| `{{TEMA}}`, `{{tema}}` | argomento di una ricerca esterna e, in minuscolo con trattini, il nome del file di output |
| `{{VOCI_VARIABILI}}` | dati che cambiano nel tempo, decisi in fase 0 (costi, tassi, tariffe…) |
| `{{TITOLO_PROGETTO}}` | nome del progetto, solo in `CONTESTO.md` |
| `{{TEMPLATE_O_ESEMPIO}}` | riferimento grafico: percorso di un documento esistente o `{{SKILL}}/assets/esempio/index.html` |
| `{{NOME}}` | nome della direzione di una variante di design (es. "Libro editoriale") |
| `{{testo libero con spiegazione}}` | **valore proposto da adattare**: la frase tra doppie graffe è un default (di solito quello della modalità B). Tienila, cambiala secondo `CONTESTO.md` o cancellala, e togli sempre le graffe |
| `{{...}}` | altri segnaposto spiegati nel brief stesso |

Prima di avviare un worker cerca i segnaposto rimasti: `grep -n '{{' <brief>` deve dare zero righe.

| Fase | Brief | Modello |
|---|---|---|
| 0 | `CONTESTO.md` (non è un brief: è il file di regole comuni) | — |
| 1 | `slide-estrazione.md` | economico |
| 2 | `riassunto.md`, `visual.md`, `slide-lettura.md`, `dubbi.md`, `ricerca-esterna.md` | economico / forte / medio / forte / medio |
| 3 | `revisore-logico.md` | frontier |
| 4 | `campione.md`, `design-variante.md`, `design-definitivo.md` | medio / forte / forte |
| 5–6 | `scrittura.md`, `revisione-parte.md` | medio / forte |
| 7 | `impaginazione-parte.md`, `revisione-grafica.md`, `assemblaggio.md`, `rifinitura.md`, `lettore-principiante.md` | medio / medio / medio / forte / medio |

Ogni brief finisce con il criterio di accettazione e il contenuto del worker_done. Se aggiungi vincoli emersi in corsa (es. decisioni dell'utente sul design), scrivili nel brief come **vincolanti**, non solo nel messaggio.
