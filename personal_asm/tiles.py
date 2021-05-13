from setting import HEIGHT, TILE_SIZE, WIDTH
import pygame, csv, os
import pygame.sprite

class Tile(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        
class TileMap:
    def __init__(self) -> None:
        self.tile_size = 32
        self.start_x = 0
        self.start_y = 0

    def read_csv(self):
        self.map = []
        with open(os.path.join("large_map.csv")) as data:
            csv_reader = csv.reader(data, delimiter=',')
            for row in csv_reader:
                self.map.append(row)

        self.tile_width = len(self.map[0])
        self.tile_height = len(self.map)

        self.width = self.tile_width * TILE_SIZE
        self.height = self.tile_height * TILE_SIZE

class Camera:
    def __init__(self, width, height) -> None:
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT / 2)
        self.camera = pygame.Rect(x, y, self.width, self.height)