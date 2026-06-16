import pygame
from Game.snake_game import SnakeGame

game = SnakeGame(render=True, fps=15)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_LEFT, pygame.K_a):
                game.move_left()
            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                game.move_right()
            elif event.key in (pygame.K_UP, pygame.K_w):
                game.move_up()
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                game.move_down()
            elif event.key == pygame.K_r:
                game.reset()

    if not game.is_done():
        game.update()
        game.overlay_lines = ["Manual Mode", "Arrows/WASD to move", "R = reset"]
    else:
        game.overlay_lines = ["GAME OVER", "Press R to restart"]

    game.render()

game.close()
