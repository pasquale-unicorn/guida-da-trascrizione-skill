# Task: variante di design {{N}} (7 pagine campione)

Cartella: {{PROGETTO}} — leggi prima `CONTESTO.md`.
Contenuto: `design/campione-contenuti.md` — usalo VERBATIM, non riscrivere i testi. Immagini: `slide/img/`.
Tema di partenza OBBLIGATORIO: `{{SKILL}}/assets/` (studia `esempio/index.html`, `stile.css`, `COMPONENTI.md`){{, e il riferimento: ...}}. La variante resta nello stesso tema e cambia l'impostazione.

**Direzione della variante {{N}} — {{NOME}}: {{descrizione in 2–3 righe}}.**
(Direzioni collaudate: manuale tecnico rifinito; libro editoriale; quaderno di campo / schede operative; visual-first con il metodo Visual Explainer — una figura = una frase, ogni numero un'immagine — ma nello stile del brand.)

Vincoli permanenti (verificati alla consegna):
- Montserrat INCORPORATO: `{{SKILL}}/assets/montserrat-embedded.css`. Verifica: `python3 {{SKILL}}/scripts/controlla-font.py <pdf>`.
- Logo vero: `{{SKILL}}/assets/logo-unicorn-*.png`. Mai la sola scritta.
- Testo in una colonna, ritmo da libro (tabelle e schemi possono avere colonne).
- A4 verticale, stampa pulita: margini, niente contenuti tagliati, niente pagine mezze vuote non volute. Mai margini negativi.
- Diagrammi in HTML/CSS o SVG inline, testo ≥9 pt, mai immagini sfocate.
- Foto reali da `slide/img/` con didascalia.
- {{Zero CTA, zero marketing (modalità B).}}
- {{Altri vincoli decisi in fase 0: sobrietà, densità, icone.}}

Output in `design/variante-{{N}}/`:
- `index.html` autonomo (percorsi relativi), 7 pagine di contenuto (anche più fogli A4 se serve aria).
- PDF: `sh {{SKILL}}/scripts/stampa.sh design/variante-{{N}}/index.html` (produce `index.pdf` e `png-index/`).
- `NOTE.md`: 5–8 righe sulle scelte e su cosa cambia rispetto al tema.

Prima del worker_done GUARDA tu stesso ogni PNG (non basta che il PDF esista) e correggi i difetti visibili. Scrivi solo in `design/variante-{{N}}/`.
Accettazione: PDF, font OK, PNG, NOTE.md.
