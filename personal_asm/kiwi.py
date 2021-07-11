import pygame
import pygame.sprite
import pygame.image

class Kiwi(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.kiwi_sprites = []
        self.kiwi_sprites.append(pygame.image.load('images/kiwi_0.png'))
        self.kiwi_sprites.append(pygame.image.load('images/kiwi_1.png'))
        self.kiwi_sprites.append(pygame.image.load('images/kiwi_2.png'))
        self.kiwi_sprites.append(pygame.image.load('images/kiwi_3.png'))
        self.kiwi_sprites.append(pygame.image.load('images/kiwi_4.png'))
        self.kiwi_sprites.append(pygame.image.load('images/kiwi_5.png'))
        self.kiwi_sprites.append(pygame.image.load('images/kiwi_6.png'))
        self.kiwi_sprites.append(pygame.image.load('images/kiwi_7.png'))
        self.kiwi_sprites.append(pygame.image.load('images/kiwi_8.png'))
        self.kiwi_sprites.append(pygame.image.load('images/kiwi_9.png'))
        self.kiwi_sprites.append(pygame.image.load('images/kiwi_10.png'))
        self.kiwi_sprites.append(pygame.image.load('images/kiwi_11.png'))
        self.kiwi_sprites.append(pygame.image.load('images/kiwi_12.png'))
        self.kiwi_sprites.append(pygame.image.load('images/kiwi_13.png'))
        self.kiwi_sprites.append(pygame.image.load('images/kiwi_14.png'))
        self.kiwi_sprites.append(pygame.image.load('images/kiwi_15.png'))
        self.kiwi_sprites.append(pygame.image.load('images/kiwi_16.png'))

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