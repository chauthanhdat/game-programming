import pygame
import pygame.time
pygame.init()

clock = pygame.time.Clock
past = pygame.time.get_ticks()
current = 0

while True:
    current = pygame.time.get_ticks()
    if (current - past >= 1000):
        print(str(current//1000) + ' ' + str(current))
        past = current
