#!/bin/sh
# Ricostruisce il manuale finale (HTML autoconsistente + PDF) dai frammenti finale/parte-N.html.
# Uso: build.sh <cartella-progetto>
# Indice a due passate: stampa, assembla.py trova la pagina di ogni titolo con pdftotext,
# riscrive l'indice, ristampa; si ferma quando i numeri non cambiano più (max 4 giri).
. "$(dirname "$0")/_comune.sh"
QUI=$(cd "$(dirname "$0")" && pwd)
P=${1:?uso: build.sh <cartella-progetto>}
CONF="$P/finale/manuale.json"
[ -f "$CONF" ] || { echo "manca $CONF" >&2; exit 1; }
NOME=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1])).get("file","Manuale"))' "$CONF")
HTML="$P/finale/$NOME.html"; PDF="$P/finale/$NOME.pdf"

stampa() {
  python3 "$QUI/assembla.py" "$P" html || exit 1
  stampa_pdf "$HTML" "$PDF" || exit 1
}

rm -f "$P/finale/pagine.json"
giro=1
while :; do
  stampa
  python3 "$QUI/assembla.py" "$P" pagine && break     # exit 0 = numeri stabili
  [ "$giro" -ge 4 ] && { echo "indice non stabile dopo 4 giri" >&2; exit 1; }
  giro=$((giro + 1))
done

pdfinfo "$PDF" | grep -E 'Pages|Page size'
pdffonts "$PDF"
