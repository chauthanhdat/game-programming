import pygame
import pygame.sprite
import pygame.image

class Trap(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.image = pygame.image.load('trap.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y