#!/bin/sh
# Attende il prossimo messaggio vero dei worker Orca (worker_done, escalation, question),
# confermando in automatico le consegne fatte solo di heartbeat. Timeout di default: 15 minuti,
# così il coordinatore torna comunque a fare il controllo stalli (stalli.sh).
# Uso: attendi.sh <run-id> [timeout-ms]
RUN=${1:?uso: attendi.sh <run-id> [timeout-ms]}; TIMEOUT=${2:-900000}
fine=$(( $(date +%s) + TIMEOUT / 1000 ))
while [ "$(date +%s)" -lt "$fine" ]; do
  orca orchestration check --run "$RUN" --wait --types "worker_done,escalation,question" \
    --timeout-ms "$TIMEOUT" --json >/dev/null
  OUT=$(orca orchestration check --run "$RUN" --json | python3 -c '
import json, sys
r = json.load(sys.stdin).get("result", {})
msgs = r.get("messages", [])
veri = [m for m in msgs if m["type"] != "heartbeat"]
print(("VERO" if veri else ("HB" if msgs else "VUOTO")), r.get("deliveryId"))
for m in veri:
    print(m["type"], "|", m["subject"], "|", m["body"][:600])')
  case "$OUT" in
    VERO*) echo "$OUT"; exit 0 ;;
    HB*) orca orchestration check --run "$RUN" --ack "$(echo "$OUT" | head -1 | awk '{print $2}')" --json >/dev/null ;;
    *) break ;;
  esac
done
echo "Nessun messaggio entro il timeout: esegui stalli.sh $RUN"
exit 2
