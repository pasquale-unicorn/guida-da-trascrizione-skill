# Funzioni comuni agli script shell (si include con: . "$(dirname "$0")/_comune.sh").

# Trova Chrome/Chromium: variabile CHROME, poi percorso macOS, poi PATH.
trova_chrome() {
  if [ -n "$CHROME" ] && [ -x "$CHROME" ]; then echo "$CHROME"; return 0; fi
  for c in "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
           "/Applications/Chromium.app/Contents/MacOS/Chromium"; do
    [ -x "$c" ] && { echo "$c"; return 0; }
  done
  for c in google-chrome chromium chromium-browser; do
    command -v "$c" >/dev/null 2>&1 && { command -v "$c"; return 0; }
  done
  echo "Chrome non trovato: installa Google Chrome o imposta CHROME=/percorso/chrome" >&2
  return 1
}

# Stampa un HTML in PDF con Chrome headless (formato e margini li decide il CSS @page).
# --virtual-time-budget lascia a Chrome il tempo di caricare font e immagini prima di stampare.
stampa_pdf() {   # stampa_pdf <file.html> <file.pdf>
  chrome=$(trova_chrome) || return 1
  html_abs=$(cd "$(dirname "$1")" && pwd)/$(basename "$1")
  "$chrome" --headless=new --disable-gpu --no-pdf-header-footer --virtual-time-budget=10000 \
    --print-to-pdf="$2" "file://$html_abs" 2>/dev/null
  [ -s "$2" ] || { echo "PDF non prodotto: $2" >&2; return 1; }
}

richiedi() {     # richiedi <comando> <come installarlo>
  command -v "$1" >/dev/null 2>&1 || { echo "Manca $1. Installa: $2" >&2; return 1; }
}
