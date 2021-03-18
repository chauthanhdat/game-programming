import pygame, sys
import pygame.display
import pygame.transform
import pygame.image
import pygame.time
import pygame.sprite
import pygame.font
import pygame.event
import pygame.mixer

import random

class Axe():
    pass

class Zombie(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('zombie.png')
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

class GameState():
    def __init__(self):
        self.state = 'intro'
        self.past_time = 0
        self.score = 0
        self.miss = 0
        self.bg = pygame.image.load('bg.png')
        self.axe = pygame.image.load('axe.png')
        self.explosion = pygame.transform.scale(pygame.image.load('explosion.png'),(100,100))
        self.zombie_idx = -1
        self.whack = False  
        self.whack_sound = pygame.mixer.Sound('whack.wav')

    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'main_game'
                self.past_time = pygame.time.get_ticks()

        
        ready_text = pixeboy_font.render('Ready ?', False, WHITE)
        text_rect = ready_text.get_rect(center=[screen_w/2, screen_h/2])
        screen.blit(ready_text, text_rect)

        pygame.display.flip()

    def main_game(self):
        pygame.mouse.set_visible(False)

        current_time = pygame.time.get_ticks()

        temp = current_time - self.past_time

        if temp >= 1000:
            self.whack = False
            if zombie_sprites:
                self.miss += 1
            zombie_sprites.empty()
            
            random_idx = random.randint(0,8)
            while random_idx == self.zombie_idx:
                random_idx = random.randint(0,8)
            self.zombie_idx = random_idx

            zombie_sprites.add(Zombie(zombie_pos[random_idx]))
            self.past_time = current_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.whack_sound.play().set_volume(.1)
                self.axe = pygame.transform.rotate(self.axe, -30)

                # xac dinh dap trung hay khong
                click_pos = pygame.mouse.get_pos()
                if click_pos[0] > zombie_pos[self.zombie_idx][0] and click_pos[0] < zombie_pos[self.zombie_idx][0] + 100:
                    if click_pos[1] > zombie_pos[self.zombie_idx][1] and click_pos[1] < zombie_pos[self.zombie_idx][1] + 100:
                        self.score += 1
                        zombie_sprites.empty()
                        self.whack = True

                        pygame.mixer.Sound('kick.wav').play().set_volume(30.5)

            if event.type == pygame.MOUSEBUTTONUP:
                self.axe = pygame.image.load('axe.png')

        # Drawing
        screen.blit(self.bg, (0,0))
        zombie_sprites.draw(screen)
        if self.whack:
            screen.blit(self.explosion, zombie_pos[self.zombie_idx])
        
        pos = pygame.mouse.get_pos()
        screen.blit(self.axe, (pos[0] - 75, pos[1] - 35))


        text = pixeboy_font.render("Score", False, (255,255,255))
        screen.blit(text, (10,10))
        text = pixeboy_font.render(": " + str(self.score), False, (255,255,255))
        screen.blit(text, (200,10))
        text = pixeboy_font.render("Miss", False, (255,255,255))
        screen.blit(text, (10,70))
        text = pixeboy_font.render(": " + str(self.miss), False, (255,255,255))
        screen.blit(text, (200,70))

        pygame.display.flip()

    def state_manager(self):
        if self.state == 'intro':
            self.intro()
        if self.state == 'main_game':
            self.main_game()

pygame.init()

#Screen
screen_w = 1280
screen_h = 720
size = (screen_w,screen_h)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Whack A Zombie')
pygame.display.set_icon(pygame.image.load('icon.png'))

clock = pygame.time.Clock()

# Color
WHITE = (255,255,255)
BLACK = (0,0,0)

game_state = GameState()
zombie_sprites = pygame.sprite.Group()
zombie_pos = [(385,125),(601,125),(817,125),(385,341),(601,341),(817,341),(385,557),(601,557),(817,557)]
pixeboy_font = pygame.font.Font('Pixeboy.ttf', 80)

pygame.mixer.music.load('bg (1).wav')
pygame.mixer.music.play(-1)

while True:
    game_state.state_manager()
    clock.tick(60)
    