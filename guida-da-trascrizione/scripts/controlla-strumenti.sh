#!/bin/sh
# Controlla gli strumenti usati dalla pipeline e dice cosa installare (macOS + Homebrew).
. "$(dirname "$0")/_comune.sh"
ok=0
richiedi python3   "brew install python (o Xcode Command Line Tools)" || ok=1
richiedi pdftotext "brew install poppler" || ok=1
richiedi pdftoppm  "brew install poppler" || ok=1   # serve anche a estrai-pdf-slide.py
richiedi pdffonts  "brew install poppler" || ok=1
richiedi pdfinfo   "brew install poppler" || ok=1
richiedi ffmpeg    "brew install ffmpeg   (serve per il foglio delle pagine)" || ok=1
richiedi sips      "è incluso in macOS; su altri sistemi adatta gli script a ImageMagick" || ok=1
trova_chrome >/dev/null || ok=1
if command -v orca >/dev/null 2>&1; then echo "orca: presente (orchestrazione con worker Orca)"
else echo "orca: assente (orchestrazione con l'Agent tool di Claude Code)"; fi
if command -v whisper >/dev/null 2>&1; then echo "whisper: presente (trascrizione facoltativa di audio/video)"
else echo "whisper: assente (facoltativo: pip install openai-whisper, solo se manca la trascrizione)"; fi
if command -v codex >/dev/null 2>&1; then echo "codex: presente"; else echo "codex: assente"; fi
if [ $ok = 0 ]; then echo "Strumenti OK"; else echo "Strumenti mancanti: vedi sopra" >&2; exit 1; fi
