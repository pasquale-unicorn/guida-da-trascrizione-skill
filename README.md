# guida-da-trascrizione

Skill per **Claude Code** che trasforma trascrizioni di lezioni, corsi, audio o video (più slide e foto) in un documento PDF + HTML impaginato con il brand Unicorn.

Due modalità:

- **A — Lead magnet**: guida breve con funnel e CTA verso un evento, una lezione o una call.
- **B — Manuale operativo**: manuale lungo per chi deve imparare a fare, zero CTA. Percorso completo: pianificazione con domande → estrazione → mappa → revisione logica e indice → design (a varianti o diretto da assets/) → scrittura per parti → revisione di fedeltà → impaginazione, revisione grafica, assemblaggio, rifinitura → verifiche finali.

La skill guida Claude a **fare le domande giuste prima di partire**, a procedere fase per fase fermandosi ai cancelli di approvazione (piano, indice, design, consegna), a delegare il lavoro pesante a worker (Orca o subagent di Claude Code) e a verificare di persona ogni artefatto.

## Installazione

```sh
git clone <questo-repo>
cp -R guida-da-trascrizione ~/.claude/skills/
```

Claude Code la carica da sola: basta chiedere, per esempio, *"fammi un manuale operativo da queste trascrizioni"* o *"crea il PDF della lezione"*.

## Requisiti

macOS (gli script usano `sips`, incluso nel sistema) con:

| Strumento | A cosa serve | Installazione |
|---|---|---|
| Google Chrome | stampa HTML → PDF (headless), screenshot | sito di Google Chrome |
| poppler (`pdftotext`, `pdftoppm`, `pdffonts`, `pdfinfo`) | estrazione testo, PNG delle pagine, controllo font | `brew install poppler` |
| ffmpeg | foglio d'insieme delle pagine | `brew install ffmpeg` |
| python3 (solo libreria standard) | estrazione pptx, assemblaggio, controlli | `brew install python` |

Controllo rapido: `sh ~/.claude/skills/guida-da-trascrizione/scripts/controlla-strumenti.sh`.

Facoltativi:
- Whisper (`pip install openai-whisper`) per trascrivere audio/video quando manca il testo; la trascrizione va poi controllata a mano.
- CLI `orca` (Orca) per orchestrare worker Claude e Codex; senza Orca la skill usa i subagent di Claude Code.
- Skill `humanizer` (toglie i segni della scrittura da IA), una skill di voce del brand e un copywriter: se installate, vengono usate in scrittura. Senza, la skill ha comunque regole minime di voce e anti-scrittura da IA (`references/06-scrittura.md`).

## Esempio d'uso

```
Tu:     Ho 4 trascrizioni PDF di un corso e le slide in pptx. Mi serve un manuale per i corsisti.
Claude: (fase 0) domande a giri: modalità, pubblico, fonti da escludere, relatori,
        dati che cambiano, date e citazioni sì/no, sobrietà e densità della grafica...
        → CONTESTO.md + piano in 5 righe. Aspetta il tuo ok.
Claude: (fasi 1–3) estrae testo e slide, fa mappare le fonti ai worker, fa rivedere tutto
        a un revisore logico → ti mostra l'indice con le fonti per capitolo. Aspetta il tuo ok.
Claude: (fase 4) 3–4 varianti di design sulle stesse 7 pagine campione → scegli o mescoli.
        (per manuali piccoli o successivi: design diretto da assets/, senza varianti)
Claude: (fasi 5–8) scrittura, revisione di fedeltà, impaginazione, assemblaggio con indice
        a numeri di pagina veri, controlli → PDF + HTML autoconsistente in finale/.
```

## Struttura

```
guida-da-trascrizione/
  SKILL.md              entry point: modalità, regole d'oro, fasi con cancelli e criteri di completamento
  references/           una reference per fase + orchestrazione, verifiche, errori noti, modalità A
  templates/briefs/     i brief dei worker, con segnaposto {{...}}
  assets/               stile.css, Montserrat incorporato, loghi Unicorn, COMPONENTI.md (incluso il bottone CTA a pillola, solo modalità A), esempio/index.html
  scripts/              estrazione (pptx e PDF di slide), stampa, contact sheet, assemblaggio con indice a due passate, controlli, stalli
```

## Note

- Il sistema grafico è quello Unicorn. Per un altro brand: sostituisci loghi, palette in `assets/stile.css` e, se serve, il font (e la famiglia controllata da `scripts/controlla-font.py`).
- Montserrat è distribuito con licenza SIL Open Font License 1.1. I loghi Unicorn sono marchi del rispettivo titolare e non sono coperti dalla licenza del repository.
- `assets/esempio/index.html` viene da un progetto reale (manuale su affitti brevi): mostra tutti i componenti; in un progetto nuovo si tengono le strutture, non i testi.
