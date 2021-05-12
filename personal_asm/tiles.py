import pygame, csv, os
import pygame.sprite

class Tile(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        
class TileMap():
    def __init__(self) -> None:
        self.tile_size = 48
        self.start_x = 0
        self.start_y = 0

    def read_csv(self):
        map = []
        with open(os.path.join("map.csv")) as data:
            data = csv.reader(data)