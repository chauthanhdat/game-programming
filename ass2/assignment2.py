import pygame
import sys
import pygame.display
import pygame.draw

class Ball:
    def __init__(self) -> None:
        self.speed_x = 1
        self.speed_y = 1
        pass
    pass


class GameState:
    def __init__(self):
        self.state = 'main_game'
        self.speed_x = 5
        self.speed_y = 10

    def intro(self):
        pass

    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        ball.x += self.speed_x
        ball.y += self.speed_y

        if ball.top <= 0 or ball.bottom >= screen_h:
            self.speed_y *= -1
        if ball.left <= 0 or ball.right >= screen_w:
            self.speed_x *= -1

        screen.fill(LIGHT_GRAY)
        pygame.draw.ellipse(screen, BLACK, ball)

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
ball = pygame.Rect(screen_w/2 - BALL_RADIUS, screen_h/2 - BALL_RADIUS, 2*BALL_RADIUS, 2*BALL_RADIUS)
pygame.display.set_caption('Double Ball')



game_state = GameState()

while True:
    game_state.state_manager()

    pygame.display.flip()
    clock.tick(60)
