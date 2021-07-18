import pygame
import pygame.sprite
import pygame.image

from setting import *

class Button(pygame.sprite.Sprite):
    def __init__(self, file_name, y) -> None:
        super().__init__()
        self.image = pygame.image.load(file_name)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH/2 - self.rect.width/2
        self.rect.y = 32 * y

# class Button(pygame.sprite.Sprite):
#     def __init__(self, file_name) -> None:
#         super().__init__()
#         self.image = pygame.image.load('btn_new_game.png')
#         self.rect = self.image.get_rect()
#         self.rect.x = WIDTH/2 - self.rect.width/2
#         self.rect.y = 32 * 6

# class Button(pygame.sprite.Sprite):
#     def __init__(self, file_name) -> None:
#         super().__init__()
#         self.image = pygame.image.load('btn_new_game.png')
#         self.rect = self.image.get_rect()
#         self.rect.x = WIDTH/2 - self.rect.width/2
#         self.rect.y = 32 * 6