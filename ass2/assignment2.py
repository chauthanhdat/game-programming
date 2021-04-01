import pygame
import sys
import pygame.display
import pygame.draw
import pygame.sprite
import pygame.image

class Ball(pygame.sprite.Sprite):
    def __init__(self, speed) -> None:
        super().__init__()
        self.image = pygame.image.load('data/ball.png')
        self.rect = pygame.Rect(screen_w/2 - BALL_RADIUS, screen_h/2 - BALL_RADIUS, 2*BALL_RADIUS, 2*BALL_RADIUS)
        self.rect.x = screen_w/2
        self.rect.y = screen_h/2
        self.speed_x = speed[0]
        self.speed_y = speed[1]

class GameState:
    def __init__(self):
        self.state = 'main_game'

    def intro(self):
        pass

    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for _ in ball_sprites:
            if type(_) is Ball:
                _.rect.x += _.speed_x
                _.rect.y += _.speed_y
                
                if _.rect.top <= 0 or _.rect.bottom >= screen_h:
                    _.speed_y *= -1
                if _.rect.left <= 0 or _.rect.right >= screen_w:
                    _.speed_x *= -1

        screen.fill(LIGHT_GRAY)
        ball_sprites.draw(screen)

    def state_manager(self):
        if self.state == 'intro':
            self.intro()
        if self.state == 'main_game':
            self.main_game()

WHITE = (255,255,255)
LIGHT_GRAY = (200,200,200)
BLACK = (0,0,0)
BALL_RADIUS = 50

pygame.init()
clock = pygame.time.Clock()

screen_w = 1280
screen_h = 720
screen = pygame.display.set_mode([screen_w, screen_h])
pygame.display.set_caption('Double Ball')

game_state = GameState()
ball_sprites = pygame.sprite.Group()

ball_sprites.add(Ball((1,2)), Ball((-2,-3)))

while True:
    game_state.state_manager()

    pygame.display.flip()
    clock.tick(60)
