import pygame
from pygame import mouse
from pygame.image import tostring
pygame.init()
pygame.font.init()

size = (1280,720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Whack A Zombie")
# pygame.mouse.set_visible(False)

carryOn = True
clock = pygame.time.Clock()

bg = pygame.transform.scale(pygame.image.load("bg.png"), size)
axe = pygame.transform.scale(pygame.image.load('axe.png'), (100,100))
pixeboy_font = pygame.font.Font("Pixeboy.ttf", 80)

score = 0
miss = 0

while carryOn:
    screen.blit(bg, [0,0])
    # screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            axe = pygame.transform.rotate(axe, -30)

            if event.button == 1:
                score += 1
            if event.button == 3:
                miss += 1

            pos = pygame.mouse.get_pos()
            print(pos)

        if event.type == pygame.MOUSEBUTTONUP:
            axe = pygame.transform.scale(pygame.image.load('axe.png'), (100,100))

    pos = pygame.mouse.get_pos()
    screen.blit(axe, (-axe.get_size()[0]/2 + pos[0], -axe.get_size()[1]/2 + pos[1]))

    text = pixeboy_font.render("Score", False, (255,255,255))
    screen.blit(text, (10,10))
    text = pixeboy_font.render(": " + str(score), False, (255,255,255))
    screen.blit(text, (200,10))
    text = pixeboy_font.render("Miss", False, (255,255,255))
    screen.blit(text, (10,70))
    text = pixeboy_font.render(": " + str(miss), False, (255,255,255))
    screen.blit(text, (200,70))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()