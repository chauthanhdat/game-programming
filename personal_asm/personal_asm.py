import pygame
import pygame.display
import pygame.time

import setting
from game_state import GameState

# Set up
pygame.init()
clock = pygame.time.Clock()

pygame.display.set_caption(setting.TITLE)

game_state = GameState()

while True:
    game_state.state_manger()
    pygame.display.flip()
    clock.tick(setting.FPS)