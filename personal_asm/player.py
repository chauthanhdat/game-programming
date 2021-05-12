from setting import *
import pygame
import pygame.image
import pygame.sprite
import pygame.mixer
import pygame.transform

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        self.idle_sprites = []
        self.idle_sprites.append(pygame.image.load('player_idle_0.png'))
        self.idle_sprites.append(pygame.image.load('player_idle_1.png'))
        self.idle_sprites.append(pygame.image.load('player_idle_2.png'))
        self.idle_sprites.append(pygame.image.load('player_idle_3.png'))
        self.idle_sprites.append(pygame.image.load('player_idle_4.png'))
        self.idle_sprites.append(pygame.image.load('player_idle_5.png'))
        self.idle_sprites.append(pygame.image.load('player_idle_6.png'))
        self.idle_sprites.append(pygame.image.load('player_idle_7.png'))
        self.idle_sprites.append(pygame.image.load('player_idle_8.png'))
        self.idle_sprites.append(pygame.image.load('player_idle_9.png'))
        self.idle_sprites.append(pygame.image.load('player_idle_10.png'))

        self.image = pygame.image.load('player_fall.png')
        self.rect = pygame.Rect(96,96,96,96)
        print(self.image.get_rect())
        # self.rect.x = 100
        # self.rect.y = 100

        self.state = 'idle'
        self.idle = 0
        
        self.isDoubleJump = False
        self.jumpCount = JUMP_COUNT
        self.standing = False
        self.jumping = False
        self.running = False
        self.falling = True
        self.lefting = True # can move left or not
        self.righting = True # can move right or not

    def update(self):
        if self.state == 'idle':
            if self.idle < len(self.idle_sprites) - 1:
                self.idle += 1
                self.image = self.idle_sprites[self.idle]
            else:
                self.idle = 0
        elif self.state == 'fall':
            self.image = pygame.image.load('player_fall.png')
        elif self.state == 'jump':
            self.image = pygame.image.load('player_jump.png')
        elif self.state == 'run':
            pass