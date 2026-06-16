
import gymnasium as gym
from gymnasium import spaces


import numpy as np


class SnakeEnv(gym.Env):

    metadata = {"render_modes": ["human", None]}
    total_step=0

    def __init__(self, game, render: bool = False):
        self.game = game
        self.render_enabled = render
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(
            low=0, high=25, shape=(4,), dtype=np.float32
        )
        self.episode = 0
        self.steps = 0

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        self.game.reset()

        self.episode += 1
        self.steps = 0

        obs = np.array(self.game.get_state(), dtype=np.float32)

        return obs, {}

   
    def step(self, action):

        if action == 0:
            self.game.move_left()
        elif action == 1:
            self.game.move_right()
        elif action == 2:
            self.game.move_up()
        elif action == 3:
            self.game.move_down()

        self.game.update()

        self.steps += 1
        SnakeEnv.total_step += 1
        obs = np.array(self.game.get_state(), dtype=np.float32)

        reward = self.game.get_reward()

        done = self.game.is_done()

        if self.render_enabled:
            self.game.overlay_lines = [
                f"Episode: {self.episode}",
                f"Steps: {self.steps}",
                f"Total Steps: {SnakeEnv.total_step}",
                f"Last reward: {reward:.2f}",
            ]
            self.game.render()


        return obs, reward, done, False, {}

    def close(self):
        self.game.close()
        super().close()
