
from stable_baselines3 import PPO

from Game.snake_game import SnakeGame

from RL.snake_env import SnakeEnv

game = SnakeGame(render=True, fps=20)

env = SnakeEnv(game, render=True)

model = PPO.load("snake_model")

obs, _ = env.reset()


while True:

    action, _ = model.predict(obs, deterministic=True)

    obs, reward, done, _, _ = env.step(action)

    if done:
        obs, _ = env.reset()
