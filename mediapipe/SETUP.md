# mediapipe — setup & run

Hand / face landmark demos and small games built on
[MediaPipe](https://github.com/google/mediapipe).

## Quick start

```bash
./setup.sh                # installs uv (if missing) + Python 3.12 + dependencies into .venv
./run.sh app.py           # hand tracking
./run.sh index.py         # hand landmark demo
./run.sh snake.py         # gesture-controlled snake
./run.sh flappyBird.py    # gesture-controlled flappy bird
```

`setup.sh` is automatic and safe to re-run. It installs [`uv`](https://astral.sh/uv)
if needed, and `uv` downloads **Python 3.12** for you if it's missing.

## Notes
- Requires a **webcam** and a **display** (OpenCV / pygame windows).
- **Version pin matters:** mediapipe **≥ 0.10.30 removed the legacy `mp.solutions`
  API** (slim, tasks-only builds). Every script here uses `mp.solutions.hands`,
  so `requirments.txt` pins `mediapipe>=0.10.14,<0.10.30`. Don't unpin it.
- This project deliberately does **not** include TensorFlow: mediapipe requires
  `protobuf<5` while TensorFlow ≥ 2.20 requires `protobuf>=5.28` — they can't
  coexist in one environment, and the scripts don't use TensorFlow.

## Windows / manual
```bash
uv venv --python 3.12 .venv
uv pip install --python .venv -r requirments.txt
.venv\Scripts\python app.py
```
