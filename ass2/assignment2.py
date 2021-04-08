from os import terminal_size
import pygame
import sys
from pygame import key
from pygame.constants import KEYDOWN, K_DOWN, K_LEFT, K_RIGHT, K_UP, K_a, K_d, K_s, K_w
from pygame.cursors import arrow
import pygame.display
import pygame.draw
from pygame.mixer import fadeout
import pygame.sprite
import pygame.image
import pygame.event

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, speed) -> None:
        super().__init__()
        self.image = pygame.image.load('data/b.png')
        self.rect = pygame.Rect(screen_w/2 - BALL_RADIUS, screen_h/2 - BALL_RADIUS, 2*BALL_RADIUS, 2*BALL_RADIUS)
        self.rect.x = x
        self.rect.y = y
        self.vel_x = 0
        self.vel_y = 0
        self.speed_x = speed[0]
        self.speed_y = speed[1]
        self.speed = speed

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        if self.rect.top <= 0 or self.rect.bottom >= screen_h:
            self.speed_y *= -1
        if self.rect.left <= 0:
            self.speed_x *= -1
            p2_score += 1
        if self.rect.right >= screen_w:
            p1_score += 1

class Player(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, row: int) -> None:
        super().__init__()

class Player_1(Player, pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, row: int) -> None:
        super().__init__(x, y, row)
        self.image = pygame.image.load('data/player_1.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.row = row

class Player_2(Player):
    def __init__(self, x: int, y: int, row: int) -> None:
        super().__init__(x, y, row)
        self.image = pygame.image.load('data/player_2.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.row = row

class Arrow(pygame.sprite.Sprite):
    def __init__(self, x, y, image) -> None:
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class GameState:
    p1_current_row = 2
    p2_current_row = 2
    p1_can_move_up = True
    P1_can_move_down = True
    p2_can_move_up = True
    p2_can_move_down = True

    def __init__(self):
        self.state = 'main_game'

    def intro(self):
        pass

    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.p1_can_move_up = True
                    self.p1_can_move_down = True
                    if self.p1_current_row > 0:
                        self.p1_current_row -= 1
                elif event.key == pygame.K_d:
                    self.p1_can_move_up = True
                    self.p1_can_move_down = True
                    if self.p1_current_row < 3:
                        self.p1_current_row += 1
                elif event.key == pygame.K_RIGHT:
                    self.p2_can_move_up = True
                    self.p2_can_move_down = True
                    if self.p2_current_row > 0:
                        self.p2_current_row -= 1
                elif event.key == pygame.K_LEFT:
                    self.p2_can_move_up = True
                    self.p2_can_move_down = True
                    if self.p2_current_row < 3:
                        self.p2_current_row += 1
        # Control
        keys = key.get_pressed()

        # P1 control
        if keys[K_w]:
            self.p1_can_move_up = True
            for player in player_sprites:
                if player.rect.top <= 0 and player.row == self.p1_current_row:
                    self.p1_can_move_up = False
                    break

            for player in player_sprites:
                if type(player) is Player_1:
                    if player.row == self.p1_current_row:
                        if self.p1_can_move_up:
                            player.rect.y -= 10
        if keys[K_s]:
            self.p1_can_move_down = True
            for player in player_sprites:
                if player.rect.bottom >= screen_h and player.row == self.p1_current_row:
                    self.p1_can_move_down = False
                    break

            for player in player_sprites:
                if type(player) is Player_1:
                    if player.row == self.p1_current_row:
                        if self.p1_can_move_down:
                            player.rect.y += 10
        # P2 control
        if keys[K_UP]:
            self.p2_can_move_up = True
            for player in player_sprites:
                if player.rect.top <= 0 and player.row == self.p2_current_row:
                    self.p2_can_move_up = False
                    break

            for player in player_sprites:
                if type(player) is Player_2:
                    if player.row == self.p2_current_row:
                        if self.p2_can_move_up:
                            player.rect.y -= 10
        if keys[K_DOWN]:
            self.p2_can_move_down = True
            for player in player_sprites:
                if player.rect.bottom >= screen_h and player.row == self.p2_current_row:
                    self.p2_can_move_down = False
                    break

            for player in player_sprites:
                if type(player) is Player_2:
                    if player.row == self.p2_current_row:
                        if self.p2_can_move_down:
                            player.rect.y += 10
        
        # check ball collision
        for ball_1 in ball_sprites:
            for ball_2 in ball_sprites:
                if ball_1 != ball_2:
                    delta_x = ball_1.rect.x - ball_2.rect.x
                    delta_y = ball_1.rect.y - ball_2.rect.y
                    
                    if delta_x * delta_x + delta_y * delta_y <= BALL_RADIUS * BALL_RADIUS * 4:
                        if type(ball_1) is Ball:
                            ball_1.speed_x *= -1
                            ball_1.speed_y *= -1

        gc = pygame.sprite.groupcollide(ball_sprites, player_sprites, False, False)
        
        for ball in ball_sprites:
            if type(ball) is Ball and ball in gc:
                player = gc[ball][0]
                
                if abs(player.rect.top - ball.rect.bottom) < 10:
                    ball.speed_y *= -1
                if abs(player.rect.bottom - ball.rect.top) < 10:
                    ball.speed_y *= -1
                if abs(player.rect.right - ball.rect.left) < 10:
                    ball.speed_x *= -1
                if abs(player.rect.left - ball.rect.right) < 10:
                    ball.speed_x *= -1

        # draws
        screen.blit(bg, (0,0))
        ball_sprites.draw(screen)
        ball_sprites.update()
        player_sprites.draw(screen)
        player_sprites.update()
        
        arrow_sprites.empty()
        if self.p1_current_row == 0:
            arrow_sprites.add(Arrow(112,10,'data/arrow_1.png'))
        elif self.p1_current_row == 1:
            arrow_sprites.add(Arrow(262,10,'data/arrow_1.png'))
        elif self.p1_current_row == 2:
            arrow_sprites.add(Arrow(562,10,'data/arrow_1.png'))
        elif self.p1_current_row == 3:
            arrow_sprites.add(Arrow(862,10,'data/arrow_1.png'))
        if self.p2_current_row == 0:
            arrow_sprites.add(Arrow(1162,10,'data/arrow_2.png'))
        elif self.p2_current_row == 1:
            arrow_sprites.add(Arrow(1012,10,'data/arrow_2.png'))
        elif self.p2_current_row == 2:
            arrow_sprites.add(Arrow(712,10,'data/arrow_2.png'))
        elif self.p2_current_row == 3:
            arrow_sprites.add(Arrow(412,10,'data/arrow_2.png'))
        arrow_sprites.draw(screen)

    def state_manager(self):
        if self.state == 'intro':
            self.intro()
        if self.state == 'main_game':
            self.main_game()

WHITE = (255,255,255)
BLACK = (0,0,0)
BALL_RADIUS = 10

pygame.init()
clock = pygame.time.Clock()

screen_w = 1280
screen_h = 720
screen = pygame.display.set_mode([screen_w, screen_h])
pygame.display.set_caption('Double Ball')

bg = pygame.image.load('data/bg.png')

game_state = GameState()

ball_sprites = pygame.sprite.Group()
sp = 2
ball_sprites.add(Ball(screen_w/2,100,(1*sp,2*sp)), Ball(screen_w/2,200,(-2*sp,-3*sp)))

p1_score = 0
p2_score = 0

player_sprites = pygame.sprite.Group()
player_sprites.add(Player_1(100, 300, 0))
player_sprites.add(Player_1(250, 150, 1), Player_1(250, 450, 1))
player_sprites.add(Player_2(400, 100, 3), Player_2(400, 300, 3), Player_2(400, 500, 3))
player_sprites.add(Player_1(550, 150, 2), Player_1(550, 300, 2), Player_1(550, 450, 2), Player_1(550, 600, 2))
player_sprites.add(Player_2(700, 150, 2), Player_2(700, 300, 2), Player_2(700, 450, 2), Player_2(700, 600, 2))
player_sprites.add(Player_1(850, 100, 3), Player_1(850, 300, 3), Player_1(850, 500, 3))
player_sprites.add(Player_2(1000, 150, 1), Player_2(1000, 450, 1))
player_sprites.add(Player_2(1150, 300, 0))

arrow_sprites = pygame.sprite.Group()

while True:
    game_state.state_manager()

    pygame.display.flip()
    clock.tick(60)
