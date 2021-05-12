from os import terminal_size
import sys
import pygame
from pygame import key
from pygame import scrap
from pygame.constants import FULLSCREEN, KEYDOWN, K_DOWN, K_LEFT, K_RIGHT, K_SPACE, K_UP, RESIZABLE
import pygame.event
import pygame.sprite
import pygame.display
import pygame.image
import pygame.mask
import pygame.draw
import pygame.transform

from setting import *
from player import Player

class GameState:
    def __init__(self) -> None:
        self.state = 'main_game'

        self.screen_w = WIDTH
        self.screen_h = HEIGHT
        self.screen_size = (self.screen_w, self.screen_h)
        self.screen = pygame.display.set_mode(self.screen_size)

        self.map = pygame.transform.scale(pygame.image.load('map.png'), [WIDTH,HEIGHT])
        self.map_mask = pygame.mask.from_surface(self.map)

        self.player = Player()
        self.player_mask = pygame.mask.from_surface(pygame.image.load('player_mask.png'))

    def checkCollision(self):
        offset = (self.player.rect.x - self.map.get_rect().x, self.player.rect.y - self.map.get_rect().y)
        collision = self.map_mask.overlap(self.player_mask, offset)
        return collision

    def main_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.state = 'pause_menu'
                if event.key == pygame.K_SPACE:
                    pass

        keys = key.get_pressed()
        if keys[K_LEFT]:
            # self.player.righting = True
            # if self.player.lefting:
                self.player.rect.x -= VELOCITY
                collision = self.checkCollision()
                if collision:
                    if collision[0] >= self.player.rect.x and collision[1] >= self.player.rect.y:
                        self.player.lefting = False
                        while self.checkCollision():
                            self.player.rect.x += 1

        if keys[K_RIGHT]:
            # self.player.lefting = True
            # if self.player.righting:
                self.player.rect.x += VELOCITY
                collision = self.checkCollision()
                if collision:
                    if collision[0] > self.player.rect.x and collision[1] >= self.player.rect.y:
                        self.player.righting = False
                        while self.checkCollision():
                            self.player.rect.x -= 1

        if keys[K_SPACE]:
            self.player.lefting = True
            self.player.righting = True

            if self.player.standing:
                self.player.state = 'jump'
                self.player.standing = False
                self.player.jumping = True
        
        # jump
        if self.player.jumping:
            if self.player.jumpCount > 0:
                self.player.rect.y -= (self.player.jumpCount * self.player.jumpCount) * 0.5
                self.player.jumpCount -= 1
                collision = self.checkCollision()
                if collision:
                    # if collision[0] == self.player.rect.left and collision[1] >= self.player.rect.top:
                        self.player.jumpCount = JUMP_COUNT
                        self.player.jumping = False
                        while self.checkCollision():
                            self.player.rect.y += 1
            else:
                self.player.jumpCount = JUMP_COUNT
                self.player.jumping = False
                self.player.state = 'fall'
                # self.player.standing = True
        # /jump
        
        # gravity
        self.player.rect.y += GRAVITY
        collision = self.checkCollision()
        if collision:
            if collision[0] >= self.player.rect.x and collision[1] > self.player.rect.y:
                self.player.standing = True
                self.player.image = self.player.idle_sprites[self.player.idle]
                self.player.state = 'idle'
                while self.checkCollision():
                    self.player.rect.y -= 1
        # /gravity

        self.screen.fill(pygame.Color(255,255,255)) # background
        self.screen.blit(self.map, (0,0)) # ground, wall
        self.player.update()
        self.screen.blit(self.player.image, (self.player.rect.x, self.player.rect.y))

        if self.checkCollision():
            pygame.draw.circle(self.screen, pygame.Color(0,0,0), self.checkCollision(), 3, 3)
        pygame.display.flip()

    def pause_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def state_manger(self):
        if self.state == 'main_menu':
            self.main_menu()
        if self.state == 'main_game':
            self.main_game()
        if self.state == 'pause_menu':
            self.pause_menu()