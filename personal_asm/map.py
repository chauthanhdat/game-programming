from setting import SCREEN_HEIGHT, TILE_SIZE, SCREEN_WIDTH
import pygame, csv, os
import pygame.sprite
import pygame.image

class Map():
    def __init__(self):
        self.obstacle_list = []

        # store tile
        self.tile_list = []
        for i in range(10):
            img = pygame.image.load(f'images/tiles/{i}.png')
            self.tile_list.append(img)

    def process_data(self, data):
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if tile >= 0:
                    img = self.tile_list[tile]
                    img_rect = img.get_rect()
                    img_rect.x = x * TILE_SIZE
                    img_rect.y = y * TILE_SIZE
                    tile_data = (img, img_rect)

                    if True:
                        self.obstacle_list.append(tile_data)
    
    def draw(self, screen):
        for tile in self.obstacle_list:
            screen.blit(tile[0], tile[1])