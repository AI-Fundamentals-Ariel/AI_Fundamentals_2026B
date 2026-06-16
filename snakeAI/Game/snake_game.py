import pygame
import random

CELL = 25
GRID = 25
WIDTH = HEIGHT = CELL * GRID

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)


class SnakeGame:
   
    def __init__(self, render: bool = True, fps: int = 15):
        self.render_enabled = render
        self.fps = fps

        if self.render_enabled:
            pygame.init()
            self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
            pygame.display.set_caption("Snake (RL Training / Manual)")
            self.clock = pygame.time.Clock()
            self.font = pygame.font.SysFont(None, 28)
        else:
            self.screen = None
            self.clock = None
            self.font = None

        self.reset()

    def reset(self):
        self.snake = [(10, 10)]
        self.direction = (1, 0) 
        self.food = self._random_food()
        self.score = 0
        self.game_over = False

        self.last_reward = 0.0

        self.overlay_lines = []

    def close(self):
        if self.render_enabled:
            pygame.quit()

    def _random_food(self):
        while True:
            pos = (random.randint(0, GRID - 1), random.randint(0, GRID - 1))
            if pos not in self.snake:
                return pos

    def _set_direction(self, new_dir):
        dx, dy = self.direction
        ndx, ndy = new_dir
        if (dx, dy) == (-ndx, -ndy):
            return 
        self.direction = new_dir

    def move_left(self):
        self._set_direction((-1, 0))

    def move_right(self):
        self._set_direction((1, 0))

    def move_up(self):
        self._set_direction((0, -1))

    def move_down(self):
        self._set_direction((0, 1))

    def update(self):
        
        if self.game_over:
            self.last_reward = -1.0
            return

        hx, hy = self.snake[0]
        dx, dy = self.direction
        new_head = (hx + dx, hy + dy)

       
        if not (0 <= new_head[0] < GRID and 0 <= new_head[1] < GRID):
            self.game_over = True
            self.last_reward = -1.0
            return

   
        if new_head in self.snake:
            self.game_over = True
            self.last_reward = -1.0
            return

    
        self.snake.insert(0, new_head)

       
        if new_head == self.food:
            self.score += 1
            self.last_reward = 1.0
            self.food = self._random_food()
        else:
            self.snake.pop()
            self.last_reward = -0.01


    def get_state(self):
        hx, hy = self.snake[0]
        fx, fy = self.food
        return [hx, hy, fx, fy]

    def get_reward(self):
        return float(self.last_reward)

    def is_done(self):
        return self.game_over

    def render(self):
        
        if not self.render_enabled:
            return

        pygame.event.pump()

        self.screen.fill(BLACK)

        for x, y in self.snake:
            pygame.draw.rect(self.screen, GREEN, (x * CELL, y * CELL, CELL, CELL))

        fx, fy = self.food
        pygame.draw.rect(self.screen, RED, (fx * CELL, fy * CELL, CELL, CELL))

        y0 = 8
        score_surf = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_surf, (2, y0))
        y0 += 22

        for line in self.overlay_lines[:6]:
            surf = self.font.render(line, True, WHITE)
            self.screen.blit(surf, (2, y0))
            y0 += 22

        pygame.display.flip()
        self.clock.tick(self.fps)
