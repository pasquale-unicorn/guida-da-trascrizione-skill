#!/bin/sh
# Estrae il testo delle trascrizioni: sorgenti/*.pdf -> testo/*.txt (pdftotext); copia .txt/.md/.srt/.vtt.
# Poi conta le parole di ogni file e segnala i file vuoti.
# Uso: estrai-testo.sh <cartella-progetto>
. "$(dirname "$0")/_comune.sh"
P=${1:?uso: estrai-testo.sh <cartella-progetto>}
richiedi pdftotext "brew install poppler" || exit 1
mkdir -p "$P/testo"
for f in "$P"/sorgenti/*; do
  [ -f "$f" ] || continue
  base=$(basename "$f"); nome=${base%.*}
  case "$base" in
    *.pdf|*.PDF) pdftotext -enc UTF-8 "$f" "$P/testo/$nome.txt" ;;
    *.txt|*.md|*.srt|*.vtt) cp "$f" "$P/testo/$base" ;;
  esac
done
echo "Parole per file:"
totale=0
for t in "$P"/testo/*; do
  case "$t" in */parte-*) continue ;; esac
  [ -f "$t" ] || continue
  n=$(wc -w < "$t" | tr -d ' '); totale=$((totale + n))
  printf '%8s  %s\n' "$n" "$(basename "$t")"
  [ "$n" -eq 0 ] && echo "  ATTENZIONE: file vuoto: chiedi all'utente la fonte giusta" >&2
done
echo "Totale: $totale parole"
if [ "$totale" -lt 10000 ]; then echo "Corpus piccolo (<10k parole): il coordinatore può leggerlo da sé."
else echo "Corpus grande: le trascrizioni le leggono solo i worker."; fi
