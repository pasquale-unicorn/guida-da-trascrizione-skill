#!/bin/sh
# Controllo stalli dei worker Orca: per ogni worker attivo stampa dispatch, modello e le ultime
# righe del suo terminale. Un worker fermo su "Usage limit reached", su una domanda o su un
# prompt di permesso non manda escalation: si vede solo qui.
# Uso: stalli.sh <run-id>      (il run-id lo restituisce `orca orchestration run-start` / worker-list)
RUN=${1:?uso: stalli.sh <run-id>}
command -v orca >/dev/null || { echo "orca non installato: con l'Agent tool usa la lista dei task" >&2; exit 1; }
orca orchestration worker-list --run "$RUN" --json | python3 -c '
import json, sys
for w in json.load(sys.stdin)["result"]["workers"]:
    if w["terminalState"] == "active":
        modello = (w.get("projection") or {}).get("provider", {}).get("model")
        print(w["dispatchId"], w["agentTerminalHandle"], modello)' | while read d t m; do
  coda=$(orca terminal read --terminal "$t" --json 2>/dev/null | python3 -c '
import json, sys
righe = json.load(sys.stdin)["result"]["terminal"].get("tail") or []
print(" / ".join(x.strip() for x in righe[-6:] if x.strip())[:300])' 2>/dev/null)
  echo "$d $m :: $coda"
done
