# deepface — setup & run

Live face **age / emotion** detection with [DeepFace](https://github.com/serengil/deepface).

## Quick start

```bash
./setup.sh            # installs uv (if missing) + Python 3.12 + dependencies into .venv
./run.sh age.py       # live age estimation from the webcam
./run.sh emotion.py   # live emotion detection from the webcam
```

`setup.sh` is automatic and safe to re-run. It installs [`uv`](https://astral.sh/uv)
if you don't have it, and `uv` then downloads **Python 3.12** for you if it's
missing — no system Python required.

## Notes
- Requires a **webcam** and a **display** (opens an OpenCV window; press `ESC` to quit).
- First run downloads the DeepFace model weights (~0.5 GB) to `~/.deepface/`.
- `deepface` pulls in a compatible **TensorFlow** automatically; `tf-keras` is
  required for TensorFlow ≥ 2.16.

## Windows / manual
```bash
uv venv --python 3.12 .venv
uv pip install --python .venv -r requirments.txt
.venv\Scripts\python age.py
```
