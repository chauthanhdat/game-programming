from os import terminal_size
from typing import final
import pygame, sys
import pygame.constants
import pygame.display
import pygame.transform
import pygame.image
import pygame.time
import pygame.sprite
import pygame.font
import pygame.event
import pygame.mixer
import random

class Zombie(pygame.sprite.Sprite):
    def __init__(self, idx):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('data/zombie_0.png'))
        self.sprites.append(pygame.image.load('data/zombie_1.png'))
        self.sprites.append(pygame.image.load('data/zombie_2.png'))
        self.sprites.append(pygame.image.load('data/zombie_3.png'))
        self.sprites.append(pygame.image.load('data/zombie_4.png'))
        self.sprites.append(pygame.image.load('data/zombie_5.png'))
        self.sprites.append(pygame.image.load('data/zombie_6.png'))
        self.sprites.append(pygame.image.load('data/zombie_7.png'))
        self.sprites.append(pygame.image.load('data/zombie_8.png'))
        self.sprites.append(pygame.image.load('data/zombie_9.png'))
        self.current_sprite = 0

        self.index = idx
        self.isDie = False
        self.spawn_time = pygame.time.get_ticks()

        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.x = AVAILABLE_POS[idx][0]
        self.rect.y = AVAILABLE_POS[idx][1]
    
    def update(self):
        if self.isDie:
            if self.current_sprite > 0:
                self.current_sprite -= 1
                self.image = self.sprites[self.current_sprite]
        else:
            if self.current_sprite < len(self.sprites) - 1:
                self.current_sprite += 1
                self.image = self.sprites[self.current_sprite]

class Hit(pygame.sprite.Sprite):
    def __init__(self, idx):
        super().__init__()
        self.image = pygame.image.load('data/hit.png')
        self.rect = self.image.get_rect()
        self.rect.x = AVAILABLE_POS[idx][0]
        self.rect.y = AVAILABLE_POS[idx][1]
        self.spawn_time = pygame.time.get_ticks()
        
class GameState():
    def __init__(self):
        self.state = 'intro'
        self.score = 0
        self.miss = 0
        self.available_idx = [True,True,True,True,True,True,True,True,True]
        self.zombie_spawn_time = 3000
        self.prev_zombie_spawn_time = 0

        self.bg_img = pygame.image.load('data/bg.png')
        self.axe_img = pygame.image.load('data/axe.png')
        
        self.whack_sound = pygame.mixer.Sound('data/whack.wav')
        self.hit_sound = pygame.mixer.Sound('data/kick.wav')
        

    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'main_game'
                self.prev_zombie_spawn_time = pygame.time.get_ticks() - 2000

                pygame.mixer.music.load('data/bg.wav')
                pygame.mixer.music.play(-1)

        # <Drawing>
        ready_text = pixeboy_font.render('Ready ?', False, WHITE)
        text_rect = ready_text.get_rect(center=[screen_w/2, screen_h/2])
        screen.blit(ready_text, text_rect)

        pygame.display.flip()
        # </Drawing>

    def main_game(self):
        pygame.mouse.set_visible(False)

        current_time = pygame.time.get_ticks()
        past_time = current_time - self.prev_zombie_spawn_time

        if past_time >= self.zombie_spawn_time:
            if self.zombie_spawn_time > 500:
                self.zombie_spawn_time -= 100
            
            # Zombie khong xuat hien tai vi tri cu
            random_idx = random.randint(0,8)
            while not self.available_idx[random_idx]:
                random_idx = random.randint(0,8)
            self.available_idx[random_idx] = False
            zombie_sprites.add(Zombie(random_idx))

            self.prev_zombie_spawn_time = current_time

        for _ in hit_sprites:
            if type(_) is Hit:
                if current_time - _.spawn_time >= HIT_LIFE_CYCLE:
                    hit_sprites.remove(_)

        for _ in zombie_sprites:
            if type(_) is Zombie:
                if _.isDie:
                    if _.current_sprite == 0:
                        self.available_idx[_.index] = True
                        zombie_sprites.remove(_)
                elif current_time - _.spawn_time >= ZOMBIE_LIFE_CYCLE:
                    _.isDie = True
                    self.miss += 1
                    if self.miss >= 10:
                        self.state = 'play_again'

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.whack_sound.play().set_volume(0.1)
                self.axe_img = pygame.transform.rotate(self.axe_img, -30)

                # Check hit Zombie or not
                click_pos = pygame.mouse.get_pos()
                for _ in zombie_sprites:
                    if type(_) is Zombie:
                        if _.rect.collidepoint(click_pos) and not _.isDie:
                            _.isDie = True
                            self.score += 1
                            self.hit_sound.play()
                            hit_sprites.add(Hit(_.index))

            if event.type == pygame.MOUSEBUTTONUP:
                self.axe_img = pygame.image.load('data/axe.png')

        # <Drawing>
        screen.blit(self.bg_img, (0,0))

        zombie_sprites.draw(screen)
        zombie_sprites.update()
        hit_sprites.draw(screen)
        
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(self.axe_img, (mouse_pos[0] - 75, mouse_pos[1] - 35))

        draw_text("Score", (10,10))
        draw_text(": " + str(self.score), (200,10))
        draw_text("Miss", (10,70))
        draw_text(": " + str(self.miss), (200,70))

        pygame.display.flip()
        # </Drawing>
    
    def play_again(self):
        pygame.mouse.set_visible(True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.state = 'main_game'
                    self.score = 0
                    self.miss = 0
                    self.available_idx = [True,True,True,True,True,True,True,True,True]
                    self.zombie_spawn_time = 3000
                    self.prev_zombie_spawn_time = pygame.time.get_ticks() - 2000

                    zombie_sprites.empty()
                    hit_sprites.empty()

        # <Drawing>
        ready_text = pixeboy_font.render('PLAY AGAIN', False, WHITE)
        text_rect = ready_text.get_rect(center=[screen_w/2, screen_h/2])
        screen.blit(ready_text, text_rect)

        pygame.display.flip()
        # </Drawing>


    def state_manager(self):
        if self.state == 'intro':
            self.intro()
        if self.state == 'main_game':
            self.main_game()
        if self.state == 'play_again':
            self.play_again()

def draw_text(text, dest):
    screen.blit(pixeboy_font.render(text, False, WHITE), dest)


pygame.init()

# Set up
screen_w = 1280
screen_h = 720
size = (screen_w,screen_h)
screen = pygame.display.set_mode(size)
pixeboy_font = pygame.font.Font('data/Pixeboy.ttf', 80)
clock = pygame.time.Clock()

pygame.display.set_caption('Whack A Zombie')
pygame.display.set_icon(pygame.image.load('data/icon.png'))

# <Define>
WHITE = (255,255,255)
BLACK = (0,0,0)

ZOMBIE_LIFE_CYCLE = 2000
HIT_LIFE_CYCLE = 200
AVAILABLE_POS = [(385,125),(601,125),(817,125),(385,341),(601,341),(817,341),(385,557),(601,557),(817,557)]
# </Define>

game_state = GameState()

zombie_sprites = pygame.sprite.Group()
hit_sprites = pygame.sprite.Group()

while True:
    game_state.state_manager()
    clock.tick(60)
