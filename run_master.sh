#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 1 ]; then
  echo "Usage: $0 <script.py>"
  exit 1
fi

SCRIPT="$1"

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR/python"

# Use the same python3 on PATH; master_run.py uses sys.executable internally.
python3 master_run.py "$SCRIPT"
