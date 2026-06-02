#!/usr/bin/env bash
# Run a script from this project inside its own .venv.
# Creates the environment first (via ./setup.sh) if it doesn't exist yet.
# Usage:  ./run.sh <script.py> [args...]
set -euo pipefail
cd "$(dirname "$0")"

# Ensure the environment exists.
if [ ! -x .venv/bin/python ]; then
  echo ">> No .venv yet — running setup first ..."
  ./setup.sh
fi

# No script given? Show what's available.
if [ $# -eq 0 ]; then
  echo "Usage: ./run.sh <script.py> [args...]"
  echo "Available scripts in this project:"
  ls *.py 2>/dev/null | sed 's/^/  - /' || echo "  (none found)"
  exit 1
fi

exec .venv/bin/python "$@"
