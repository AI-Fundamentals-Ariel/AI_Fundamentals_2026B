from stable_baselines3 import PPO
from Game.snake_game import SnakeGame
from RL.snake_env import SnakeEnv

TOTAL_TIMESTEPS = 200


game = SnakeGame(render=True, fps=20)
env = SnakeEnv(game, render=True)

model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=TOTAL_TIMESTEPS)

model.save("snake_model")

env.close()
print("Saved model: snake_model.zip")

