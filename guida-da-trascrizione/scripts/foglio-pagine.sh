#!/bin/sh
# Foglio di controllo di un PDF: tutte le pagine in miniatura, 8 per immagine (4 x 2).
# Uso: foglio-pagine.sh <file.pdf> <uscita.png>
# Con più di 8 pagine produce <uscita>-01.png, -02.png, ... Serve per la vista d'insieme
# (ritmo, pagine vuote, pagine piene); il controllo dettagliato si fa sulle PNG a piena risoluzione.
. "$(dirname "$0")/_comune.sh"
PDF=${1:?uso: foglio-pagine.sh <file.pdf> <uscita.png>}; OUT=${2:?manca il file di uscita}
richiedi pdftoppm "brew install poppler" || exit 1
richiedi ffmpeg "brew install ffmpeg" || exit 1
T=$(mktemp -d)
pdftoppm -png -scale-to-x 500 -scale-to-y 707 "$PDF" "$T/p"
N=$(find "$T" -name 'p-*.png' | wc -l | tr -d ' ')
base=${OUT%.png}
if [ "$N" -le 8 ]; then
  ffmpeg -loglevel error -y -pattern_type glob -i "$T/p-*.png" \
    -vf "pad=520:727:10:10:gray,tile=4x2" -frames:v 1 "$OUT"
  echo "$N pagine -> $OUT"
else
  ffmpeg -loglevel error -y -pattern_type glob -i "$T/p-*.png" \
    -vf "pad=520:727:10:10:gray,tile=4x2" "$base-%02d.png"
  echo "$N pagine -> $base-01.png ... ($(( (N + 7) / 8 )) fogli)"
fi
rm -r "$T"
