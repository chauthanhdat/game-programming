import pygame
import pygame.display
import pygame.time

import setting
from game_state import GameState

# Set up
pygame.init()
pygame.display.set_caption(setting.TITLE)

clock = pygame.time.Clock()
game_state = GameState()

run = True
while run:
    game_state.state_manger()
    pygame.display.flip()
    clock.tick(setting.FPS)