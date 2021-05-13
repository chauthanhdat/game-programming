import pygame
import pygame.sprite
import pygame.image

class Kiwi(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.kiwi_sprites = []
        self.kiwi_sprites.append(pygame.image.load('kiwi_0.png'))
        self.kiwi_sprites.append(pygame.image.load('kiwi_1.png'))
        self.kiwi_sprites.append(pygame.image.load('kiwi_2.png'))
        self.kiwi_sprites.append(pygame.image.load('kiwi_3.png'))
        self.kiwi_sprites.append(pygame.image.load('kiwi_4.png'))
        self.kiwi_sprites.append(pygame.image.load('kiwi_5.png'))
        self.kiwi_sprites.append(pygame.image.load('kiwi_6.png'))
        self.kiwi_sprites.append(pygame.image.load('kiwi_7.png'))
        self.kiwi_sprites.append(pygame.image.load('kiwi_8.png'))
        self.kiwi_sprites.append(pygame.image.load('kiwi_9.png'))
        self.kiwi_sprites.append(pygame.image.load('kiwi_10.png'))
        self.kiwi_sprites.append(pygame.image.load('kiwi_11.png'))
        self.kiwi_sprites.append(pygame.image.load('kiwi_12.png'))
        self.kiwi_sprites.append(pygame.image.load('kiwi_13.png'))
        self.kiwi_sprites.append(pygame.image.load('kiwi_14.png'))
        self.kiwi_sprites.append(pygame.image.load('kiwi_15.png'))
        self.kiwi_sprites.append(pygame.image.load('kiwi_16.png'))

        self.kiwi = 0

        self.image = self.kiwi_sprites[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if self.kiwi < len(self.kiwi_sprites) - 1:
            self.kiwi += 1
        else:
            self.kiwi = 0
        
        self.image = self.kiwi_sprites[self.kiwi]