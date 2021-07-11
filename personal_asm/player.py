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
        self.idle_sprites.append(pygame.image.load('images/player_idle_0.png'))
        self.idle_sprites.append(pygame.image.load('images/player_idle_1.png'))
        self.idle_sprites.append(pygame.image.load('images/player_idle_2.png'))
        self.idle_sprites.append(pygame.image.load('images/player_idle_3.png'))
        self.idle_sprites.append(pygame.image.load('images/player_idle_4.png'))
        self.idle_sprites.append(pygame.image.load('images/player_idle_5.png'))
        self.idle_sprites.append(pygame.image.load('images/player_idle_6.png'))
        self.idle_sprites.append(pygame.image.load('images/player_idle_7.png'))
        self.idle_sprites.append(pygame.image.load('images/player_idle_8.png'))
        self.idle_sprites.append(pygame.image.load('images/player_idle_9.png'))
        self.idle_sprites.append(pygame.image.load('images/player_idle_10.png'))
        self.idle = 0

        self.run_sprites = []
        self.run_sprites.append(pygame.image.load('images/player_run_0.png'))
        self.run_sprites.append(pygame.image.load('images/player_run_1.png'))
        self.run_sprites.append(pygame.image.load('images/player_run_2.png'))
        self.run_sprites.append(pygame.image.load('images/player_run_3.png'))
        self.run_sprites.append(pygame.image.load('images/player_run_4.png'))
        self.run_sprites.append(pygame.image.load('images/player_run_5.png'))
        self.run_sprites.append(pygame.image.load('images/player_run_6.png'))
        self.run_sprites.append(pygame.image.load('images/player_run_7.png'))
        self.run_sprites.append(pygame.image.load('images/player_run_8.png'))
        self.run_sprites.append(pygame.image.load('images/player_run_9.png'))
        self.run_sprites.append(pygame.image.load('images/player_run_10.png'))
        self.run_sprites.append(pygame.image.load('images/player_run_11.png'))
        self.run = 0

        self.image = pygame.image.load('images/player_fall.png')
        self.rect = pygame.Rect(32*1, 32*7,32,32)

        self.state = 'fall'
        
        self.isDoubleJump = False
        self.jumpCount = JUMP_COUNT
        self.standing = False
        self.jumping = False
        self.running = False
        self.falling = True

        self.flip = False

    def update(self):
        if self.state == 'idle':
            if self.idle < len(self.idle_sprites) - 1:
                self.idle += 1
            else:
                self.idle = 0

            if self.flip:
                self.image = pygame.transform.flip(self.idle_sprites[self.idle], True, False)
            else:
                self.image = self.idle_sprites[self.idle]

        elif self.state == 'fall':
            if self.flip:
                self.image = pygame.transform.flip(pygame.image.load('images/player_fall.png'), True, False)
            else:
                self.image = pygame.image.load('images/player_fall.png')

        elif self.state == 'jump':
            if self.flip:
                self.image = pygame.transform.flip(pygame.image.load('images/player_jump.png'), True, False)
            else:
                self.image = pygame.image.load('images/player_jump.png')

        elif self.state == 'run':
            if self.run < len(self.run_sprites) - 1:
                self.run += 1
            else:
                self.run = 0
                
            if self.flip:
                self.image = pygame.transform.flip(self.run_sprites[self.run], True, False)
            else:
                self.image = self.run_sprites[self.run]