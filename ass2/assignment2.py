import pygame, sys
import pygame.time

class GameState():
    def __init__(self):
        self.state = 'main_game'

    def main_game(self):
        pass

    def state_manager(self):
        if self.state == 'main_game':
            self.main_game()
            pass

pygame.init()
clock = pygame.time.Clock()

while True:
    clock.tick(60)
