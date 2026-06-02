#!/usr/bin/env bash
# Self-contained setup for this project.
# Ensures `uv` is installed, then lets uv auto-download the right Python
# (from .python-version), create a local .venv, and install dependencies.
# Re-runnable: safe to run multiple times.
set -euo pipefail
cd "$(dirname "$0")"

# --- 1. Make sure uv is available (install it if missing) ---------------------
ensure_uv() {
  if command -v uv >/dev/null 2>&1; then return; fi
  echo ">> uv not found — installing (https://astral.sh/uv) ..."
  curl -LsSf https://astral.sh/uv/install.sh | sh
  # uv installs to ~/.local/bin (or ~/.cargo/bin on older installers)
  export PATH="$HOME/.local/bin:$HOME/.cargo/bin:$PATH"
  command -v uv >/dev/null 2>&1 || {
    echo "!! uv was installed but is not on PATH. Open a new terminal (or add"
    echo "   ~/.local/bin to PATH) and re-run ./setup.sh"; exit 1; }
}
ensure_uv

# --- 2. Pick the requirements file (this repo mixes requirements/requirments) --
REQ="$(ls requirements.txt requirments.txt 2>/dev/null | head -n1 || true)"
[ -n "$REQ" ] || { echo "!! No requirements file found in $(pwd)"; exit 1; }

PYVER="$(cat .python-version)"
echo ">> Using Python $PYVER (uv will download it if it's not installed)"

# --- 3. Create the venv with the pinned Python, then install deps -------------
uv venv --python "$PYVER" .venv
uv pip install --python .venv/bin/python -r "$REQ"

echo ""
echo ">> Setup complete. Environment: $(pwd)/.venv"
echo ">> Run a script with:  ./run.sh <script.py>   (no args = list scripts)"
