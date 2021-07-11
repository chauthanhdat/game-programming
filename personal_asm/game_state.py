import sys
import pygame

import pygame.event
import pygame.sprite
import pygame.display
import pygame.image
import pygame.mask
import pygame.draw
import pygame.transform
import pygame.mouse
import pygame.mixer
import pygame.key
from pygame.constants import FULLSCREEN, KEYDOWN, K_DOWN, K_LEFT, K_RIGHT, K_SPACE, K_UP, RESIZABLE

from setting import *
from player import Player
from button import Button
from trap import Trap
from kiwi import Kiwi
from tiles import TileMap

class GameState:
    def __init__(self) -> None:
        self.state = 'main_menu'

        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])

        self.map = pygame.transform.scale(pygame.image.load('images/map.png'), [WIDTH,HEIGHT])
        self.map_mask = pygame.mask.from_surface(self.map)

        self.player = Player()
        self.player_mask = pygame.mask.from_surface(pygame.image.load('images/player_mask.png'))

        self.kiwi = pygame.sprite.Group()
        self.trap = pygame.sprite.Group()
        self.reset_level_1()

        self.player_jump_sound = pygame.mixer.Sound('sounds/jump.wav')
        self.player_collect_kiwi_sound = pygame.mixer.Sound('sounds/collect.wav')

        pygame.mixer.music.load('sounds/menu.wav')
        pygame.mixer.music.play(-1)

        m_test = TileMap()
        m_test.read_csv()

    def checkCollision(self):
        offset = (self.player.rect.x - self.map.get_rect().x, self.player.rect.y - self.map.get_rect().y)
        collision = self.map_mask.overlap(self.player_mask, offset)
        return collision

    def main_menu(self):
        title = pygame.image.load('images/title.png')
        btn_new = Button('images/btn_new_game.png',6)
        btn_option = Button('images/btn_option.png',7)
        btn_exit = Button('images/btn_exit.png',8)

        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_new.rect.x <= mouse_pos[0] <= btn_new.rect.x + btn_new.rect.width and btn_new.rect.y <= mouse_pos[1] <= btn_new.rect.y + btn_new.rect.height:
                    self.state = 'level_1'

                    pygame.mixer.music.load('sounds/theme.wav')
                    pygame.mixer.music.play(-1)

                elif btn_exit.rect.x <= mouse_pos[0] <= btn_exit.rect.x + btn_exit.rect.width and btn_exit.rect.y <= mouse_pos[1] <= btn_exit.rect.y + btn_exit.rect.height:
                    pygame.quit()
                    sys.exit()
        
        if btn_new.rect.x <= mouse_pos[0] <= btn_new.rect.x + btn_new.rect.width and btn_new.rect.y <= mouse_pos[1] <= btn_new.rect.y + btn_new.rect.height:
            btn_new.image = pygame.transform.scale(btn_new.image, [btn_new.rect.width+2, btn_new.rect.height+2])
        else:
            btn_new.image = pygame.transform.scale(btn_new.image, [btn_new.rect.width, btn_new.rect.height])

        if btn_option.rect.x <= mouse_pos[0] <= btn_option.rect.x + btn_option.rect.width and btn_option.rect.y <= mouse_pos[1] <= btn_option.rect.y + btn_option.rect.height:
            btn_option.image = pygame.transform.scale(btn_option.image, [btn_option.rect.width+2, btn_option.rect.height+2])
        else:
            btn_new.image = pygame.transform.scale(btn_new.image, [btn_new.rect.width, btn_new.rect.height])

        if btn_exit.rect.x <= mouse_pos[0] <= btn_exit.rect.x + btn_exit.rect.width and btn_exit.rect.y <= mouse_pos[1] <= btn_exit.rect.y + btn_exit.rect.height:
            btn_exit.image = pygame.transform.scale(btn_exit.image, [btn_exit.rect.width+2, btn_exit.rect.height+2])
        else:
            btn_exit.image = pygame.transform.scale(btn_exit.image, [btn_exit.rect.width, btn_exit.rect.height])

        self.screen.blit(pygame.image.load('images/bg.png'), (0,0))
        self.screen.blit(title, (WIDTH/2-title.get_width()/2, 48))
        self.screen.blit(btn_new.image, (btn_new.rect.x, btn_new.rect.y))
        self.screen.blit(btn_option.image, (btn_option.rect.x, btn_option.rect.y))
        self.screen.blit(btn_exit.image, (btn_exit.rect.x, btn_exit.rect.y))

    def level_1(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.state = 'pause_menu'
                if event.key == pygame.K_SPACE:
                    self.player.lefting = True
                    self.player.righting = True

                    if self.player.standing:
                        self.player.state = 'jump'
                        self.player.standing = False
                        self.player.jumping = True
                        self.player_jump_sound.play()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.player.running = False

        keys = key.get_pressed()
        if keys[K_LEFT]:
            if self.player.standing:
                self.player.running = True
                self.player.state = 'run'
            self.player.rect.x -= VELOCITY
            self.player.flip = True
            collision = self.checkCollision()
            if collision:
                if collision[0] >= self.player.rect.x and collision[1] >= self.player.rect.y:
                    self.player.lefting = False
                    while self.checkCollision():
                        self.player.rect.x += 1

        if keys[K_RIGHT]:
            if self.player.standing:
                self.player.running = True
                self.player.state = 'run'
            self.player.rect.x += VELOCITY
            self.player.flip = False
            collision = self.checkCollision()
            if collision:
                if collision[0] > self.player.rect.x and collision[1] >= self.player.rect.y:
                    self.player.righting = False
                    while self.checkCollision():
                        self.player.rect.x -= 1

        if pygame.sprite.spritecollide(self.player, self.kiwi, True):
            self.player_collect_kiwi_sound.play().set_volume(2)

        if pygame.sprite.spritecollideany(self.player, self.trap):
            self.reset_level_1()
            pass

        print(len(self.kiwi))

        if len(self.kiwi) == 0:
            self.reset_level_1()
            pygame.mixer.music.load('sounds/menu.wav')
            pygame.mixer.music.play(-1)
            self.state = 'main_menu'
        
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
        # /jump
        
        # gravity
        self.player.rect.y += GRAVITY
        collision = self.checkCollision()
        if collision:
            if collision[0] >= self.player.rect.x and collision[1] > self.player.rect.y:
                self.player.standing = True
                self.player.image = self.player.idle_sprites[self.player.idle]
                if not self.player.running:
                    self.player.state = 'idle'
                while self.checkCollision():
                    self.player.rect.y -= 1
        else:
            self.player.state = 'fall'
            # self.player.standing = False # can jump while fall
        # /gravity

        self.screen.blit(pygame.image.load('images/bg.png'), (0,0))
        self.screen.blit(self.map, (0,0)) # ground, wall
        self.player.update()
        self.screen.blit(self.player.image, (self.player.rect.x, self.player.rect.y))
        self.kiwi.update()
        self.kiwi.draw(self.screen)
        self.trap.draw(self.screen)
        pygame.display.flip()

        # print(self.player.state)

    def reset_level_1(self):
        self.kiwi.empty()
        self.kiwi.add(Kiwi(32*10, 32*3))
        self.kiwi.add(Kiwi(32*13, 32*3))
        self.kiwi.add(Kiwi(32*7, 32*3))
        self.kiwi.add(Kiwi(32*4, 32*3))
        for i in range(8,28):
            self.trap.add(Trap(16*i, 16*17))
        self.player.rect.x = 32*1
        self.player.rect.y = 32*7
        print('reset')

    def pause_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def level_2(self):
        pass

    def level_select(self):
        pass

    def state_manger(self):
        if self.state == 'main_menu':
            self.main_menu()
        if self.state == 'level_select':
            self.level_select()
        if self.state == 'level_1':
            self.level_1()
        if self.state == 'level_2':
            self.level_2()
        if self.state == 'pause_menu':
            self.pause_menu()