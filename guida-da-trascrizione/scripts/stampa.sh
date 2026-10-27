#!/bin/sh
# Stampa un HTML in PDF (Chrome headless) e ne fa le PNG da guardare.
# Uso: stampa.sh <file.html> [dpi]  ->  <file>.pdf + png-<file>/pagina-NN.png, poi pdfinfo e pdffonts
. "$(dirname "$0")/_comune.sh"
H=${1:?uso: stampa.sh <file.html> [dpi]}; DPI=${2:-70}
richiedi pdftoppm "brew install poppler" || exit 1
dir=$(dirname "$H"); nome=$(basename "$H" .html)
pdf="$dir/$nome.pdf"; png="$dir/png-$nome"
stampa_pdf "$H" "$pdf" || exit 1
mkdir -p "$png"
find "$png" -name 'pagina-*.png' -delete
pdftoppm -r "$DPI" -png "$pdf" "$png/pagina"
pdfinfo "$pdf" | grep -E 'Pages|Page size'
pdffonts "$pdf"
echo "PNG in $png: guardale una per una."
