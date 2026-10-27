# Task: estrazione meccanica delle slide

Cartella: {{PROGETTO}} — leggi prima `CONTESTO.md`.
Target: `sorgenti/{{FILE}}.pptx` (non modificarlo). Non estrarre i video.
Se le slide sono un PDF (`sorgenti/{{FILE}}.pdf`), al passo 1 usa `python3 {{SKILL}}/scripts/estrai-pdf-slide.py sorgenti/{{FILE}}.pdf slide`: nessuna nota relatore, nessun video.

1. `python3 {{SKILL}}/scripts/estrai-pptx.py sorgenti/{{FILE}}.pptx slide`
2. `python3 {{SKILL}}/scripts/foglio-immagini.py slide`
3. Apri due fogli in `slide/contact/` e controlla che le miniature si vedano e i nomi corrispondano.

Vincoli: lavora solo dentro `slide/`. Niente interpretazione dei contenuti.
Accettazione: numero di slide nell'indice = slide del pptx (o pagine del PDF), nell'ordine di presentazione; immagini estratte = immagini referenziate; fogli contact presenti.
worker_done: numero slide, immagini, slide con video, eventuali errori.
