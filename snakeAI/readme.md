# Grid Runner RL Project (Pygame + Gymnasium + Stable-Baselines3)

This repository is an educational project for learning **Reinforcement Learning (RL)** with a custom game written in **Pygame**.

Students build the game and define:
- **Actions** (what the agent can do)
- **State / Observation** (what the agent “sees”)
- **Reward** (feedback signal for learning)
- **Done** (when an episode ends)

Then a ready-made RL library (**Stable-Baselines3**) trains an agent to play the students’ game.

---

## Learning Objectives

By the end of this project, students should be able to:
- Explain the RL loop: **state → action → reward → next state**
- Build a small Pygame game using clean game logic
- Wrap the game into a **Gymnasium environment** (`reset()` / `step()`)
- Train an RL agent with **PPO** (Stable-Baselines3)
- Compare **manual play**, **heuristics**, and **RL**
- Connect Grid-based games to **Graph Theory** (cells as nodes, moves as edges)

---

## Recommended Folder Structure

```
grid_runner_project/
│
├── requirements.txt
├── train.py
├── play.py
├── manual_play.py
│
├── game/
│   └── grid_runner_game.py
│
└── rl/
    └── grid_runner_env.py
```

### What each file does

- `game/grid_runner_game.py`  
  The Pygame game: player, goal, obstacles, score, rendering.  
  Must provide: `move_left/right/up/down`, `update()`, `get_state()`, `get_reward()`, `is_done()`, `render()`.

- `rl/grid_runner_env.py`  
  Gymnasium wrapper that connects RL to the game.  
  Implements `reset()` and `step(action)` and defines `action_space` and `observation_space`.

- `train.py`  
  Trains a PPO model and saves it (example name: `grid_runner_model.zip`).

- `play.py`  
  Loads a saved model and lets it play automatically.

- `manual_play.py`  
  Human plays using keyboard (arrows / WASD).

---

## Requirements

- Python 3.10+ recommended

Install dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Example `requirements.txt`:

```txt
pygame
numpy
gymnasium
stable-baselines3
```

---

## How to Run

### 1) Manual Play (Human)

```bash
python manual_play.py
```

Controls (recommended):
- Arrow keys or **WASD**
- **R** to reset after game over / finish

---

### 2) Train the AI Agent

```bash
python train.py
```

Training notes:
- If you render during training (Pygame window open), training will be slower but easier to understand.
- If you disable rendering, training can be much faster.

---

### 3) Watch the Trained Agent Play

```bash
python play.py
```

---

## Game Rules (Grid Runner)

- The world is a grid (e.g., 15×15, 20×20, etc.)
- The player starts in a start cell
- The goal is to reach the **Goal cell**
- Some cells are blocked as **Obstacles/Walls**
- The agent can move in 4 directions:
  - Left / Right / Up / Down
- Episode ends if:
  - The player reaches the goal (success)
  - The player hits a wall/obstacle (failure) *(depending on your design)*
  - (Optional) Step limit exceeded

---

## RL Interface Contract (Must Implement)

### Actions
Your environment must expose 4 discrete actions:

- `0`: left
- `1`: right
- `2`: up
- `3`: down

Mapping is done inside `grid_runner_env.py`.

### State / Observation
Minimum recommended state:

```
[player_x, player_y, goal_x, goal_y]
```

This is a **vector of 4 numbers** (use `np.float32`).

### Reward (recommended baseline)
- `+1` when reaching the goal
- `-1` when failing (collision / forbidden move / etc.)
- `-0.01` for each normal step (encourages shorter paths)

### Done
Return `done=True` when the episode ends (success or failure).

---

## Student Tasks (Implementation Requirements)

1. Build the Grid Runner game in Pygame:
   - Grid drawing
   - Player (one cell)
   - Goal cell
   - Obstacles
   - Keyboard support for manual play

2. Implement the RL interface:
   - `get_state()`
   - `get_reward()`
   - `is_done()`
   - Action functions: `move_left/right/up/down`

3. Create a Gymnasium wrapper (`grid_runner_env.py`):
   - `action_space = Discrete(4)`
   - `observation_space = Box(..., shape=(4,), dtype=np.float32)`
   - `reset()` and `step(action)`

4. Train and save a model:
   - `model = PPO("MlpPolicy", env, verbose=1)`
   - `model.learn(...)`
   - `model.save("grid_runner_model")`

5. Load and play with the trained model:
   - `model = PPO.load("grid_runner_model")`
   - `model.predict(obs, deterministic=True)`

---

## Research Assignment (2–4 pages, required)

Submit a short report answering these sections:

### 1) System Pipeline (End-to-end explanation)
Explain the flow:
- game → env → model → action → env.step → reward/state
Include a simple block diagram.

### 2) State Representation
- What did you include in the state and why?
- What did you exclude and why?
- Is your state sufficient for solving the task?

### 3) Reward Design (Reward Shaping)
- Describe your reward function.
- Try at least **two** reward variants and compare results.
  Examples:
  - stronger step penalty
  - reward for moving closer to the goal
  - penalty for moving away

### 4) Compare 3 approaches
Compare:
1. Manual control (human)
2. A rule-based heuristic (greedy / shortest-path)
3. RL trained agent (PPO)

Discuss pros/cons and performance.

### 5) Graph Theory Connection
Explain why Grid Runner is a graph problem:
- Cells = vertices (nodes)
- Legal moves = edges
- Obstacles = blocked vertices/edges
Compare **BFS/A\*** vs **RL**:
- BFS/A\* finds paths using explicit search
- RL learns a policy from rewards through experience

### 6) Limitations + Ethics
Pick at least one:
- What happens if the environment changes?
- Does the agent “understand” or “pattern match”?
- Reward hacking: can the agent exploit your reward function?

### 7) Results
Include evidence:
- average steps to goal after training
- number of successes/failures
- screenshot(s) or short description of behavior

---

## Bonus Ideas (Optional)

- Moving obstacles (dynamic environment)
- Coins to collect (multi-objective reward)
- Richer state: danger ahead/left/right, direction, distances
- Plot training progress (reward over episodes)
- Compare PPO vs DQN

---

## Troubleshooting

### VSCode import warning (Pylance: reportMissingImports)
- Open the **project root folder** in VSCode
- Ensure `__init__.py` exists in `game/` and `rl/`
- Select the correct interpreter:
  `Ctrl+Shift+P → Python: Select Interpreter`

### Training is slow
- Disable rendering in training:
  - create game with `render=False`
  - create env with `render=False`

---

## Educational Use

This project is intended for classroom / educational use.
Students are encouraged to modify game rules, state, and rewards and analyze the effects.
